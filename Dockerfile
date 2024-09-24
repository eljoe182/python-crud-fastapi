# Usa una imagen base de Python 3.10
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo pyproject.toml y poetry.lock (si existe) a la imagen
COPY pyproject.toml poetry.lock* /app/

# Actualiza pip y Poetry
RUN pip install --upgrade pip \
    && pip install poetry

# Instala las dependencias del proyecto usando Poetry sin crear un virtualenv
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copia el código de la aplicación en el contenedor
COPY . /app

# Expone el puerto en el que correrá el servicio FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn
CMD ["pyhton", "-m", "app.server"]
