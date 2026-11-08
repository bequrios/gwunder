FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY app/ ./app/

RUN pip install --no-cache-dir uv && \
    uv sync --frozen --no-dev

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "60", "main:app"]
