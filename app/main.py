from fastapi import FastAPI
from sqladmin import Admin

from app.admin import view
from app.admin.auth import authentication_backend

from app.database import engine

from app.users.router import router_user
from app.points.router import router_point
from app.profiles.router import router_profiles
from app.calc.router import router_calc
from app.parts.router import router_parts
from app.cafe.router import router_cafe
from app.trophys.router import router_trophy

app = FastAPI(
    title="API_FH",
    version="0.1.0",
)

app.include_router(router_user)
app.include_router(router_point)
app.include_router(router_profiles)
app.include_router(router_parts)
app.include_router(router_calc)
app.include_router(router_cafe)
app.include_router(router_trophy)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(view.UsersAdmin)
admin.add_view(view.UnverifiedUsersAdmin)
admin.add_view(view.ProfilesAdmin)
admin.add_view(view.PointsAdmin)
admin.add_view(view.RolesAdmin)
admin.add_view(view.PermissionsAdmin)
