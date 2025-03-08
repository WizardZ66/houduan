from fastapi import APIRouter, Depends
from ..services.database import get_db

router = APIRouter(prefix="/announcements", tags=["公告栏"])

@router.get("")
async def get_announcements(active_only: bool = True, db=Depends(get_db)):
    query = '''
        SELECT * FROM announcements 
        WHERE is_active = ? 
        ORDER BY publish_date DESC
    '''
    announcements = db.execute(query, (1 if active_only else 0,)).fetchall()
    return [dict(ann) for ann in announcements]