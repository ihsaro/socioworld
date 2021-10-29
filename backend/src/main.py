from fastapi import FastAPI

from features.authentication import routes as authentication_routes

app = FastAPI()


app.include_router(authentication_routes.router)
