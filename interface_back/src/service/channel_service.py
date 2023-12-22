from src.service.model.channel.channel import Channel
from src.service.model.channel.channel_new import NewChannel
from src.sql import crud_channel_member, crud_channel, crud_user


# нвоый канал
def create_channel(channel: NewChannel):
    return crud_channel.insert_channel(channel)


# все каналы
def get_all_channel():
    channel = crud_channel.get_all_channel()
    return channel


# все каналы id-пользователя
def get_all_channel_user(user_id: int, limit: int):
    channels_id = crud_channel_member.get_user_all_channel(user_id=user_id, limit=limit)
    channels = []
    for item in channels_id:
        channels.append(get_channel_by_id(item[0]))
    return channels


# канал id-пользователя
def get_channel_by_id(channels_id: int):
    channel = crud_channel.get_channel_by_id(channels_id)
    return channel


# изменение канала
def update_channel(channel: Channel):
    return crud_channel.update_channel(channel=channel)


# удаление канала
def delete_channel(channel_id: int):
    return crud_channel.delete_channel(channel_id=channel_id)