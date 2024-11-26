from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database
from fastapi.responses import JSONResponse

app = FastAPI()

# Crear base de datos
models.Base.metadata.create_all(bind=database.engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.UserCreate)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return {"message": "User created successfully", "user_id": db_user.id}

@app.get("/balance/{user_id}")
def get_balance(user_id: int, db: Session = Depends(get_db)):
    balance = crud.get_balance(db, user_id)
    return {"balance": balance}

@app.post("/transaction")
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, transaction.user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_transaction = crud.create_transaction(db, transaction)
    return JSONResponse(content={"message": "Transaction successful", "balance": crud.get_balance(db, transaction.user_id)})

@app.get("/transactions/{user_id}")
def get_transactions(user_id: int, db: Session = Depends(get_db)):
    transactions = crud.get_transactions(db, user_id)
    return transactions
