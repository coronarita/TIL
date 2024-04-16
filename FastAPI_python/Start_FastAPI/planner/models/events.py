from beanie import Document
from typing import Optional, List
from pydantic import BaseModel

class Event(Document):

    title: str          # title : 이벤트 타이틀
    image: str          # image : 이벤트 이미지 배너의 링크
    description: str    # description : 이벤트 설명
    tags: List[str]     # tags: 그룹화를 위한 이벤트 태그
    location: str       # location : 이벤트 위치
    
    model_config = {
        "json_schema_extra": {
            "example":
                {
                 "title": "FastAPI Book Launch",
                 "image": "https://linktomyimage.com/image.png",
                 "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                 "tags": ["python", "fastapi", "book", "launch"],
                 "location": "Google Meet",   
                }
        }
    }
    class Settings:
        name = "events"

    
# UPDATE 처리의 바디 유형으로 추가
class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
        
    model_config = {
        "json_schema_extra": {
            "example":
                {
                 "title": "FastAPI Book Launch",
                 "image": "https://linktomyimage.com/image.png",
                 "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                 "tags": ["python", "fastapi", "book", "launch"],
                 "location": "Google Meet",   
                }
        }
    }