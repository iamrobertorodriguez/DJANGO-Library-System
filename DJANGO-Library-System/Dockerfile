FROM python:3.11

# Instalar dependencias necesarias para Poetry y Git
RUN apt-get update \
    && apt-get install -y curl

# Agregar el directorio de la aplicación al contenedor
WORKDIR /app

ENV POETRY_HOME=/opt/poetry
ENV PATH="${POETRY_HOME}/bin:${PATH}"
ENV PORT=8010
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false
# RUN poetry config virtualenvs.in-project true

# Copiar los archivos necesarios al contenedor
COPY pyproject.toml poetry.lock /app/

# Instalar las dependencias utilizando Poetry
COPY ./library /app/library
RUN poetry install
# RUN ~/.poetry/bin/poetry install --no-dev

# Copiar todo el código fuente de la aplicación al contenedor
COPY . /app

# RUN poetry run python manage.py collectstatic --no-input

# Iniciar la aplicación con make y correr migraciones
CMD ["make", "run"]
