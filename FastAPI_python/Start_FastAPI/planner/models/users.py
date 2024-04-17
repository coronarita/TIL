from typing import Optional, List
from pydantic import BaseModel, EmailStr
from beanie import Document, Link
from models.events import Event

class User(Document):
    email: EmailStr                     # email : 사용자 이메일
    password: str                       # password : 사용자 패스워드
    events: Optional[List[Event]]
    # = None : 에러 날 경우에 이거 위에다 넣어주기
    # events : 해당 사용자가 생성한 이벤트, 처음에는 비어있다.
    
    class Settings:
        name = "users"
    
    # deprecated
    class Config:
        schema_extra = {
            "example":
                {
                 "email": "fastapi@packt.com",
                 "password": "strong!!!",
                 "events": [],
                }
        }
    
    # model_config = {
    #     "json_schema_extra": {
    #         "example":
    #             {
    #              "email": "fastapi@packt.com",
    #              "password": "strong!!!",
    #              "events": [],
    #             }
    #     }
    # }
    
    
class UserSignIn(BaseModel):
    email: EmailStr
    password: str