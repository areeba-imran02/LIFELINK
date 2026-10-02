from typing import List, Optional
from pydantic import BaseModel, Field

class Need(BaseModel):
    raw_request: str
    category: str
    summary: str
    location: str
    urgency: str
    budget: Optional[float] = None
    constraints: List[str] = Field(default_factory=list)
    keywords: List[str] = Field(default_factory=list)

class Resource(BaseModel):
    id: str
    name: str
    type: str
    category: str
    description: str
    city: str
    country: str
    services: List[str]
    accessibility: List[str] = Field(default_factory=list)
    estimated_cost: str = "Unknown"
    available: bool = False
    rating: float = 0.0
    verified: bool = False
    contact: str = ""

class Match(BaseModel):
    resource: Resource
    match_score: int
    distance: str
    data_status: str

class AgentEvent(BaseModel):
    agent: str
    action: str
    output: str
