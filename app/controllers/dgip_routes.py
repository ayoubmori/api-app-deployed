from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.models.DGIP import DigitalInputs
from app.constants.http_responces import *

degitalinput = APIRouter(tags=["Digital Input"])


class DigitalInputState(BaseModel):
    state: str  # Assuming state can be either "ON" or "OFF"


@degitalinput.get(
    "/digital-inputs",
    responses={
        200: {"model": ExampleResponseOK, "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    },
)
async def get_all_digital_input():
    """Get all digital_input status"""
    return {id: dgin for id, dgin in DigitalInputs.items()}
