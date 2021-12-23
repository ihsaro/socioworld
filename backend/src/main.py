import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from features.authentication import routes as authentication_routes
from features.feed import routes as feed_routes
from features.friend import routes as friend_routes

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication_routes.router)
app.include_router(feed_routes.router)
app.include_router(friend_routes.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
