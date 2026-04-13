# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos de nuestro proyecto al contenedor
COPY . .

# Instalamos las dependencias necesarias
RUN pip install flask pybuilder

# Exponemos el puerto que usa la app
EXPOSE 5000

# Comando para arrancar la aplicación
CMD ["python", "inventory.py"]
