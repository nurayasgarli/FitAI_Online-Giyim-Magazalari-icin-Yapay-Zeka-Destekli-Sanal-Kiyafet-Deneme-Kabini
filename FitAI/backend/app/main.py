from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from .auth import verify_api_key
from .database import Base, engine, get_db
from .models import TryOnRequest
from .schemas import TryOnCreate, TryOnResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FitAI Backend API",
    description="Sanal Kıyafet Deneme Kabini (Virtual Try-On) 4. Hafta Backend İskeleti",
    version="0.1.0",
)


@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok", "service": "FitAI Backend"}


@app.post(
    "/api/v1/tryon",
    response_model=TryOnResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Virtual Try-On"],
)
def create_tryon_request(
    payload: TryOnCreate,
    db: Session = Depends(get_db),
    api_key: str = Depends(verify_api_key),
):
    new_req = TryOnRequest(
        garment_type=payload.garment_type,
        height_cm=payload.height_cm,
        weight_kg=payload.weight_kg,
        body_size=payload.body_size,
        person_image_path=payload.person_image_path,
        garment_image_path=payload.garment_image_path,
        status="pending",
    )
    db.add(new_req)
    db.commit()
    db.refresh(new_req)
    return new_req


@app.get(
    "/api/v1/tryon",
    response_model=List[TryOnResponse],
    tags=["Virtual Try-On"],
)
def list_tryon_requests(
    db: Session = Depends(get_db),
    api_key: str = Depends(verify_api_key),
):
    return db.query(TryOnRequest).order_by(TryOnRequest.id.desc()).all()


@app.get(
    "/api/v1/tryon/{request_id}",
    response_model=TryOnResponse,
    tags=["Virtual Try-On"],
)
def get_tryon_request(
    request_id: int,
    db: Session = Depends(get_db),
    api_key: str = Depends(verify_api_key),
):
    item = db.query(TryOnRequest).filter(TryOnRequest.id == request_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Try-on kaydı bulunamadı.")
    return item