# FitAI Backend API Dokümantasyonu (4. Hafta)

## Çalıştırma ve Swagger UI
Sanal ortam (`.venv`) aktifken `FitAI` klasöründe:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000