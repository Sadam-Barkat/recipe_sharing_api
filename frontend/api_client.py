# frontend/api_client.py

import requests
import json
from typing import List, Dict, Optional
from config import RECIPES_ENDPOINT

class RecipeAPIClient:
    """Client for interacting with the Recipe Sharing API"""
    
    def __init__(self, base_url: str = RECIPES_ENDPOINT):
        self.base_url = base_url
    
    def get_all_recipes(self) -> List[Dict]:
        """Fetch all recipes from the API"""
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching recipes: {e}")
            return []
    
    def get_recipe_by_id(self, recipe_id: str) -> Optional[Dict]:
        """Fetch a specific recipe by ID"""
        try:
            response = requests.get(f"{self.base_url}/{recipe_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching recipe {recipe_id}: {e}")
            return None
    
    def create_recipe(self, recipe_data: Dict) -> Optional[Dict]:
        """Create a new recipe"""
        try:
            response = requests.post(
                self.base_url,
                json=recipe_data,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating recipe: {e}")
            return None
    
    def delete_recipe(self, recipe_id: str) -> bool:
        """Delete a recipe by ID"""
        try:
            response = requests.delete(f"{self.base_url}/{recipe_id}")
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error deleting recipe {recipe_id}: {e}")
            return False
    
    def test_connection(self) -> bool:
        """Test if the backend API is accessible"""
        try:
            response = requests.get(self.base_url)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False 