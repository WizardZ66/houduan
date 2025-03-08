from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from manage.database import get_db
from manage.dependencies import get_current_user
from manage.models import Teacher, TeacherAccount
from manage.schemas import TeacherCreate
from manage.schemas.teacher import TeacherBase, TeacherUpdate

router = APIRouter()

#增添新的老师
@router.post("/create_teachers/", response_model=TeacherBase)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    # 创建一个新的 Teacher 记录
    if teacher.username != current_user:
        raise HTTPException(status_code=404, detai="用户名不一致请重新输入")
    db_teacher = Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher


#更新教师信息
@router.put("/new_teachers/{teacher_id}", response_model=TeacherBase)
def update_teacher(teacher_id: int, teacher: TeacherUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="未找到该老师")
    # 更新教师信息
    for key, value in teacher.dict().items():
        if value is not None:
            setattr(db_teacher, key, value)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher


#删除教师信息
@router.delete("/delete_teachers/{teacher_id}", response_model=TeacherBase)
def delete_teacher(teacher_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="未找到该老师")
    db.delete(db_teacher)
    db.commit()
    return db_teacher

#查找教师信息
@router.get("/get_teachers_info/", response_model=TeacherBase)
def read_teacher(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    # 通过 current_user 的 username 查找 Teacher
    db_teacher = db.query(Teacher).filter(Teacher.username == current_user).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="未找到与当前用户关联的教师账户")
    return db_teacher