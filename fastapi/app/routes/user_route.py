from fastapi import APIRouter, Body

from database import UserModel
from models.User import User

user_route = APIRouter()


@user_route.post("/users/")
def create_users(user: User = Body(...)):
    UserModel.create(username=user.username, password=user.password, email=user.email)


@user_route.get("/users")
def get_users():
    user = UserModel.select().where(UserModel.id > 0).dicts()
    return list(user)


@user_route.get("/users/{user_id}")
def get_user(user_id: int):
    try:
        user = UserModel.get(UserModel.id == user_id)
        return user
    except UserModel.DoesNotExist:
        return {"error": "User not found"}
