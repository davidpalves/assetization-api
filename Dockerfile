FROM python:3.11-slim
ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry

COPY . .

RUN ls -la

RUN apt update && apt-get install -y python3-dev \
                        gcc \
                        libc-dev \
                        libffi-dev


RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

RUN alembic upgrade head

EXPOSE 8000
CMD [ "poetry", "run", "uvicorn", "--host", "0.0.0.0", "todo_api.app:app" ]