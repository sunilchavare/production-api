from passlib.context import CryptContext
from jose import jwt 
from datetime import datetime,timedelta
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash_password(password:str)->str:
    return pwd_context.hash(password)
    
def verify_password(plain: str,hashed:str)->bool:
    return pwd_context.verify(plain,hashed)

def create_access_token(data: dict):
    exp_time=datetime.utcnow()+ timedelta(minutes=30)
    data["exp"]=exp_time
    token=jwt.encode(data,settings.SECRET_KEY,settings.ALGORITHM)
    return token
    
