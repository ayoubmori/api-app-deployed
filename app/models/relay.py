from pydantic import BaseModel
from typing import Dict

class Relay(BaseModel):
    id: str
    state: str = "OFF"
    
class AllRelaysResponse(BaseModel):
    relays: Dict[str, Relay]
 

relays = {
    'relay1': Relay(id="relay1"),
    'relay2': Relay(id="relay2"),
    'relay3': Relay(id="relay3")
}