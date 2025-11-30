from typing import List
from pydantic import BaseModel, Field


class CodeFile(BaseModel):
    filename: str = Field(..., description="Name of the file including extension")
    code: str = Field(..., description="Full file content")


class CodeGenerationOutput(BaseModel):
    """
    Represents code generated for a groomed story.
    ALWAYS uses a list of files.
    """
    files: List[CodeFile] = Field(
        ...,
        description="List of all generated source files (ALWAYS present, even if only one file)"
    )
