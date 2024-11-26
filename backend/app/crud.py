from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(
        user_id=transaction.user_id, 
        type=transaction.type,
        amount=transaction.amount,
        date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions(db: Session, user_id: int):
    return db.query(models.Transaction).filter(models.Transaction.user_id == user_id).all()

def get_balance(db: Session, user_id: int):
    transactions = db.query(models.Transaction).filter(models.Transaction.user_id == user_id).all()
    balance = 0.0
    for t in transactions:
        if t.type == 'deposit':
            balance += t.amount
        elif t.type == 'withdraw' and balance >= t.amount:
            balance -= t.amount
    return balance
