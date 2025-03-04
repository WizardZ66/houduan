import json
from pathlib import Path
from typing import List
from pydantic import parse_file_as
from moudle import UserInDB
class DB:
    def __init__(self):
        self.__data_path = Path(r"C:\Users\13\Desktop\学生管理系统\sms\data.json")
        if not self.__data_path.exists():
            self.__data:List[UserInDB] = []
        else:
            self.__data:List[UserInDB] = parse_file_as(List[UserInDB],self.__data_path)
    def all(self):
        return self.__data
    def get_or_none(self,name):
        for user in self.__data:
            if user.username == name:
                return user
        return None
    def save(self,user):
        self.__data.append(user)
        if self.get_or_none(name=user.username) is not None:
            raise ValueError(f"当前用户名{user.username}重复")
        data = [x.dict() for x in self.__data]
        self.__data_path.write_text(json.dumps(data,indent=4),encoding="utf8")

db = DB()
if __name__ == '__main__':
    db.all()
    print(db.get_or_none("lily"))
    user = UserInDB(username="lily", password="1")
    db.save(user)
    print(db.get_or_none("lily"))