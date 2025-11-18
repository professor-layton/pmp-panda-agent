from typing import Any
from pydantic import BaseModel
from pydantic.alias_generators import to_camel

class BaseParentModel(BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True
        extra = "forbid"

Json = dict[str, Any] # define a type alias for JSON objects
