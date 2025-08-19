from pydantic import BaseModel, ConfigDict


class TransferBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class TransferCreate(TransferBase):
    from_user_id: str
    to_user_id: str
    amount: str


class TransferFromDB(TransferCreate):
    id: int