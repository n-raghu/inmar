from pydantic import BaseModel, Field


class SchemaPostLocations(BaseModel):
    location: str
    department: str
    category: str
    subcategory: str


class SchemaPutLocations(BaseModel):
    location: str = None
    department: str = None
    category: str = None
    subcategory: str = None
