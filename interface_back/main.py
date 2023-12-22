import uvicorn
from fastapi import FastAPI

from src.route.auth_route import auth_route
from src.route.chat_route import chat_route
from src.route.file_route import file_route
from src.route.user_route import user_route
from src.route.contact_route import contact_route
from src.route.channel_route import channel_route
from src.route.message_route import message_route
from src.route.attachment_route import attachment_route


app = FastAPI()

app.include_router(auth_route)
app.include_router(user_route)
app.include_router(chat_route)
app.include_router(channel_route)
app.include_router(contact_route)
app.include_router(message_route)
app.include_router(attachment_route)
app.include_router(file_route)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8007)
