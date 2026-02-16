# ⚡ FastAPI-REST-APIs - Modern REST API Development

A collection of FastAPI-REST-APIs and exercises demonstrating modern Python web API development, including RESTful services, authentication, database integration, and best practices.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 About

This repository showcases my journey learning FastAPI - a modern, fast (high-performance) web framework for building APIs with Python 3.9+ based on standard Python type hints. Each project demonstrates different aspects of API development from basic CRUD operations to advanced features like authentication, database integration, and real-time capabilities.

**Why FastAPI?**
- ⚡ High performance - comparable to NodeJS and Go
- 📚 Automatic interactive API documentation (Swagger UI)
- 🔒 Built-in data validation with Pydantic
- 🚀 Async/await support for concurrent operations
- 🎯 Type hints for better IDE support and fewer bugs

## 📋 Table of Contents

- [Projects Overview](#projects-overview)
- [Features Demonstrated](#features-demonstrated)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Projects](#running-the-projects)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Learning Resources](#learning-resources)
- [Contact](#contact)

## 🚀 Projects Overview

### 1. Basic CRUD API
**Description**: Simple REST API for managing items/resources  
**Endpoints**: GET, POST, PUT, DELETE operations  
**Concepts**: 
- Path parameters and query parameters
- Request/Response models with Pydantic
- HTTP status codes
- API versioning


---

### 2. User Authentication System
**Description**: JWT-based authentication and authorization  
**Features**:
- User registration and login
- Password hashing with bcrypt
- JWT token generation and validation
- Protected routes with dependencies

**Concepts**: 
- OAuth2 with Password flow
- Security best practices
- Token-based authentication


---

### 3. Database Integration (SQLAlchemy)
**Description**: API with PostgreSQL/MySQL database  
**Features**:
- Database connection and session management
- ORM models with SQLAlchemy
- Database migrations with Alembic
- Relationship mapping (One-to-Many, Many-to-Many)

**Concepts**:
- Database design patterns
- Connection pooling
- Transaction management


---

### 4. Todo API with Full Features
**Description**: Production-ready Todo application API  
**Features**:
- Complete CRUD operations
- User authentication
- Database persistence
- Input validation
- Error handling
- API documentation

**Tech Stack**: FastAPI + SQLAlchemy + PostgreSQL + JWT


---

### 5. File Upload/Download API
**Description**: Handle file uploads and serve files  
**Features**:
- Multiple file upload
- File type validation
- Image processing (resize, compress)
- Serve static files
- Download endpoints

**Concepts**:
- File handling in FastAPI
- Static file serving
- Streaming responses


---

### 6. WebSocket Real-time Chat
**Description**: Real-time bidirectional communication  
**Features**:
- WebSocket connections
- Real-time message broadcasting
- Connection management
- Chat rooms

**Concepts**:
- WebSocket protocol
- Async programming
- Real-time communication


---

### 7. Background Tasks & Celery
**Description**: Asynchronous task processing  
**Features**:
- Background task execution
- Email sending
- Report generation
- Scheduled tasks

**Concepts**:
- Background tasks
- Task queues (Celery)
- Redis as message broker


---

### 8. API Rate Limiting & Caching
**Description**: Performance optimization techniques  
**Features**:
- Rate limiting per user/IP
- Redis caching
- Response caching
- Request throttling

**Concepts**:
- Middleware implementation
- Caching strategies
- Performance optimization


---

*[Add more projects as you build them]*

## ✨ Features Demonstrated

### Core FastAPI Features
- ✅ RESTful API design principles
- ✅ Automatic interactive documentation (Swagger UI & ReDoc)
- ✅ Request/Response validation with Pydantic
- ✅ Dependency injection system
- ✅ Path operations and route handling
- ✅ Query parameters, path parameters, request body
- ✅ Error handling and custom exceptions
- ✅ Status codes and response models

### Advanced Features
- 🔐 Authentication & Authorization (JWT, OAuth2)
- 💾 Database integration (SQLAlchemy ORM)
- 📁 File handling (upload/download)
- 🔌 WebSocket support for real-time features
- ⚡ Background tasks & async processing
- 🚦 Middleware (CORS, rate limiting, logging)
- 📊 API versioning
- 🧪 Testing with pytest
- 🐳 Docker containerization
- 📝 API documentation best practices

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **FastAPI** | Web framework |
| **Uvicorn** | ASGI server |
| **Pydantic** | Data validation |
| **SQLAlchemy** | ORM for database |
| **Alembic** | Database migrations |
| **PostgreSQL/MySQL** | Relational database |
| **Redis** | Caching & message broker |
| **JWT** | Authentication tokens |
| **Pytest** | Testing framework |
| **Docker** | Containerization |

## 📦 Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- PostgreSQL/MySQL (for database projects)
- Redis (for caching/background tasks)
- Git

### Setup Instructions

1. **Clone the repository**
```bash
https://github.com/nushant22/FastAPI-REST-APIs.git
cd FastAPI-REST-APIs
```

2. **Create virtual environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Create .env file
cp .env.example .env

# Edit .env with your configuration
# DATABASE_URL=postgresql://user:password@localhost/dbname
# SECRET_KEY=your-secret-key-here
# REDIS_URL=redis://localhost:6379
```

5. **Set up database** (for projects requiring database)
```bash
# Run migrations
alembic upgrade head
```

## 🚀 Running the Projects

### Start the development server

```bash
# Navigate to specific project folder
cd project_folder_name

# Run with uvicorn
uvicorn main:app --reload

# Or specify host and port
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Access the application
- **API**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📚 API Documentation

Each project includes automatic interactive documentation:

### Swagger UI (OpenAPI)
Visit `/docs` endpoint to:
- View all available endpoints
- Test API calls directly in browser
- See request/response schemas
- View authentication requirements

### Example API Endpoints

```
# Health check
GET /health

# User authentication
POST /auth/register
POST /auth/login
POST /auth/refresh

# CRUD operations
GET    /api/v1/items          # Get all items
GET    /api/v1/items/{id}     # Get specific item
POST   /api/v1/items          # Create new item
PUT    /api/v1/items/{id}     # Update item
DELETE /api/v1/items/{id}     # Delete item
```

### Sample Request/Response

**POST /api/v1/items**
```json
// Request Body
{
  "name": "Sample Item",
  "description": "This is a sample item",
  "price": 29.99,
  "is_available": true
}

// Response (201 Created)
{
  "id": 1,
  "name": "Sample Item",
  "description": "This is a sample item",
  "price": 29.99,
  "is_available": true,
  "created_at": "2026-02-16T10:30:00Z"
}
```

## 📂 Project Structure

```
FastAPI-REST-APIs/
│
├── 01_basic_crud/
│   ├── main.py              # Application entry point
│   ├── models.py            # Pydantic models
│   ├── routes.py            # API routes
│   └── README.md            # Project-specific docs
│
├── 02_authentication/
│   ├── main.py
│   ├── auth/
│   │   ├── jwt.py          # JWT handling
│   │   ├── hashing.py      # Password hashing
│   │   └── dependencies.py # Auth dependencies
│   ├── models.py
│   └── routes.py
│
├── 03_database_integration/
│   ├── main.py
│   ├── database.py         # Database connection
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── crud.py             # CRUD operations
│   └── alembic/            # Database migrations
│
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── docker-compose.yml      # Docker configuration
└── README.md               # This file
```

## 🧪 Testing

Each project includes tests using pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_api.py

# Run with verbose output
pytest -v
```

## 🐳 Docker Deployment

Build and run with Docker:

```bash
# Build image
docker build -t FastAPI-REST-APIs .

# Run container
docker run -p 8000:8000 FastAPI-REST-APIs

# Or use docker-compose
docker-compose up -d
```

## 📖 Learning Resources

### Official Documentation
- [FastAPI Official Docs](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

### Tutorials I Found Helpful
- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [Real Python - FastAPI Guide](https://realpython.com/fastapi-python-web-apis/)
- [TestDriven.io - FastAPI Course](https://testdriven.io/courses/tdd-fastapi/)

### Video Courses
- [FastAPI - freeCodeCamp](https://www.youtube.com/watch?v=0sOvCWFmrtA)
- [FastAPI Full Course - Sanjeev Thiyagarajan](https://www.youtube.com/watch?v=0sOvCWFmrtA)

## 🎓 Key Learnings

Through these FastAPI projects, I've gained:

- ✅ Modern Python web development skills
- ✅ RESTful API design principles
- ✅ Asynchronous programming with async/await
- ✅ Database design and ORM usage
- ✅ Authentication and security best practices
- ✅ API testing and documentation
- ✅ Performance optimization techniques
- ✅ Deployment and containerization
- ✅ Real-time communication with WebSockets
- ✅ Background task processing

## 🤝 Contributing

Contributions are welcome! If you have improvements or new examples:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewExample`)
3. Commit your changes (`git commit -m 'Add new example'`)
4. Push to the branch (`git push origin feature/NewExample`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Nushant Ghimire**

- LinkedIn: [nushant-ghimire-861b87325](https://www.linkedin.com/in/nushant-ghimire-861b87325/)
- GitHub: [@nushant22](https://github.com/nushant22)
- Email: [nushantghimire22@gmail.com]

## 🙏 Acknowledgments

- FastAPI creator [Sebastián Ramírez](https://github.com/tiangolo)
- FastAPI community for excellent documentation
- Stack Overflow community for troubleshooting help

---

⭐ **If you find this repository helpful, please give it a star!**

🚀 **Building APIs with FastAPI?** Let's connect and share knowledge!

*Last Updated: February 2026*
