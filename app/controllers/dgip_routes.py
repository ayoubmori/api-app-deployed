from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.models.DGIP import DegitalInputs, DegitalInput


degitalinput = APIRouter(tags=["Digital Input"])


class DigitalInputState(BaseModel):
    state: str  # Assuming state can be either "ON" or "OFF"


@degitalinput.get("/digital-inputs", response_description="Successful Response", response_model=DegitalInput)
async def get_all_digital_inputs(dgip_id: str):
    """Get the status of a digital input."""
    if dgip_id in DegitalInputs:
        return  DegitalInputs[dgip_id]
    else:
        raise HTTPException(
            status_code=404, detail=f"Relay with id '{dgip_id}' does not exist"
        )







