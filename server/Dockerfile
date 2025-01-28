FROM python:3.11-alpine

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry && poetry install --no-root

COPY . .

CMD ["sh", "-c", "poetry run python manage.py migrate && poetry run python manage.py runserver 0.0.0.0:8000"]
