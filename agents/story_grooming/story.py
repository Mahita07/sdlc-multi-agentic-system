from typing import List
from pydantic import BaseModel, Field

class GroomedStory(BaseModel):
    description: str = Field(..., description="Refined, clear, unambiguous description of the story")
    acceptance_criteria: List[str] = Field(
        ..., 
        description="List of explicit, testable criteria describing the story behaviour"
    )
    tech_notes: List[str] = Field(
        ..., 
        description="List of technical considerations, dependencies, constraints, risks, or open questions"
    )
