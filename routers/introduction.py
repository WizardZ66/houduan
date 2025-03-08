from fastapi import APIRouter, Depends
from ..services.database import get_db

router = APIRouter(prefix="/introduction", tags=["书院简介"])

@router.get("")
async def get_introduction(db=Depends(get_db)):
    intro = db.execute(
        'SELECT content FROM introduction ORDER BY updated_at DESC LIMIT 1'
    ).fetchone()
    return {"content": intro["content"] if intro else "暂无简介"}