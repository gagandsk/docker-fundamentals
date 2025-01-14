```
docker build -t sitioweb:latest .
```
```
docker run -it --rm -d -p 8080:80 --name web sitioweb
```

### DockerFile

**WORKDIR** = ubicacion donde se creara la aplicacion
**COP**Y = copiar archivo local al entorno docker
**RUN** = ejecutar un comando dentro del contenedor
**COPY . .**= copiamos los fuentes dentro del WORKDIR especificado
**CMD** = ejecutar comando sh

http://localhost:8080/linktree.html

Entorno virtual Python:
```
python -m venv NOMBRE_ENTORNO
```

Activamos el entorno
```
source NOMBRE_ENTORNO/bin/activate
```

Salimos del entorno
````
deactivate
```

Configurar volúmenes básicos en Docker
```
docker run -it --rm -d -p 8080:80 -v ./sitio:/usr/share/nginx/html/sitio --name web nginx
```