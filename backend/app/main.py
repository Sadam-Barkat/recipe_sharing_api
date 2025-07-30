# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.recipe_routes import router as recipe_router

app = FastAPI(
    title="Recipe Sharing API",
    description="A simple API to manage and share cooking recipes.",
    version="1.0.0"
)

# (Optional) CORS setup for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace * with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(recipe_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe Sharing API"}
