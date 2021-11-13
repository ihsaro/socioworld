from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP
)
from sqlalchemy.sql import func


class ApplicationBaseEntity(object):
    id = Column(Integer, primary_key=True, index=True)
    created_timestamp = Column(TIMESTAMP, server_default=func.now())
    last_modified_timestamp = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
