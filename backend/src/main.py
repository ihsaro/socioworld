from fastapi import FastAPI

from features.authentication import routes as authentication_routes
from features.feed import routes as feed_routes
from features.friend import routes as friend_routes

app = FastAPI()


app.include_router(authentication_routes.router)
app.include_router(feed_routes.router)
app.include_router(friend_routes.router)
