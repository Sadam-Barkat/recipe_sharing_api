# 🍳 Recipe Sharing Application

A complete recipe sharing platform with a FastAPI backend and Streamlit frontend. This application allows users to create, view, manage, and share cooking recipes with a beautiful and intuitive interface.

## 📋 Project Overview

This project consists of two main components:

1. **Backend API** (`backend/`) - FastAPI-based REST API with MongoDB
2. **Frontend App** (`frontend/`) - Streamlit-based web interface

## 🏗️ Architecture

```
recipe_sharing_api/
├── backend/                 # FastAPI Backend
│   ├── app/
│   │   ├── main.py         # FastAPI application
│   │   ├── config.py       # Configuration settings
│   │   ├── models/         # Pydantic models
│   │   ├── routes/         # API routes
│   │   ├── db/            # Database connection
│   │   └── utils/         # Utility functions
│   ├── requirements.txt   # Backend dependencies
│   └── README.md         # Backend documentation
├── frontend/               # Streamlit Frontend
│   ├── app.py            # Main Streamlit app
│   ├── api_client.py     # API client
│   ├── components.py     # UI components
│   ├── config.py         # Frontend configuration
│   ├── requirements.txt  # Frontend dependencies
│   └── README.md         # Frontend documentation
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **MongoDB** (local or cloud)
- **Git**

### 1. Clone the Repository

```bash
git clone <repository-url>
cd recipe_sharing_api
```

### 2. Set Up Backend

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with MongoDB connection
echo "MONGODB_URI=mongodb://localhost:27017" > .env
echo "DATABASE_NAME=recipe_sharing" >> .env

# Start backend server
uvicorn app.main:app --reload
```

### 3. Set Up Frontend

```bash
# In a new terminal
cd frontend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the frontend
streamlit run app.py
```

### 4. Access the Application

- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Frontend App**: http://localhost:8501

## 🎯 Features

### Backend Features
- ✅ RESTful API with FastAPI
- ✅ MongoDB database integration
- ✅ Pydantic data validation
- ✅ CORS support for frontend
- ✅ Automatic API documentation
- ✅ Error handling and validation

### Frontend Features
- ✅ Modern Streamlit interface
- ✅ Recipe CRUD operations
- ✅ Search and filtering
- ✅ Recipe statistics and analytics
- ✅ Responsive design
- ✅ Real-time updates

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/recipes` | Get all recipes |
| GET | `/recipes/{id}` | Get specific recipe |
| POST | `/recipes` | Create new recipe |
| DELETE | `/recipes/{id}` | Delete recipe |

## 🛠️ Development

### Backend Development

```bash
cd backend
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run tests (if available)
pytest
```

### Frontend Development

```bash
cd frontend
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

# Run with custom port
streamlit run app.py --server.port 8502
```

## 🔧 Configuration

### Backend Configuration

Create a `.env` file in the `backend/` directory:

```env
MONGODB_URI=mongodb://localhost:27017
DATABASE_NAME=recipe_sharing
```

### Frontend Configuration

Create a `.env` file in the `frontend/` directory (optional):

```env
BACKEND_URL=http://localhost:8000
```

## 📝 Usage Examples

### Creating a Recipe via API

```bash
curl -X POST "http://localhost:8000/recipes" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Spaghetti Carbonara",
    "description": "Classic Italian pasta dish",
    "ingredients": ["spaghetti", "eggs", "pecorino cheese", "guanciale"],
    "steps": ["Boil pasta", "Cook guanciale", "Mix with eggs and cheese"]
  }'
```

### Getting All Recipes

```bash
curl "http://localhost:8000/recipes"
```

## 🧪 Testing

### Backend Testing

```bash
cd backend
# Run API tests (if available)
pytest

# Test API endpoints manually
curl http://localhost:8000/
curl http://localhost:8000/recipes
```

### Frontend Testing

```bash
cd frontend
# Run Streamlit app and test manually
streamlit run app.py
```

## 🚀 Deployment

### Backend Deployment

1. **Docker** (recommended):
   ```bash
   docker build -t recipe-api .
   docker run -p 8000:8000 recipe-api
   ```

2. **Cloud Platforms**:
   - Heroku
   - Railway
   - Render
   - AWS/GCP/Azure

### Frontend Deployment

1. **Streamlit Cloud**:
   - Connect your GitHub repository
   - Deploy automatically

2. **Other Platforms**:
   - Heroku
   - Railway
   - Render

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:

1. Check the troubleshooting sections in both backend and frontend READMEs
2. Verify MongoDB is running and accessible
3. Ensure all dependencies are installed
4. Check the terminal for error messages

## 🙏 Acknowledgments

- **FastAPI** for the excellent backend framework
- **Streamlit** for the amazing frontend framework
- **MongoDB** for the database
- **Pydantic** for data validation

---

**Happy Cooking! 🍳👨‍🍳**

*Built with ❤️ using FastAPI and Streamlit* 