from typing import List
from pydantic import BaseModel, Field


class UnitTestFile(BaseModel):
    filename: str = Field(..., description="Name of the test file including extension")
    test_code: str = Field(..., description="Full unit test file content")


class UnitTestGeneration(BaseModel):
    """
    Represents unit tests generated for a groomed story.
    ALWAYS uses a list of files.
    """
    files: List[UnitTestFile] = Field(
        ...,
        description="List of all generated test files (ALWAYS present, even if only one file)"
    )
    description: str = Field(..., description="Short summary of what the unit tests verify")
    tech_notes: List[str] = Field(
        default_factory=list,
        description="Assumptions, dependencies, or considerations relevant to the unit tests"
    )
