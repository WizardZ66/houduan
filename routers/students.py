from fastapi import APIRouter, HTTPException, Depends
from ..models import StudentBase
from ..services.database import get_db
from passlib.context import CryptContext
import sqlite3

router = APIRouter(prefix="/students", tags=["学生管理"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/{student_id}")
async def get_student(student_id: int, db=Depends(get_db)):
    student = db.execute(
        'SELECT * FROM students WHERE student_id = ?',
        (student_id,)
    ).fetchone()
    if not student:
        raise HTTPException(status_code=404, detail="学生不存在")
    return dict(student)

@router.put("/{student_id}")
async def update_student(
    student_id: int,
    student_data: StudentBase,
    db=Depends(get_db)
):
    try:
        hashed_password = None
        if student_data.password:
            hashed_password = pwd_context.hash(student_data.password)
        db.execute('''
            UPDATE students SET
                name = ?, gender = ?, student_number = ?,
                college = ?, major = ?, class = ?,
                grade = ?, campus = ?, ethnicity = ?,
                direction = ?, political_status = ?,
                email = ?, phone = ?, wechat = ?, qq = ?, password = COALESCE(?, password)
            WHERE student_id = ?
        ''', (
            student_data.name, student_data.gender, student_data.student_number,
            student_data.college, student_data.major, student_data.class_,
            student_data.grade, student_data.campus, student_data.ethnicity,
            student_data.direction, student_data.political_status,
            student_data.email, student_data.phone, student_data.wechat,
            student_data.qq, hashed_password, student_id
        ))
        db.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="学号已存在")
    return {"message": "学生信息更新成功"}