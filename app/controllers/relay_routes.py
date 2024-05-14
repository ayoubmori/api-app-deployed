from fastapi import APIRouter, HTTPException

from app.models.relay import Relay, relays
from app.constants.http_responces import *

relay_route = APIRouter(tags=["Relay"])


@relay_route.get(
    "/relay",
    responses={
        200: {"model": ExampleResponseOK, "description": "Successful response"},
        404: {"model": ExampleResponseNotFound, "description": "Not Found"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    },
)
async def get_relay(relay_id: str):
    """Get the status of a relay"""
    if relay_id in relays:
        return relays[relay_id]
    else:
        raise HTTPException(
            status_code=404, detail=f"Relay with id '{relay_id}' does not exist"
        )


@relay_route.post(
    "/relay/{relay_id}",
    response_description="Successful Response",
    response_model=Relay,
    responses={
        200: {"model": ExampleResponseOK, "description": "Successful response"},
        400: {"model": ExampleResponseBadRequest, "description": "Bad Request"},
        404: {"model": ExampleResponseNotFound, "description": "Not Found"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    },
)
async def change_relay_state(relay_stats: Relay):
    """Change the state of a relay."""
    if relay_stats.id in relays:
        if relay_stats.state.upper() == "ON":
            relays[relay_stats.id].state = "ON"
        elif relay_stats.state.upper() == "OFF":
            relays[relay_stats.id].state = "OFF"
        else:
            raise HTTPException(
                status_code=400, detail="Invalid state. Must be either 'ON' or 'OFF'."
            )
        return relays[relay_stats.id]
    else:
        raise HTTPException(
            status_code=404, detail=f"Relay with id '{relay_stats.id}' does not exist"
        )


@relay_route.get(
    "/relays",
    responses={
        200: {"model": ExampleResponseOK, "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    },
)
async def get_all_relays():
    """Get all relays status"""
    return {id: relay for id, relay in relays.items()}
