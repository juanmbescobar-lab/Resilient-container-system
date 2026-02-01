# Build Optimization Analysis

## Naive Dockerfile
- Base: python:3.11
- Image size: ~1.2GB
- Build time: ~30s
- Cache behavior: changing app.py invalidated pip install
- Observations: naive Dockerfile rebuilds full dependencies even for small code changes

## Optimized Dockerfile
- Base: python:3.11-slim
- Image size: ~300MB
- Build time: ~15s
- Cache behavior: changing app.py does not reinstall dependencies
- Observations: separating COPY requirements.txt and app.py improves caching

## Multi-stage Dockerfile
- Base: python:3.11-slim
- Image size: ~50MB
- Build time: ~15s (first build ~30s)
- Cache behavior: pip install cached in builder stage, runtime image minimal
- Observations: multi-stage build reduces image size dramatically, maintains caching and fast rebuilds

### Key takeaways
- Docker layer caching es clave para builds rápidos
- Separar build vs runtime reduce tamaño y superficie de ataque
- --no-cache-dir evita almacenar pip cache inútil en la imagen final
