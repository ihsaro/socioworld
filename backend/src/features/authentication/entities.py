import enum

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Enum,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.orm import relationship

from configurations.database import Base


class Roles(enum.Enum):
    ADMIN = "Admin",
    USER = "User"


class ApplicationUser(Base):
    __tablename__ = "application_user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    role = Column(Enum(Roles), default=Roles.USER)
    is_active = Column(Boolean)
    email = Column(String, index=True, unique=True)
    username = Column(String, index=True, unique=True)
    password = Column(String)
