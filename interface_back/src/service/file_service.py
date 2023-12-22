# import asyncio
# import logging
# import discord
# import os
#
# from config import discord_token, load_path
# from posts.discord_client import DiscordStorageClient
from src.service.model.attachment.attachment import Attachment
from src.service.model.file.media import Media
from src.service.model.file.video import Video
from src.service.model.file.picture import Picture
from src.service.model.file.file_new import NewFile
from src.service.model.message.message import Message
from src.sql import crud_file, crud_message, crud_attachment


#
#
# class FileService(object):
#     __instance = None
#
#     def __init__(self):
#         # Паттерн синглтон
#         if not FileService.__instance:
#             self.client: DiscordStorageClient = None
#             self.channel_id = 1159472284168359939
#         else:
#             logging.info("Connected")  # не работает, необходим нужный уровень
#
#     @classmethod
#     def get_instance(cls):
#         if not cls.__instance:
#             cls.__instance = FileService()
#         return cls.__instance
#
#     async def __init_discord_client(self, ):
#
#         intents = discord.Intents.default()
#         client = DiscordStorageClient(intents=intents)
#         asyncio.create_task(client.start(discord_token))
#         self.client = client
#         await asyncio.sleep(2)
#
#     async def upload_file(self, file):
#         if self.client is None:
#             await self.__init_discord_client()
#         await self.client.wait_until_ready()
#         with open(f"{load_path}{file[0].filename}", "wb") as f:
#             f.write(file[0].file.read())
#             url = await self.client.upload(path=f"{load_path}{file[0].filename}", channel_id=self.channel_id)
#             f.close()
#             os.remove(f.name)
#         model_file = NewFile(name=file[0].filename, url=url)
#         callable(getattr(crud_file, f'insert_{str(file[0].headers["content-type"])[:5]}'))
#         call_func = getattr(crud_file, f'insert_{str(file[0].headers["content-type"])[:5]}')
#         return call_func(model_file)
#

def insert_media(file: NewFile):
    if file.type == "picture":
        return crud_file.insert_picture(file=file)
    else:
        return crud_file.insert_video(file=file)


def get_all_media():
    pictures = crud_file.get_all_picture()
    videos = crud_file.get_all_video()
    for picture, video in zip(pictures, videos):
        picture = Picture.model_validate(picture)
        video = Video.model_validate(video)
    media = Media(picture=pictures, video=videos)
    return media


def get_all_media_user(user_id: int):
    messages = crud_message.get_all_message_user(user_id=user_id)
    attachments_id = []
    for message in messages:
        message = Message.model_validate(message)
        attachments_id.append(int(message.attachment_id))
    attachments = []
    for attachment_id in attachments_id:
        attachments.append(
            Attachment.model_validate(
                crud_attachment.get_attachment_by_id(
                    attachment_id=attachment_id)
            )
        )

    pictures = []
    videos = []
    for item in attachments:
        if item.picture_id:
            pictures.append(get_picture_by_id(item.picture_id))
        if item.video_id:
            videos.append(get_video_by_id(item.video_id))

    media = Media(picture=pictures, video=videos)
    return media


def get_all_picture():
    pictures = crud_file.get_all_picture()
    for picture in pictures:
        picture = Picture.model_validate(picture)
    return pictures


def get_all_picture_by_user_id(user_id: int):
    messages = crud_message.get_all_message_user(user_id=user_id)
    attachments_id = []

    for message in messages:
        message = Message.model_validate(message)
        attachments_id.append(int(message.attachment_id))
    attachments = []
    for attachment_id in attachments_id:
        attachments.append(
            Attachment.model_validate(
                crud_attachment.get_attachment_by_id(
                    attachment_id=attachment_id)
            )
        )

    pictures = []

    for item in attachments:
        if item.picture_id:
            pictures.append(get_picture_by_id(item.picture_id))
    return pictures


def get_picture_by_id(picture_id: int):
    picture = crud_file.get_picture_by_id(picture_id=picture_id)
    return Picture.model_validate(picture)


def get_all_video():
    videos = crud_file.get_all_video()
    for video in videos:
        video = Video.model_validate(video)
    return videos


def get_all_video_by_user_id(user_id: int):
    messages = crud_message.get_all_message_user(user_id=user_id)
    attachments_id = []

    for message in messages:
        message = Message.model_validate(message)
        attachments_id.append(int(message.attachment_id))
    attachments = []
    for attachment_id in attachments_id:
        attachments.append(
            Attachment.model_validate(
                crud_attachment.get_attachment_by_id(
                    attachment_id=attachment_id)
            )
        )

    videos = []

    for item in attachments:
        if item.video_id:
            videos.append(get_video_by_id(item.video_id))
    return videos


def get_video_by_id(video_id: int):
    video = crud_file.get_video_by_id(video_id=video_id)
    return Video.model_validate(video)


def update_picture(picture: Picture):
    return crud_file.update_picture(picture=picture)


def update_video(video: Video):
    return crud_file.update_video(video=video)


def delete_picture(picture_id: int):
    return crud_file.delete_picture(picture_id=picture_id)


def delete_video(video_id: int):
    return crud_file.delete_video(video_id=video_id)
