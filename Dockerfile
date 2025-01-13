#FROM nginx:latest

#Path: /usr/share/nginx/html
#COPY /html /usr/share/nginx/html

FROM python:3.12-alphine3.17

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ];