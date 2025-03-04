from pydantic import BaseModel, validator


class UserInDB(BaseModel):
    """这个模型是orm模型"""
    username: str
    password: str
    is_superuser:bool = False
    status:bool = True

class usersignup(BaseModel):
    username:str
    password:str
    password2:str
    @validator("password2")
    def two_password_match(cls,value,values):
        if value!=values['password']:
            raise ValueError("两个密码必须一致")
        return value