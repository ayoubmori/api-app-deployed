from pydantic import BaseModel


class Relay(BaseModel):
    id: str
    state: str = "OFF"

relays = {
    'relay1': Relay(id="relay1"),
    'relay2': Relay(id="relay2"),
    'relay3': Relay(id="relay3")
}