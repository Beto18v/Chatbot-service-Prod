# Chatbot FAQ Service - AdoptaFácil

Servicio de chatbot inteligente para preguntas frecuentes sobre la plataforma AdoptaFácil, desarrollado con FastAPI y matching difuso (fuzzy matching) para manejar variaciones en las preguntas de los usuarios.

## 🚀 Características

- **Matching Difuso**: Utiliza algoritmos de similitud de texto para encontrar respuestas incluso con errores ortográficos o variaciones
- **Base de Conocimiento Estructurada**: Más de 45 preguntas frecuentes extraídas de la documentación de AdoptaFácil
- **API REST**: Endpoints simples para integración con la plataforma principal
- **Fácil Expansión**: Agregar nuevas preguntas y respuestas sin modificar el código core
- **Umbral Configurable**: Ajusta la sensibilidad del matching difuso según necesidades

## 📋 Requisitos del Sistema

- Python 3.8+
- pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone <repository-url>
cd chatbot-faq-service
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv venv
```

### 3. Activar entorno virtual

```bash
# Windows
.\venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Verificar instalación

```bash
python -c "import fastapi, uvicorn, rapidfuzz; print('Todas las dependencias instaladas correctamente')"
```

## 🚀 Uso

### Desarrollo (local)

Ejecuta el servidor en un puerto local (ejemplo `8001`):

```bash
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

Verificar que el servicio esté corriendo:

- Root: `http://127.0.0.1:8001/`
- Swagger: `http://127.0.0.1:8001/docs`

## 📡 API (Endpoints reales)

- `GET /` → estado del servicio
- `POST /chat/` → responder a una pregunta
- `GET /docs` → documentación Swagger UI

Ejemplo (Windows):

```bash
curl.exe -s http://127.0.0.1:8001/
curl.exe -s -X POST http://127.0.0.1:8001/chat/ -H "Content-Type: application/json" -d "{\"message\":\"hola\"}"
```

## 🐳 Docker

### Build local

```bash
docker build -t adopta-chatbot:local .
```

### Run local

El contenedor escucha internamente en `8000`, por eso se mapea `8001:8000`:

```bash
docker run --rm --name adopta-chatbot -p 8001:8000 \
  -e CORS_ALLOW_ORIGINS="https://adoptafacil-prod-a3f3gvdnc8hhfkfj.eastus-01.azurewebsites.net" \
  adopta-chatbot:local
```

Probar:

```bash
curl.exe -s http://127.0.0.1:8001/
curl.exe -s -X POST http://127.0.0.1:8001/chat/ -H "Content-Type: application/json" -d "{\"message\":\"hola\"}"
```

### Variables de entorno

- `CORS_ALLOW_ORIGINS`
  - `*` (default) permite cualquier origen.
  - En producción se restringe al dominio del website.

## ✅ Producción (cómo quedó)

El servicio corre en Azure como **App Service (Linux) ejecutando un contenedor Docker**. La imagen se publica en **Docker Hub** y App Service la descarga para ejecutar el microservicio.

### Configuración aplicada en App Service

- `WEBSITES_PORT=8000`
- `WEBSITES_ENABLE_APP_SERVICE_STORAGE=false`
- `CORS_ALLOW_ORIGINS` con el origen del website (y opcionalmente orígenes locales cuando se prueba desde local)

### URLs reales

- Chatbot (API): https://adopta-chatbot-a3d0fremcabnf2h6.eastus-01.azurewebsites.net/
  - Swagger: https://adopta-chatbot-a3d0fremcabnf2h6.eastus-01.azurewebsites.net/docs
  - Endpoint chat: https://adopta-chatbot-a3d0fremcabnf2h6.eastus-01.azurewebsites.net/chat/
- Website: https://adoptafacil-prod-a3f3gvdnc8hhfkfj.eastus-01.azurewebsites.net/

## 🔗 Integración con AdoptaFacil-Prod (real)

- El website consume el microservicio desde el frontend (componente `ChatbotWidget`).
- Se usa la variable `VITE_CHATBOT_URL` como URL base del chatbot.
- Para que funcione en navegador, el chatbot permite el origen del website con `CORS_ALLOW_ORIGINS`.

**Última actualización**: Marzo 03 de 2026
**Versión**: 1.0.0
