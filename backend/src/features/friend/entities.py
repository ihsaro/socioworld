from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Boolean
)

from configurations.database import Base
from configurations.entities import ApplicationBaseEntity


class Friendship(ApplicationBaseEntity, Base):
    __tablename__ = "friendship"

    client_id = Column(Integer, ForeignKey("client.id"))
    friend_id = Column(Integer, ForeignKey("client.id"))
    requested = Column(Boolean, default=False)
    approved = Column(Boolean, default=False)
