from datetime import datetime
from typing import Optional, List

from sqlalchemy import Column, VARCHAR, DateTime
from sqlmodel import SQLModel, Field, Relationship

class Shelf(SQLModel, table=True):
    __tablename__ = "shelves"

    id: Optional[int] = Field(primary_key=True)
    name: str = Field(sa_value=Column(VARCHAR(100), nullable=False))
    description: Optional[str] = Field(sa_value=Column(VARCHAR(500), nullable=True))
    created_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), nullable=False))
    
    
    books: List["Book"] = Relationship(back_populates="shelf")  # Assuming Book model has a shelf relationship