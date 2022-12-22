from dataclasses import dataclass
from uuid import UUID


@dataclass
class SignUpDTO:
    auth_code: UUID
    name: str
    account_id: str
    password: str
    work_place: str
    subject: str
