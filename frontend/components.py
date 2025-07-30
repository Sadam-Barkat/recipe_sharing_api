# frontend/components.py

import streamlit as st
import pandas as pd
from typing import List, Dict, Optional
from datetime import datetime

def display_recipe_card(recipe: Dict, show_actions: bool = True):
    """Display a recipe in a card format"""
    with st.container():
        st.markdown("---")
        
        # Recipe header
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader(f"🍽️ {recipe['title']}")
            if recipe.get('description'):
                st.write(f"*{recipe['description']}*")
        
        with col2:
            if show_actions:
                if st.button(f"🗑️ Delete", key=f"delete_{recipe['id']}"):
                    return "delete", recipe['id']
                if st.button(f"👁️ View", key=f"view_{recipe['id']}"):
                    return "view", recipe['id']
        
        # Recipe details
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Ingredients:**")
            for i, ingredient in enumerate(recipe['ingredients'], 1):
                st.write(f"{i}. {ingredient}")
        
        with col2:
            st.write("**Steps:**")
            for i, step in enumerate(recipe['steps'], 1):
                st.write(f"{i}. {step}")
        
        # Recipe metadata
        st.caption(f"Created: {recipe['created_at'][:10]}")
        
    return None, None

def create_recipe_form():
    """Create a form for adding new recipes"""
    st.subheader("➕ Add New Recipe")
    
    # Initialize session state for ingredients and steps
    if 'ingredients' not in st.session_state:
        st.session_state.ingredients = []
    if 'steps' not in st.session_state:
        st.session_state.steps = []
    
    # Basic recipe info
    title = st.text_input("Recipe Title", placeholder="e.g., Spaghetti Carbonara")
    description = st.text_area("Description (optional)", placeholder="Brief description of the recipe...")
    
    # Ingredients section
    st.write("**Ingredients:**")
    col1, col2 = st.columns([3, 1])
    with col1:
        ingredient_input = st.text_input("Add ingredient", key="ingredient_input", placeholder="e.g., 200g spaghetti")
    with col2:
        if st.button("Add Ingredient", key="add_ingredient"):
            if ingredient_input.strip():
                st.session_state.ingredients.append(ingredient_input.strip())
                st.rerun()
    
    # Display added ingredients
    if st.session_state.ingredients:
        st.write("**Current Ingredients:**")
        for i, ingredient in enumerate(st.session_state.ingredients, 1):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"{i}. {ingredient}")
            with col2:
                if st.button(f"Remove", key=f"remove_ingredient_{i}"):
                    st.session_state.ingredients.pop(i-1)
                    st.rerun()
    
    # Steps section
    st.write("**Steps:**")
    col1, col2 = st.columns([3, 1])
    with col1:
        step_input = st.text_area("Add step", key="step_input", placeholder="e.g., Boil water and cook pasta")
    with col2:
        if st.button("Add Step", key="add_step"):
            if step_input.strip():
                st.session_state.steps.append(step_input.strip())
                st.rerun()
    
    # Display added steps
    if st.session_state.steps:
        st.write("**Current Steps:**")
        for i, step in enumerate(st.session_state.steps, 1):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"{i}. {step}")
            with col2:
                if st.button(f"Remove", key=f"remove_step_{i}"):
                    st.session_state.steps.pop(i-1)
                    st.rerun()
    
    # Submit form
    if st.button("Create Recipe", key="create_recipe", type="primary"):
        if not title.strip():
            st.error("Recipe title is required!")
            return None
        
        if not st.session_state.ingredients:
            st.error("At least one ingredient is required!")
            return None
        
        if not st.session_state.steps:
            st.error("At least one step is required!")
            return None
        
        recipe_data = {
            "title": title.strip(),
            "description": description.strip() if description.strip() else None,
            "ingredients": st.session_state.ingredients.copy(),
            "steps": st.session_state.steps.copy()
        }
        
        # Clear session state
        st.session_state.ingredients = []
        st.session_state.steps = []
        
        return recipe_data
    
    return None

def display_recipe_details(recipe: Dict):
    """Display detailed view of a recipe"""
    st.markdown("---")
    st.subheader(f"🍽️ {recipe['title']}")
    
    if recipe.get('description'):
        st.write(f"*{recipe['description']}*")
    
    # Recipe content in columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**📋 Ingredients:**")
        for i, ingredient in enumerate(recipe['ingredients'], 1):
            st.write(f"• {ingredient}")
    
    with col2:
        st.write("**👨‍🍳 Instructions:**")
        for i, step in enumerate(recipe['steps'], 1):
            st.write(f"{i}. {step}")
    
    # Metadata
    st.caption(f"Created: {recipe['created_at']}")
    
    # Back button
    if st.button("← Back to Recipes"):
        st.session_state.current_view = "list"
        st.rerun()

def display_connection_status(is_connected: bool):
    """Display backend connection status"""
    if is_connected:
        st.success("✅ Connected to backend API")
    else:
        st.error("❌ Cannot connect to backend API. Please ensure the backend is running.")
        st.info("💡 Make sure to start the backend server with: `uvicorn app.main:app --reload`")

def display_recipe_stats(recipes: List[Dict]):
    """Display recipe statistics"""
    if not recipes:
        return
    
    st.subheader("📊 Recipe Statistics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Recipes", len(recipes))
    
    with col2:
        avg_ingredients = sum(len(recipe['ingredients']) for recipe in recipes) / len(recipes)
        st.metric("Avg Ingredients", f"{avg_ingredients:.1f}")
    
    with col3:
        avg_steps = sum(len(recipe['steps']) for recipe in recipes) / len(recipes)
        st.metric("Avg Steps", f"{avg_steps:.1f}")
    
    # Recipe creation timeline
    if len(recipes) > 1:
        st.write("**📈 Recent Activity:**")
        recent_recipes = sorted(recipes, key=lambda x: x['created_at'], reverse=True)[:5]
        for recipe in recent_recipes:
            st.write(f"• {recipe['title']} - {recipe['created_at'][:10]}") 