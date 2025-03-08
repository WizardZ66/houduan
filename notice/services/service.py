
import os
import secrets
from http.client import responses

from fastapi import UploadFile
from notice.config import UPLOAD_DIR, SessionLocal


def create_filename(file: UploadFile,title):
    # 确保目录存在
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_extension = file.filename.split(".")[-1]
    #生成文件名
    unique_filename = f"{title}.{secrets.token_hex(8)}.{file_extension}"
    return unique_filename

#获取文件路径,保存文件
def save_uploaded_file(filename: str,file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR,filename)
    # 保存文件
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path

#删除对应文件
def delete_associated_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"文件已删除: {file_path}")
    else:
        print(f"文件不存在，请检查文件路径: {file_path}")


#构建会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#验证文件类型
# 在 utils/file_utils.py 中增加文件类型验证
def validate_file_type(file: UploadFile, allowed_types: list) -> bool:
    """
    验证文件类型是否在允许的类型列表中
    :param file: 上传的文件对象
    :param allowed_types: 允许的文件类型列表，例如 ['text/plain']
    :return: 如果文件类型有效则返回 True，否则返回 False
    """
    if file.content_type not in allowed_types:
        return False
    return True