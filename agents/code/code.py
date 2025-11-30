from typing import List, Union
from pydantic import BaseModel, Field

class CodeFile(BaseModel):
    filename: str = Field(..., description="Name of the file including extension")
    code: str = Field(..., description="Production-ready code for this file")

class CodeGenerationOutput(BaseModel):
    """
    Represents code generated for a groomed story.
    Can be either a single file or multiple files.
    """
    single_file: Union[str, None] = Field(
        None, 
        description="If the code fits in a single file, return it here as a string"
    )
    files: List[CodeFile] = Field(
        default_factory=list,
        description="List of code files if multiple files are needed"
    )
