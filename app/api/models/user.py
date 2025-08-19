from pydantic import BaseModel, ConfigDict, EmailStr

from settings.initial_settings import UserParams


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    name: str
    email: EmailStr
    balance: int | float = UserParams.start_balance


class UserFromDB(UserCreate):
    id: int

