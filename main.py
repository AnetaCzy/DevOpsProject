from flask import Flask, request, redirect, url_for, render_template_string
import psycopg2
import os

app = Flask(__name__)

# Function to get a database connection
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

# Ensure the feedback table exists
def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100),
            feedback TEXT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

create_table()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Employee Feedback</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        form { margin-bottom: 30px; }
        input, textarea { display: block; margin-bottom: 10px; width: 300px; padding: 5px; }
        table { border-collapse: collapse; width: 80%; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Employee Feedback</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="text" name="department" placeholder="Department" required>
        <textarea name="feedback" placeholder="Your Feedback" rows="4" required></textarea>
        <button type="submit">Submit Feedback</button>
    </form>

    <h2>All Feedback</h2>
    <table>
        <tr>
            <th>Name</th>
            <th>Department</th>
            <th>Feedback</th>
        </tr>
        {% for f in feedbacks %}
        <tr>
            <td>{{ f[0] }}</td>
            <td>{{ f[1] }}</td>
            <td>{{ f[2] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        name = request.form.get('name')
        department = request.form.get('department')
        feedback_text = request.form.get('feedback')
        if name and department and feedback_text:
            cur.execute(
                "INSERT INTO feedback (name, department, feedback) VALUES (%s, %s, %s);",
                (name, department, feedback_text)
            )
            conn.commit()
        return redirect(url_for('home'))

    cur.execute("SELECT name, department, feedback FROM feedback ORDER BY id DESC;")
    feedbacks = cur.fetchall()
    cur.close()
    conn.close()

    return render_template_string(HTML_TEMPLATE, feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

