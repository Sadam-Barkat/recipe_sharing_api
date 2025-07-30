# backend/models/recipe_model.py

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Pydantic model for request/response validation
class RecipeModel(BaseModel):
    title: str = Field(..., example="Spaghetti Carbonara")
    description: Optional[str] = Field(None, example="A classic Italian pasta dish.")
    ingredients: List[str] = Field(..., example=["spaghetti", "eggs", "cheese", "bacon"])
    steps: List[str] = Field(..., example=["Boil pasta", "Cook bacon", "Mix ingredients"])
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        schema_extra = {
            "example": {
                "title": "Spaghetti Carbonara",
                "description": "A classic Italian pasta dish.",
                "ingredients": ["spaghetti", "eggs", "cheese", "bacon"],
                "steps": ["Boil pasta", "Cook bacon", "Mix ingredients"]
            }
        }

# Helper to convert MongoDB _id to string
def recipe_serializer(recipe) -> dict:
    return {
        "id": str(recipe["_id"]),
        "title": recipe["title"],
        "description": recipe.get("description"),
        "ingredients": recipe["ingredients"],
        "steps": recipe["steps"],
        "created_at": recipe["created_at"].isoformat()
    }
