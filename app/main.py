from fastapi import FastAPI

from app.users.router import router_user
from app.points.router import router_point
from app.profiles.router import router_profiles


app = FastAPI(
    title="API_FH",
    version="0.1.0",
)

app.include_router(router_user)
app.include_router(router_point)
app.include_router(router_profiles)
