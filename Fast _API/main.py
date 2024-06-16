import sys
sys.path.append('../')
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/cleaned_data/", response_model=list[schemas.CleanedData])
def read_cleaned_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    data = crud.get_cleaned_data(db, skip=skip, limit=limit)
    return data

@app.post("/cleaned_data/", response_model=schemas.CleanedData)
def create_cleaned_data(data: schemas.CleanedDataCreate, db: Session = Depends(get_db)):
    return crud.create_cleaned_data(db, data)

@app.get("/cleaned_data/{channel_id}/{msg_id}", response_model=schemas.CleanedData)
def read_cleaned_data_by_id(channel_id: int, msg_id: int, db: Session = Depends(get_db)):
    data = crud.get_cleaned_data_by_id(db, channel_id, msg_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@app.put("/cleaned_data/{channel_id}/{msg_id}", response_model=schemas.CleanedData)
def update_cleaned_data(channel_id: int, msg_id: int, data: schemas.CleanedDataCreate, db: Session = Depends(get_db)):
    db_data = crud.update_cleaned_data(db, channel_id, msg_id, data)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data

@app.delete("/cleaned_data/{channel_id}/{msg_id}", response_model=schemas.CleanedData)
def delete_cleaned_data(channel_id: int, msg_id: int, db: Session = Depends(get_db)):
    db_data = crud.delete_cleaned_data(db, channel_id, msg_id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data