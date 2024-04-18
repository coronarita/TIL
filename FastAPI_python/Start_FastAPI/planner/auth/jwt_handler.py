from http.client import HTTPSConnection
import time
from datetime import datetime

from fastapi import HTTPException, status
from jose import jwt, JWTError
from database.connection import Settings

# SECRET_KEY 변수를 추출할 수 있도록 Settings 클래스 인스턴스 생성, 토큰 생성용 함수 정의
settings = Settings()

def create_access_token(user: str):
    if settings.SECRET_KEY is None : 
        raise ValueError("SECRET_KEY must bet set!")
    
    payload = {
        "user": user, 
        "expires": time.time() + 3600
    }
    
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token

# 토큰 생성 함수는 문자열 하나를 받아서 payload 딕셔너리에 전달.
# payload 딕셔너리는 사용자명과 만료시간을 포함하며 JWT가 디코딩 될 때 반환
# expires값(만료 시간)은 생성 시점에서 한 시간 후로 설정

def verify_access_token(token: str):
    if settings.SECRET_KEY is None : 
        raise ValueError("SECRET_KEY must bet set!")
    
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        expire = data.get("expires")
        
        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied"
            )
        # if datetime.utcnow() > datetime.utcfromtimestamp(expire): # deprecated
        if datetime.now() > datetime.fromtimestamp(expire): 
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token expired!"
            )
        return data
    
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token"
        )