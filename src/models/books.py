from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Integer, String, VARCHAR
from sqlmodel import Field, SQLModel, Relationship      


class Book(SQLModel, table=True):
    __tablename__ = "books"
    
    id: Optional[int] = Field(primary_key=True)
    name:str = Field(sa_value=Column(VARCHAR(100), nullable=False))
    description: str = Field(sa_value=Column(VARCHAR(500), nullable=True))
    link: str = Field(sa_value=Column(VARCHAR(500), nullable=True))
    created_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), nullable=False))
    
    