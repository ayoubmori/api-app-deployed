from fastapi import FastAPI
from app.controllers.relay_routes import relay_route
from app.controllers.dgip_routes import degitalinput


app = FastAPI(title="rest api")

app.include_router(relay_route, prefix="/api")
app.include_router(degitalinput, prefix="/api")
