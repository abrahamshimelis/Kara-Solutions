import sys
sys.path.append('../')
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CleanedDataBase(BaseModel):
    channel_id: int
    msg_id: int
    channel_name: Optional[str]
    message: Optional[str]
    cleaned_message: Optional[str]
    date: Optional[datetime]
    msg_link: Optional[str]
    views: Optional[int]
    number_replies: Optional[int]
    number_forwards: Optional[int]
    is_forward: Optional[bool]
    is_reply: Optional[bool]
    contains_media: Optional[bool]
    media_type: Optional[str]
    has_url: Optional[bool]

    class Config:
        orm_mode = True

class CleanedDataCreate(CleanedDataBase):
    pass

class CleanedData(CleanedDataBase):
    pass
