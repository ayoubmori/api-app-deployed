from pydantic import BaseModel
from typing import List, Optional, Dict

class TimeControl(BaseModel):
    timeEvtType: str
    dimmingLevel: int
    fixedTime: Optional[str] = None
    astroTypeEvt: Optional[str] = None
    offset: int

class Program(BaseModel):
    _id: Dict[str, str]
    controlProgramId: int
    version: int
    name: str
    timeControls: List[TimeControl]
    _class: str
