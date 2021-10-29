from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from configurations.database import Base


class ApplicationUser(Base):
    __tablename__ = "application_user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    is_active = Column(Boolean)
    email = Column(String, index=True, unique=True)
    username = Column(String, index=True, unique=True)
    password = Column(String)