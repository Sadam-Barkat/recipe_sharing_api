# frontend/app.py

import streamlit as st
import sys
import os

# Add the current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import APP_TITLE, APP_ICON, PAGE_CONFIG
from api_client import RecipeAPIClient
from components import (
    display_recipe_card, 
    create_recipe_form, 
    display_recipe_details,
    display_connection_status,
    display_recipe_stats
)

def main():
    """Main Streamlit application"""
    
    # Page configuration
    st.set_page_config(**PAGE_CONFIG)
    
    # Initialize session state
    if 'current_view' not in st.session_state:
        st.session_state.current_view = "list"
    if 'selected_recipe' not in st.session_state:
        st.session_state.selected_recipe = None
    
    # Header
    st.title(f"{APP_ICON} {APP_TITLE}")
    st.markdown("---")
    
    # Initialize API client
    api_client = RecipeAPIClient()
    
    # Test connection
    is_connected = api_client.test_connection()
    display_connection_status(is_connected)
    
    if not is_connected:
        st.stop()
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["🏠 Home", "➕ Add Recipe", "📊 Statistics"]
    )
    
    # Main content area
    if page == "🏠 Home":
        show_home_page(api_client)
    elif page == "➕ Add Recipe":
        show_add_recipe_page(api_client)
    elif page == "📊 Statistics":
        show_statistics_page(api_client)

def show_home_page(api_client):
    """Display the home page with recipe list"""
    st.header("🍽️ Recipe Collection")
    
    # Get all recipes
    recipes = api_client.get_all_recipes()
    
    if not recipes:
        st.info("No recipes found. Add your first recipe!")
        return
    
    # Search and filter
    col1, col2 = st.columns([2, 1])
    with col1:
        search_term = st.text_input("🔍 Search recipes", placeholder="Enter recipe name...")
    with col2:
        sort_by = st.selectbox("Sort by", ["Newest", "Oldest", "Title"])
    
    # Filter recipes based on search
    if search_term:
        recipes = [r for r in recipes if search_term.lower() in r['title'].lower()]
    
    # Sort recipes
    if sort_by == "Newest":
        recipes = sorted(recipes, key=lambda x: x['created_at'], reverse=True)
    elif sort_by == "Oldest":
        recipes = sorted(recipes, key=lambda x: x['created_at'])
    elif sort_by == "Title":
        recipes = sorted(recipes, key=lambda x: x['title'])
    
    # Display recipes
    if st.session_state.current_view == "list":
        st.write(f"Found {len(recipes)} recipe(s)")
        
        for recipe in recipes:
            action, recipe_id = display_recipe_card(recipe)
            
            if action == "delete":
                if st.button(f"Confirm Delete", key=f"confirm_delete_{recipe_id}"):
                    if api_client.delete_recipe(recipe_id):
                        st.success("Recipe deleted successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to delete recipe")
            
            elif action == "view":
                st.session_state.current_view = "detail"
                st.session_state.selected_recipe = recipe_id
                st.rerun()
    
    elif st.session_state.current_view == "detail":
        if st.session_state.selected_recipe:
            recipe = api_client.get_recipe_by_id(st.session_state.selected_recipe)
            if recipe:
                display_recipe_details(recipe)
            else:
                st.error("Recipe not found")
                st.session_state.current_view = "list"
                st.rerun()

def show_add_recipe_page(api_client):
    """Display the add recipe page"""
    st.header("➕ Add New Recipe")
    
    # Create recipe form
    recipe_data = create_recipe_form()
    
    if recipe_data:
        # Submit recipe to API
        result = api_client.create_recipe(recipe_data)
        
        if result:
            st.success("✅ Recipe created successfully!")
            st.balloons()
            
            # Show the created recipe
            st.subheader("Created Recipe:")
            display_recipe_details({
                "title": recipe_data["title"],
                "description": recipe_data.get("description"),
                "ingredients": recipe_data["ingredients"],
                "steps": recipe_data["steps"],
                "created_at": "Just now"
            })
        else:
            st.error("❌ Failed to create recipe. Please try again.")

def show_statistics_page(api_client):
    """Display recipe statistics"""
    st.header("📊 Recipe Statistics")
    
    # Get all recipes
    recipes = api_client.get_all_recipes()
    
    if not recipes:
        st.info("No recipes found. Add some recipes to see statistics!")
        return
    
    # Display statistics
    display_recipe_stats(recipes)
    
    # Additional analytics
    st.subheader("📈 Recipe Analytics")
    
    # Ingredients analysis
    all_ingredients = []
    for recipe in recipes:
        all_ingredients.extend(recipe['ingredients'])
    
    if all_ingredients:
        st.write("**Most Common Ingredients:**")
        ingredient_counts = {}
        for ingredient in all_ingredients:
            ingredient_counts[ingredient] = ingredient_counts.get(ingredient, 0) + 1
        
        # Show top 5 most common ingredients
        top_ingredients = sorted(ingredient_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        for ingredient, count in top_ingredients:
            st.write(f"• {ingredient}: {count} times")
    
    # Recipe complexity analysis
    st.write("**Recipe Complexity:**")
    simple_recipes = [r for r in recipes if len(r['ingredients']) <= 3 and len(r['steps']) <= 3]
    medium_recipes = [r for r in recipes if 4 <= len(r['ingredients']) <= 6 or 4 <= len(r['steps']) <= 6]
    complex_recipes = [r for r in recipes if len(r['ingredients']) > 6 or len(r['steps']) > 6]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Simple Recipes", len(simple_recipes))
    with col2:
        st.metric("Medium Recipes", len(medium_recipes))
    with col3:
        st.metric("Complex Recipes", len(complex_recipes))

if __name__ == "__main__":
    main() 