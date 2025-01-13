```
docker build -t sitioweb:latest .
```
```
docker run -it --rm -d -p 8080:80 --name web sitioweb
```

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