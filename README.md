# SecureBlogAPI

SecureBlogAPI is a FastAPI-based blog application that provides user authentication, blog management, and database-backed storage using SQLite and SQLAlchemy. It is designed as a secure and scalable backend for a simple blogging platform.

## Features

- User registration and authentication
- JWT-based login flow
- CRUD operations for blog posts
- SQLite database integration
- API endpoints built with FastAPI
- Pydantic validation for request/response models

## Tech Stack

- Python 3.x
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT (JSON Web Tokens)
- Uvicorn

Getting Started
1. Clone the repository
bash
git clone https://github.com/ashleythomas18/SecureBlogAPI.git
cd SecureBlogAPI
2. Create a virtual environment
bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
3. Install dependencies
bash
pip install fastapi uvicorn sqlalchemy pydantic python-jose[cryptography] passlib[bcrypt] python-multipart
If your project includes a requirements file, you can also use:

bash
pip install -r requirements.txt
Running the Application
From the project root, start the FastAPI app with:

bash
cd fastapi
uvicorn blog.main:app --reload
Then open the API docs in your browser:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Authentication
This API uses JWT authentication. Users can log in with their email and password to receive an access token, which must be included in the Authorization header for protected routes.

Example login request:

bash
curl -X POST "http://127.0.0.1:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=yourpassword"
Example authenticated request:

bash
curl -X GET "http://127.0.0.1:8000/blog/" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
API Endpoints
Authentication
POST /login — Authenticate user and return JWT token
Users
POST /user/ — Create a new user
GET /user/{id} — Get a user by ID
Blogs
GET /blog/ — Get all blogs
GET /blog/{id} — Get a single blog by ID
POST /blog/ — Create a new blog
PUT /blog/{id} — Update a blog
DELETE /blog/{id} — Delete a blog
Database
The project uses SQLite with the database file:

Text
fastapi/blog/blog.db
The database connection is configured in:

Python
fastapi/blog/database.py
Notes
This project is a solid example of a beginner-to-intermediate FastAPI application with:

SQLAlchemy ORM
JWT authentication
Reusable repository pattern
Modular router-based architecture
License
This project is currently distributed without a formal license. If you plan to publish it publicly, consider adding an open-source license such as MIT.

Contributing
Contributions are welcome. If you'd like to improve the project:

Fork the repository
Create a feature branch
Commit your changes
Open a pull request


## Project Structure

```text
SecureBlogAPI/
├── fastapi/
│   ├── README.md
│   ├── __init__.py
│   └── blog/
│       ├── __init__.py
│       ├── database.py
│       ├── hashing.py
│       ├── JWTtoken.py
│       ├── main.py
│       ├── models.py
│       ├── oauth2.py
│       ├── schemas.py
│       ├── blog.db
│       ├── repository/
│       │   ├── blog.py
│       │   └── user.py
│       └── routers/
│           ├── authentication.py
│           ├── blog.py
│           ├── user.py
│           └── __init__.py
└── README.md
