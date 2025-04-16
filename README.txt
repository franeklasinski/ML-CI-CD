# Uruchamianie aplikacji

## Lokalnie (bez Dockera)
1. Zainstaluj wymagane zależności:
   ```sh
   pip install -r requirements.txt
   ```
2. Uruchom serwer FastAPI:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
3. API będzie dostępne pod adresem: http://localhost:8000

## Za pomocą Dockera
1. Zbuduj obraz:
   ```sh
   docker build -t fastapi-ml .
   ```
2. Uruchom kontener:
   ```sh
   docker run -p 8000:8000 fastapi-ml
   ```

## Za pomocą Docker Compose
1. Uruchom aplikację i bazę Redis:
   ```sh
   docker-compose up --build
   ```
