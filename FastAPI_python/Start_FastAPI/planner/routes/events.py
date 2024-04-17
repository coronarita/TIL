from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event, EventUpdate
from typing import List
from beanie import PydanticObjectId
from database.connection import Database

event_router = APIRouter(
    tags=["Events"]
)

event_database = Database(Event)

# 모든 이벤트 추출하는 라우트
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

# 특정 ID 이벤트 추출하는 라우트
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event

# 이벤트 생성 라우트
@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict: # ... 은 필수 입력해야 함 명시
    await event_database.save(body)
    return {
        "message": "Event created successfully."
    }
    
# 이벤트 업데이트 라우트
@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated_event
    
# 단일 이벤트 삭제 라우트
@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return {
        "message": "Event deleted successfully."
    }        

# 전체 이벤트 삭제 라우트
# @event_router.delete("/")
# async def delete_all_events() -> dict :
#     await event_database.clear()
#     return {
#         "message": "Events deleted successfully."
#     }
