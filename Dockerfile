WORKDIR /app
 
RUN apt update && apt install -y git
 
RUN git clone https://github.com/AnetaCzy/DevOpsProject.git .
 
RUN pip install Flask

CMD ["python", "main.py"]]
