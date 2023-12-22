from datetime import timedelta
from typing import Annotated
from fastapi import Depends
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from src.service import user_service, token_service
from src.service.model.user.user_new import NewUser
from src.service.model.token.token import Token
from src.service.token_service import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token

auth_route = APIRouter(tags=["Авторизация"])


@auth_route.post("/registration")
async def new_user(client: NewUser):
    return user_service.insert_user(client)


@auth_route.post("/authorization", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = token_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "user_id": user.id,
              "password": user.hash_password, "phone": user.phone,
              "status": user.status},
        expires_delta=access_token_expires
    )
    user_service.update_user_last_online(user_id=user.id)
    return {"access_token": access_token, "token_type": "bearer"}
