from auth.hash_password import HashPassword

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm # 인증 정보 추출을 위해 로그인 라우트에 주입
from auth.jwt_handler import create_access_token

from models.users import User, TokenResponse
from database.connection import Database

user_router = APIRouter(
    tags=["User"],
)
user_database = Database(User)
hash_password = HashPassword()

@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already"
        )
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    await user_database.save(user)
    return {
        "message": "User created successfully."
    }
    
@user_router.post("/signin", response_model=TokenResponse) # 응답 모델 지정
# OAuth2PasswordRequestForm을 주입하여 함수가 OAuth2사양을 업격하게 따르도록 한다.
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()) -> dict: 
    user_exist = await User.find_one(User.email == user.username)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist"
        )    
    # if user_exist.password == user.password:
    #     return {
    #     "message": "User signed in successfully."
    #     }
    
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed"
    )
    
    
