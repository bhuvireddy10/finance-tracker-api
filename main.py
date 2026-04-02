from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Finance Tracker API"}

@app.post("/transactions", response_model=schemas.TransactionResponse)
def create(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, transaction)

@app.get("/transactions")
def get_all(db: Session = Depends(get_db)):
    return crud.get_transactions(db)

@app.delete("/transactions/{transaction_id}")
def delete(transaction_id: int, db: Session = Depends(get_db)):
    result = crud.delete_transaction(db, transaction_id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "Deleted"}

@app.get("/summary")
def summary(db: Session = Depends(get_db)):
    return crud.get_summary(db)