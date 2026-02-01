# Resilient Container System

Proyecto educativo para aprender Docker, optimización de imágenes y CI/CD a nivel profesional.

---

## 🚀 Evolución del proyecto

1. **Naive Dockerfile**  
   - Imagen grande (~1.2GB)  
   - Cada cambio en app.py reconstruía dependencias  
   - Sin caching optimizado  

2. **Optimized Dockerfile**  
   - Base `python:3.11-slim`  
   - Capa de dependencias separada  
   - Build más rápido, caching de dependencias intacto  

3. **Multi-stage Dockerfile**  
   - Imagen final ligera (~50MB)  
   - Separación clara: builder vs runtime  
   - Build rápido, runtime limpio  

4. **CI/CD con GitHub Actions**  
   - Cada push construye la imagen automáticamente  
   - Levanta contenedor y corre smoke test  
   - Build fail si algo no funciona  

---

## 🧪 Cómo usarlo

```bash
# Build manual
docker build -t resilient-api ./api

# Run
docker run -p 5000:5000 resilient-api
curl http://localhost:5000
