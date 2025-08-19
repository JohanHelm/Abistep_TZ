from dataclasses import dataclass

from app.api.models.transfer import TransferCreate, TransferFromDB


@dataclass
class Transfer:
    id: int
    from_user_id: int
    to_user_id: int
    amount: float


class TransferManager:
    def __init__(self):
        self.ids_counter: int = 0
        self.transfers: list[Transfer] = []


    def create_transfer(self, transfer_data: TransferCreate) -> Transfer:
        self.ids_counter += 1
        new_transfer = Transfer(
            id=self.ids_counter,
            from_user_id=int(transfer_data.from_user_id),
            to_user_id=int(transfer_data.to_user_id),
            amount=float(transfer_data.amount),
        )
        self.transfers.append(new_transfer)
        return new_transfer



transfer_manager = TransferManager()

def get_transfer_manager():
    return transfer_manager