import mimetypes
import os
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from fastapi.responses import StreamingResponse
from school_info.config import HOST, PORT
from school_info.models.model import newsBase
from school_info.services.service import get_db, validate_file_type, create_filename, save_uploaded_file, \
    delete_associated_file

router = APIRouter()


# 上传公告（支持文件上传）
@router.post("/upload_news/")
async def create_news(
        title: str,
        file: UploadFile = File(None),
        db: Session = Depends(get_db)
):
    # 验证文件类型是否为 TXT
    if not validate_file_type(file, ['text/plain']):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="仅支持上传 TXT 文件"
        )
    #生成保存文件路径，文件名
    unique_filename=create_filename(file, title)
    file_path=save_uploaded_file(unique_filename, file)

    #生成显示公告url
    download_url = f"http://{HOST}:{PORT}/school_info/show_news?file_path={file_path}"
    #公告信息存入数据库
    db_bulletin = newsBase(unique_filename=unique_filename, file_path=file_path,file_show_url=download_url)
    db.add(db_bulletin)
    db.commit()
    db.refresh(db_bulletin)
    return {"获取文件url":download_url,"唯一文件名":db_bulletin.unique_filename}


# 公告传输
@router.get("/show_news/")
def show_news(file_path: str):

    # 检查文件是否存在
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="文件不存在")

    # 获取文件的 MIME 类型
    mime_type, _ = mimetypes.guess_type(file_path)

    # 打开文件并创建 StreamingResponse
    file_like = open(file_path, 'rb')

    # 设置正确的 MIME 类型为 text/plain，确保浏览器以纯文本显示
    response = StreamingResponse(
        file_like,
        media_type="text/plain",
    )
    # 不设置 Content-Disposition，避免触发下载
    return response


# 删除公告（同时删除关联文件）
@router.delete("/delete_bulletin/")
def delete_bulletin(unique_filename:str,db: Session = Depends(get_db)):
    db_news = db.query(newsBase).filter(newsBase.unique_filename == unique_filename).first()
    if db_news is None:
        raise HTTPException(status_code=404, detail="公告不存在")

    # 删除关联文件
    delete_associated_file(db_news.file_path)
    #删除公告
    db.delete(db_news)
    db.commit()
    return {"message": "公告已删除"}