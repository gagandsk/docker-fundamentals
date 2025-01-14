FROM nginx:latest
COPY /sitio /usr/share/nginx/html
#VOLUME ["/sitio", "/usr/share/nginx/html"]

#------> app.py
#FROM python:3.12-alphine3.17
#WORKDIR /app
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#COPY . .
#CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ];
