from mpl_toolkits.axes_grid1.parasite_axes import HostAxesBase
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./teacher_management.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#端口信息
PORT=8000
HOST="localhost"

SECRET_KEY = "ab34ef56"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30