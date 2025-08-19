from dataclasses import dataclass

from app.api.models.user import UserCreate


@dataclass
class User:
    id: int
    name: str
    email: str
    balance: int | float


class UsersManager:
    def __init__(self):
        self.ids_counter: int = 0
        self.users: list[User] = []


    def check_unique_email(self, user_data: UserCreate) -> bool:
        return not bool(*filter(lambda x: x.email == user_data.email , self.users))


    def create_new_user(self, user_data: UserCreate) -> User:
        self.ids_counter += 1
        new_user = User(
            id=self.ids_counter,
            name=user_data.name,
            email=user_data.email,
            balance=user_data.balance,
        )
        self.users.append(new_user)
        return new_user


    def find_user(self, user_id) -> User | None:
        found_user = tuple(filter(lambda x: x.id == user_id , self.users))
        if found_user:
            return found_user[0]
        else:
            return None


users_manager = UsersManager()


def get_user_manager():
    return users_manager
