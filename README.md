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
