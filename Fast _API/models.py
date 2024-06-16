import sys
sys.path.append('../')
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base

class CleanedData(Base):
    __tablename__ = "cleaned_data"
    
    channel_id = Column(Integer, primary_key=True, index=True)
    msg_id = Column(Integer, primary_key=True, index=True)
    channel_name = Column(String, index=True)
    message = Column(String)
    cleaned_message = Column(String)
    date = Column(DateTime)
    msg_link = Column(String)
    views = Column(Integer)
    number_replies = Column(Integer)
    number_forwards = Column(Integer)
    is_forward = Column(Boolean)
    is_reply = Column(Boolean)
    contains_media = Column(Boolean)
    media_type = Column(String)
    has_url = Column(Boolean)
