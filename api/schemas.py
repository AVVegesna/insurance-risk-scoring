from pydantic import BaseModel, Field
from typing import Literal

class ClaimInput(BaseModel):
    age: int = Field(..., ge=18, le=100)
    tenure: int = Field(..., ge=0)
    vehicle_type: Literal["Sedan", "SUV", "Truck", "Motorcycle"]
    claims_history: int = Field(..., ge=0)