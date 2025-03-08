import mimetypes
import os
import secrets
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from manage.config import PORT, HOST
from manage.database import get_db
from manage.dependencies import get_current_user
from manage.models import TeacherAccount

router=APIRouter()

#生成文件夹
UPLOAD_DIR = "photos"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # 生成唯一的文件名
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{secrets.token_hex(8)}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # 保存文件
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    download_url=f"http://{HOST}:{PORT}/photo/download_images?filename={unique_filename}"

    return {"message": "Image uploaded successfully", "URL":download_url}


@router.get("/download_images/")
def show_images(filename:str):
    file_path = os.path.join(UPLOAD_DIR,filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="文件不存在")
    mime_type, _ = mimetypes.guess_type(file_path)

    # 创建一个StreamingResponse，以便流式传输大文件，同时设置正确的MIME类型
    response = StreamingResponse(
        open(file_path, 'rb'),
        media_type=mime_type,
    )
    # 不设置Content-Disposition，避免浏览器触发下载
    return response

