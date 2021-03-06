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

    title = Column(String, nullable=False, default="")
    description = Column(String, nullable=False, default="")
    published = Column(Boolean, nullable=False, default=True)
    client_id = Column(Integer, ForeignKey("client.id"))
