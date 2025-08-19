from fastapi import APIRouter, Depends, HTTPException, status

from app.api.models.transfer import TransferCreate, TransferFromDB
from fake_db.transfer_db import TransferManager, get_transfer_manager
from fake_db.user_db import UsersManager, get_user_manager

transfer_router = APIRouter(
    prefix="/transfer",
    tags=["Transfer"],
)


@transfer_router.post("/",
                      response_model=TransferFromDB | dict,
                      status_code=status.HTTP_201_CREATED,
                      )
async def create_transfer(transfer_data: TransferCreate,
                          transfer_manager: TransferManager = Depends(get_transfer_manager),
                          user_manager: UsersManager = Depends(get_user_manager),
                          ):

    if transfer_data.to_user_id == transfer_data.from_user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="don't be naughty")

    sender = user_manager.find_user(int(transfer_data.from_user_id))
    if sender is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Sender doesn't exist")

    receiver = user_manager.find_user(int(transfer_data.to_user_id))
    if receiver is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Receiver doesn't exist")

    if float(transfer_data.amount) > sender.balance:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="the sender's account does not have "
                                   "sufficient funds to complete the transaction")

    new_transfer = transfer_manager.create_transfer(transfer_data)
    receiver.balance += float(transfer_data.amount)
    sender.balance -= float(transfer_data.amount)

    return new_transfer


