from fastapi import APIRouter, Depends, HTTPException, status

from app.api.models.user import UserCreate, UserFromDB
from fake_db.user_db import UsersManager, get_user_manager

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@user_router.post("/", response_model=UserFromDB | dict, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate,
                      user_manager: UsersManager = Depends(get_user_manager),
                      ):

    if user_manager.check_unique_email(user_data):
        new_user = user_manager.create_new_user(user_data)
        return new_user
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Users email {user_data.email} is not unique")


@user_router.get("/", response_model=list[UserFromDB])
async def get_users(user_manager: UsersManager = Depends(get_user_manager),
                    ):
    return user_manager.users
