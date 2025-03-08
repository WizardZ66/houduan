
from pydantic import BaseModel
from datetime import datetime

class BulletinBase(BaseModel):
    title: str
    file_path: str = None

class BulletinCreate(BulletinBase):
    pass

class BulletinUpdate(BulletinBase):
    pass

class Bulletin(BulletinBase):
    id: int
    created_at: datetime

    class Config:
         from_attributes= True