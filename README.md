Used commands:
  1) docker --version 
  2) vi main.py 
  3) vi requirements.txt 
  4) vi Dockerfile 
  5) docker build -t python-app .
  6) docker container run -d \
      --name postgres-db \
      -e POSTGRES_USER=myuser \
      -e POSTGRES_PASSWORD=mypassword \
      -e POSTGRES_DB=mydatabase \
      -v pgdata:/var/lib/postgresql/data \
      postgres:15-alpine
  7) docker container run -d \ 
      --name python-app \ 
      -p 8080:8080 \ 
      --link postgres-db:db \ 
      -e POSTGRES_HOST=db \ 
      -e POSTGRES_DB=mydatabase \ 
      -e POSTGRES_USER=myuser \ 
      -e POSTGRES_PASSWORD=mypassword \ 
      python-app 
  8) docker run -d \python-app 

<img width="697" height="91" alt="final_run" src="https://github.com/user-attachments/assets/04355651-acb1-43ea-bd79-3750a4289dc8" />
<img width="1455" height="157" alt="final_containers" src="https://github.com/user-attachments/assets/1d8fb236-1d6b-49de-9f10-9af5afef3a9d" />


