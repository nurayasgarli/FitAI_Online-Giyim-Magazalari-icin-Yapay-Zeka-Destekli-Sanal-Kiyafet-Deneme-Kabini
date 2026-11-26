from datetime import datetime
from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from .database import Base


class TryOnRequest(Base):
    __tablename__ = "tryon_requests"

    id = Column(Integer, primary_key=True, index=True)
    garment_type = Column(String(32), nullable=False)  # "top", "bottom", "dress"
    height_cm = Column(Float, nullable=False)
    weight_kg = Column(Float, nullable=False)
    body_size = Column(String(16), nullable=True)  # "S", "M", "L", "XL" vb.
    person_image_path = Column(String(255), nullable=False)
    garment_image_path = Column(String(255), nullable=False)
    result_image_path = Column(String(255), nullable=True)
    status = Column(String(32), default="pending", nullable=False)  # "pending", "processing", "completed", "failed"
    processing_time_ms = Column(Integer, nullable=True)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)