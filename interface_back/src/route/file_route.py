from typing import Annotated

from fastapi import File, UploadFile, HTTPException
from fastapi import APIRouter
from jose import jwt

from config import SECRET_KEY
from src.service import file_service
from src.service.model.file.file_new import NewFile
from src.service.model.file.media import Media
from src.service.model.file.picture import Picture
from src.service.model.file.video import Video

file_route = APIRouter(tags=["Файл"])


# @file_route.post("/uploadfile/")
# async def create_upload_file(
#         files: Annotated[list[UploadFile],
#         File(description="Multiple files as UploadFile")]):
#
#     file_service = FileService.get_instance()
#
#     await file_service.upload_file(file=files)
#
#     return {"filenames": [file for file in files]}
#     return


# всё медиа
@file_route.get("/media", response_model=Media)
async def media():
    return file_service.get_all_media()


# всё медиа id-пользователя
@file_route.get("/media/me", response_model=Media)
async def media(token: str):
    user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if user.get('user_id') is None:
        raise HTTPException(status_code=401, detail="Неверные логин и пароль")
    return file_service.get_all_media_user(user.get('user_id'))


# всё медиа id-пользователя
@file_route.get("/media/{user_id}", response_model=Media)
async def media(user_id: int):
    return file_service.get_all_media_user(user_id=user_id)


# новое медиа
@file_route.post("/media/new_media")
async def media(file: NewFile):
    return file_service.insert_media(file=file)


# все фотографии
@file_route.get("/pictures", response_model=list[Picture])
async def _picture():
    return file_service.get_all_picture()


# фотографии id-пользователя
@file_route.get("/pictures/me", response_model=list[Picture])
async def picture_me(token: str):
    user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if user.get('user_id') is None:
        raise HTTPException(status_code=401, detail="Неверные логин и пароль")
    return file_service.get_all_picture_by_user_id(user.get('user_id'))


# id-фотография
@file_route.get("/pictures/{picture_id}", response_model=Picture)
async def _picture_id(picture_id: int):
    return file_service.get_picture_by_id(picture_id=picture_id)


# все видео
@file_route.get("/videos", response_model=list[Video])
async def _video():
    return file_service.get_all_video()


# видео id-пользователя
@file_route.get("/videos/me", response_model=list[Picture])
async def video_me(token: str):
    user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if user.get('user_id') is None:
        raise HTTPException(status_code=401, detail="Неверные логин и пароль")
    return file_service.get_all_video_by_user_id(user.get('user_id'))


# id-фотография
@file_route.get("/videos/{video_id}", response_model=Video)
async def _video_id(video_id: int):
    return file_service.get_video_by_id(video_id=video_id)


# обновление изображения
@file_route.put("/pictures/{picture_id}/change")
async def update_media(picture_id: int, picture: Picture):
    return file_service.update_picture(picture=picture)


# обновление видео
@file_route.put("/videos/{video_id}/change")
async def update_media(video_id: int, video: Video):
    return file_service.update_video(video=video)


# удаление изображения
@file_route.delete("/pictures/{picture_id}/delete")
async def update_media(picture_id: int):
    return file_service.delete_picture(picture_id=picture_id)


# удаление видео
@file_route.delete("/videos/{video_id}/delete")
async def update_media(video_id: int):
    return file_service.delete_video(video_id=video_id)
