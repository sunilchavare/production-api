from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal, Base
from db.models import User
from schemas.user import UserCreate, UserResponse
from fastapi import HTTPException
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

app = FastAPI()


# Create tables automatically
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(email=user.email)
    db.add(new_user)

    try:
        db.commit()
        db.refresh(new_user)
        return new_user

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

@app.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()