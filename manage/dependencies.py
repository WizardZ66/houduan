from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from manage.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
#token解码依赖
async def get_current_user(token: str = Depends(oauth2_scheme)):
    #定义异常
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    #使用 jwt.decode 解码 token，验证其签名是否有效。
    # token: 当前的 Bearer Token。
    # SECRET_KEY: 用于验证签名的密钥。
    # algorithms=[ALGORITHM]: 指定使用的算法。
    # 如果解码失败（例如 token 过期或被篡改），会抛出 JWTError 异常，并触发认证失败的异常处理。
    # 从解码后的 payload 中提取用户名（sub 字段）。如果用户名为空，也触发认证失败。
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # 这里可以查询数据库验证用户是否存在
    # user = get_user(username)
    # if user is None:
    #     raise credentials_exception
    return username