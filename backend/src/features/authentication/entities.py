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

from configurations.database import Base
from configurations.entities import ApplicationBaseEntity


class Roles(enum.Enum):
    ADMIN = "Admin",
    CLIENT = "Client"


class ApplicationUser(ApplicationBaseEntity, Base):
    __tablename__ = "application_user"

    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    role = Column(Enum(Roles), default=Roles.CLIENT)
    is_active = Column(Boolean)
    email = Column(String, index=True, unique=True)
    username = Column(String, index=True, unique=True)
    password = Column(String)


class Client(ApplicationBaseEntity, Base):
    __tablename__ = "client"

    application_user_id = Column(Integer, ForeignKey("application_user.id"))


class Admin(ApplicationBaseEntity, Base):
    __tablename__ = "admin"

    application_user_id = Column(Integer, ForeignKey("application_user.id"))


class BlacklistedToken(ApplicationBaseEntity, Base):
    __tablename__ = "blacklisted_token"

    token = Column(String)
