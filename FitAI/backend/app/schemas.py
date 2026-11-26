from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field


class TryOnCreate(BaseModel):
    garment_type: Literal["top", "bottom", "dress"] = Field(
        ..., description="Kıyafet türü: top (üst), bottom (alt), dress (elbise)"
    )
    height_cm: float = Field(..., gt=50, lt=260, description="Kullanıcı boyu (cm)")
    weight_kg: float = Field(..., gt=20, lt=300, description="Kullanıcı kilosu (kg)")
    body_size: Optional[str] = Field(None, description="Beden ölçüsü (S, M, L, XL vb.)")
    person_image_path: str = Field(..., description="Kullanıcı tam beden fotoğrafı yolu")
    garment_image_path: str = Field(..., description="Hedef kıyafet görseli yolu")


class TryOnResponse(BaseModel):
    id: int
    garment_type: str
    height_cm: float
    weight_kg: float
    body_size: Optional[str]
    person_image_path: str
    garment_image_path: str
    result_image_path: Optional[str]
    status: str
    processing_time_ms: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True