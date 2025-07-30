# 🍳 Recipe Sharing App - Frontend

A beautiful and modern Streamlit frontend for the Recipe Sharing API. This application provides an intuitive interface for managing and sharing cooking recipes.

## 🚀 Features

- **📱 Modern UI**: Clean and responsive design with emojis and intuitive navigation
- **🔍 Search & Filter**: Search recipes by name and sort by different criteria
- **➕ Add Recipes**: Easy-to-use form for adding new recipes with ingredients and steps
- **👁️ View Details**: Detailed view of individual recipes
- **🗑️ Delete Recipes**: Remove recipes with confirmation
- **📊 Statistics**: Analytics and insights about your recipe collection
- **🔗 API Integration**: Seamless connection with the backend FastAPI

## 📋 Prerequisites

Before running the frontend, make sure you have:

1. **Python 3.8+** installed
2. **Backend API** running (see backend README for setup)
3. **MongoDB** database configured

## 🛠️ Installation

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. **Create environment file** (optional):
   Create a `.env` file in the frontend directory:
   ```
   BACKEND_URL=http://localhost:8000
   ```

   If no `.env` file is found, the app will use the default backend URL: `http://localhost:8000`

## 🚀 Running the Application

1. **Start the backend API first:**
   ```bash
   cd ../backend
   uvicorn app.main:app --reload
   ```

2. **In a new terminal, start the frontend:**
   ```bash
   cd frontend
   streamlit run app.py
   ```

3. **Open your browser** and navigate to:
   ```
   http://localhost:8501
   ```

## 📁 Project Structure

```
frontend/
├── app.py              # Main Streamlit application
├── api_client.py       # API client for backend communication
├── components.py       # Reusable UI components
├── config.py          # Configuration and settings
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## 🎯 Usage Guide

### Home Page (🏠)
- View all your recipes in a card layout
- Search recipes by name
- Sort recipes by newest, oldest, or title
- Click "View" to see recipe details
- Click "Delete" to remove recipes

### Add Recipe (➕)
- Fill in the recipe title and description
- Add ingredients one by one
- Add cooking steps one by one
- Submit to create the recipe

### Statistics (📊)
- View recipe collection statistics
- See most common ingredients
- Analyze recipe complexity
- Track recent activity

## 🔧 Troubleshooting

### Connection Issues
- Ensure the backend API is running on `http://localhost:8000`
- Check if MongoDB is properly configured
- Verify all environment variables are set correctly

### Import Errors
- Make sure you're in the frontend directory
- Activate the virtual environment
- Install all dependencies with `pip install -r requirements.txt`

### Streamlit Issues
- Clear browser cache if UI doesn't update
- Restart the Streamlit server if needed
- Check the terminal for error messages

## 🎨 Customization

### Styling
The app uses Streamlit's built-in styling with custom CSS. You can modify the appearance by:

1. Adding custom CSS in the `app.py` file
2. Modifying the `PAGE_CONFIG` in `config.py`
3. Updating component layouts in `components.py`

### Features
- Add new pages by extending the sidebar navigation
- Create new components in `components.py`
- Modify API endpoints in `api_client.py`

## 📝 API Endpoints Used

The frontend communicates with these backend endpoints:

- `GET /recipes` - Get all recipes
- `GET /recipes/{id}` - Get specific recipe
- `POST /recipes` - Create new recipe
- `DELETE /recipes/{id}` - Delete recipe

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is part of the Recipe Sharing API project.

## 🆘 Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Verify your backend is running correctly
3. Check the terminal for error messages
4. Ensure all dependencies are installed

---

**Happy Cooking! 🍳👨‍🍳** 