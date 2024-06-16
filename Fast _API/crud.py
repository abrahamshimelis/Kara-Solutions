import sys
sys.path.append('../')
from sqlalchemy.orm import Session
import models
import schemas

def get_cleaned_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.CleanedData).offset(skip).limit(limit).all()

def create_cleaned_data(db: Session, data: schemas.CleanedDataCreate):
    db_data = models.CleanedData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_cleaned_data_by_id(db: Session, channel_id: int, msg_id: int):
    return db.query(models.CleanedData).filter(models.CleanedData.channel_id == channel_id, models.CleanedData.msg_id == msg_id).first()

def update_cleaned_data(db: Session, channel_id: int, msg_id: int, data: schemas.CleanedDataCreate):
    db_data = db.query(models.CleanedData).filter(models.CleanedData.channel_id == channel_id, models.CleanedData.msg_id == msg_id).first()
    if db_data:
        for key, value in data.dict().items():
            setattr(db_data, key, value)
        db.commit()
        db.refresh(db_data)
    return db_data

def delete_cleaned_data(db: Session, channel_id: int, msg_id: int):
    db_data = db.query(models.CleanedData).filter(models.CleanedData.channel_id == channel_id, models.CleanedData.msg_id == msg_id).first()
    if db_data:
        db.delete(db_data)
        db.commit()
    return db_data