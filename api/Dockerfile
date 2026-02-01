# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app

# Copiamos sólo requirements
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos la app
COPY . .

# Stage 2: Runtime
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copiamos solo lo necesario desde builder
COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "app.py"]
