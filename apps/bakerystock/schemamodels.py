from pydantic import BaseModel, Field


class SchemaPostLocations(BaseModel):
    location: str
    department: str
    category: str
    subcategory: str
