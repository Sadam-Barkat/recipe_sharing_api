# backend/routes/recipe_routes.py

from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.models.recipe_model import RecipeModel, recipe_serializer
from app.db.connection import recipe_collection

router = APIRouter(prefix="/recipes", tags=["Recipes"])


@router.post("/", response_model=dict)
def create_recipe(recipe: RecipeModel):
    recipe_dict = recipe.model_dump()
    result = recipe_collection.insert_one(recipe_dict)
    return {"message": "Recipe added successfully", "id": str(result.inserted_id)}


@router.get("/", response_model=list)
def get_all_recipes():
    recipes = recipe_collection.find()
    return [recipe_serializer(r) for r in recipes]


@router.get("/{recipe_id}", response_model=dict)
def get_recipe(recipe_id: str):
    if not ObjectId.is_valid(recipe_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    return recipe_serializer(recipe)


@router.delete("/{recipe_id}", response_model=dict)
def delete_recipe(recipe_id: str):
    if not ObjectId.is_valid(recipe_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    
    result = recipe_collection.delete_one({"_id": ObjectId(recipe_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    return {"message": "Recipe deleted successfully"}
