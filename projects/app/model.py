from datetime import datetime
from time import time_ns
from typing import Optional
from uuid import UUID, uuid4

from app.enums import Language


class User:
    def __init__(self,
                 full_name: Optional[str] = None,
                 password: Optional[str] = None,
                 phone_number: Optional[str] = None,
                 email: Optional[str] = None,
                 user_id: Optional[UUID] = None,
                 created_at: Optional[datetime] = None,
                 language: Optional[Language] = None
                 ):
        self.full_name = full_name
        self.password = password
        self.phone_number = phone_number
        self.email = email
        self.user_id = user_id
        self.created_at = created_at or str(datetime.now())
        self.language = language or Language.English.value


# user1 = User(full_name='ali', password='123')
# user2 = User(full_name='ali', password='123')
# user2 = user1
