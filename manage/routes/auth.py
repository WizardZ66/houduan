from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from manage.config import ACCESS_TOKEN_EXPIRE_MINUTES
from manage.database import get_db
from manage.models import TeacherAccount
from manage.schemas import TeacherAccountCreate
from manage.services import get_password_hash, verify_password, create_access_token

router = APIRouter()

@router.post("/register")
def register_teacher_account(account: TeacherAccountCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(account.password)
    db_account = TeacherAccount(username=account.username, password=hashed_password)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return {"message": "Account created successfully"}

@router.post("/login")
def login_teacher_account(account: TeacherAccountCreate, db: Session = Depends(get_db)):
    db_account = db.query(TeacherAccount).filter(TeacherAccount.username == account.username).first()
    if not verify_password(account.password, db_account.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    elif not db_account:
        raise HTTPException(status_code=400, detail="user not found")
    #生成期望的令牌过期时间
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # 生成token令牌
    access_token = create_access_token(
        data={"sub": db_account.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}