from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String
)

from configurations.database import Base
from configurations.entities import ApplicationBaseEntity


class Feed(ApplicationBaseEntity, Base):
    __tablename__ = "feed"

    title = Column(String)
    description = Column(String)
    published = Column(Boolean, default=True)
    application_user_id = Column(Integer, ForeignKey("application_user.id"))