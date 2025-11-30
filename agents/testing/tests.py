from typing import List, Union
from pydantic import BaseModel, Field

class UnitTestFile(BaseModel):
    filename: str = Field(..., description="Name of the test file including extension")
    test_code: str = Field(..., description="Production-ready unit test code for this file")

class UnitTestGeneration(BaseModel):
    """
    Unit tests generated for a groomed story.
    Can be either single-file or multi-file.
    """
    single_file: Union[str, None] = Field(
        None,
        description="All unit tests in a single file if sufficient"
    )
    files: List[UnitTestFile] = Field(
        default_factory=list,
        description="List of test files if multiple files are required"
    )
    description: str = Field(..., description="Short summary of what the unit tests verify")
    tech_notes: List[str] = Field(
        default_factory=list,
        description="Any assumptions, dependencies, or considerations relevant to the unit tests"
    )
