# Usa una imagen oficial de Python para ejecutar el servidor Flask
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias necesarias
RUN pip install Flask

# Exponer el puerto en el que el servidor Flask estará corriendo
EXPOSE 5000

# Comando para ejecutar el servidor Flask
CMD ["python", "app.py"]
