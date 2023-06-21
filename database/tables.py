from sqlalchemy import create_engine, Column, String, Table, Integer, DateTime, Boolean, Text, ForeignKey, func
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from decouple import config

USERNAME_DATABASE = config("USERNAME_DATABASE")
PASSWORD_DATABASE = config("PASSWORD_DATABASE")
ADDRESS_DATABASE = config("ADDRESS_DATABASE")
DATABASE_NAME = config("DATABASE_NAME")

url = f"mysql://{USERNAME_DATABASE}:{PASSWORD_DATABASE}@{ADDRESS_DATABASE}/{DATABASE_NAME}"

async def async_main():
    engine = create_async_engine(
        url,
        echo=True
    )
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    await insert_objects(async_session)
    await select_and_update_objects
engine = create_engine(url)
class Base(AsyncAttrs, DeclarativeBase):
    pass
# Base = declarative_base(bind=engine)
# Session = sessionmaker(bind=engine)()

class AdminList(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    chat_id = Column(String(16), unique=True, nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True, unique=True, nullable=False, autoincrement=True)
    chat_id = Column(String(16), unique=True, nullable=False)
    first_name = Column(String(60))
    last_name = Column(String(60))
    username = Column(String(75))
    is_blocked = Column(Boolean, default=False)
    messages = relationship("Message", backref="message")
    created = Column(DateTime(timezone=True), default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())

class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key = True, unique=True, nullable=False, autoincrement=True)
    user = Column(Integer, ForeignKey("user.id"))
    user_chat_id = Column(String(16),nullable=False)
    text = Column(Text())
    created = Column(DateTime(timezone=True), default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())

class Music(Base):
    __tablename__ = "music"
    id = Column(Integer, primary_key = True, unique=True, nullable=False, autoincrement=True)
    message_id = Column(Integer, unique=True)
    created = Column(DateTime(timezone=True), default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())

class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key = True, unique=True, nullable=False, autoincrement=True)
    message_id = Column(Integer, unique=True)
    created = Column(DateTime(timezone=True), default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key = True, unique=True, nullable=False, autoincrement=True)
    message_id = Column(Integer, unique=True)
    created = Column(DateTime(timezone=True), default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())

Base.metadata.create_all(bind=engine)