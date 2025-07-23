# Snake Game - Azure DevOps Deployment

Este repositorio contiene el código fuente y la configuración de CI/CD para desplegar una aplicación Snake Game en Azure usando Azure DevOps, Docker y Azure App Service.

## Sobre el juego

Snake Game es una aplicación web desarrollada con Django que permite a los usuarios jugar el clásico juego de la serpiente. La aplicación incluye:
- Juego interactivo de Snake con JavaScript
- Sistema de puntuaciones altas
- Interfaz de administración Django para gestionar puntajes

## Estructura del repositorio

- `docker/dockerfile`: Dockerfile para construir la imagen de la aplicación.
- `azure-pipelines.yml`: Pipeline de Azure DevOps para construir, publicar y desplegar la aplicación.
- `src/`: Código fuente de la aplicación (ajusta según tu estructura real).

## Despliegue automático

Cada vez que haces un push a la rama `main`, el pipeline se ejecuta automáticamente:
1. Construye la imagen Docker.
2. Publica la imagen en Azure Container Registry (ACR).
3. Despliega la imagen en Azure App Service.

## ¿Cómo actualizar el README?

1. Modifica este archivo (`README.md`) con la información que desees.
2. Haz commit y push a la rama `main`:
   ```sh
   git add README.md
   git commit -m "Actualiza el README"
   git push origin main
   ```
3. El pipeline se ejecutará automáticamente tras el push.
---