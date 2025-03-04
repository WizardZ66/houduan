from fastapi import FastAPI,Body

from moudle import usersignup, UserInDB

from db import db

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/path/{p}",summary="路径参数-简单实用")
def get_path(p:str):
    return{"msg":p}
@app.post("/signup",summary="注册接口")
def signup(form_data:usersignup=Body(...)):
    # 拿到前端传回来的数据
    username =form_data.username
    password = form_data.password
    #检验数据
    #根据用户名去数据库查找对应的user
    user = db.get_or_none(username)
    if user is not None:
        return {"msg":"当前用户名已经被占用了"}
    #保存到数据库
    user = UserInDB(username=username, password=password)
    db.save(user)
    #给前端响应数据
    return{'msg':"ok"}
