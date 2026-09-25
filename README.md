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

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ashleythomas18/SecureBlogAPI.git
cd SecureBlogAPI
```

### 2. Create a Virtual Environment

#### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic python-jose[cryptography] passlib[bcrypt] python-multipart
```

If the project includes a `requirements.txt` file, install the dependencies with:

```bash
pip install -r requirements.txt
```

## Running the Application

From the project root, navigate to the `fastapi` directory:

```bash
cd fastapi
uvicorn blog.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### API Documentation

Once the application is running, open one of the following URLs in your browser:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Authentication

SecureBlogAPI uses JWT authentication. Users can log in with their email address and password to receive an access token.

The access token must be included in the `Authorization` header when accessing protected endpoints.

### Login Request

```bash
curl -X POST "http://127.0.0.1:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=yourpassword"
```

A successful response will return an access token:

```json
{
  "access_token": "your-access-token",
  "token_type": "bearer"
}
```

### Authenticated Request

Use the returned token as a Bearer token:

```bash
curl -X GET "http://127.0.0.1:8000/blog/" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/login` | Authenticate a user and return a JWT access token |

### Users

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/user/` | Create a new user |
| `GET` | `/user/{id}` | Retrieve a user by ID |

### Blogs

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/blog/` | Retrieve all blog posts |
| `GET` | `/blog/{id}` | Retrieve a single blog post |
| `POST` | `/blog/` | Create a new blog post |
| `PUT` | `/blog/{id}` | Update an existing blog post |
| `DELETE` | `/blog/{id}` | Delete a blog post |

## Database

SecureBlogAPI uses SQLite as its database.

The database file is located at:

```text
fastapi/blog/blog.db
```

The database connection and SQLAlchemy configuration are defined in:

```text
fastapi/blog/database.py
```

Database tables are created automatically when the application starts.

## Project Architecture

The project uses a modular FastAPI structure:

- **Routers** — Define API endpoints for authentication, users, and blogs.
- **Schemas** — Validate request and response data using Pydantic.
- **Models** — Define database tables using SQLAlchemy.
- **Repositories** — Contain database operations and business logic.
- **OAuth2/JWT** — Handle authentication and protected routes.
- **SQLite** — Store users and blog posts.

## Key Technologies

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- JWT authentication
- OAuth2
- Passlib password hashing

## Notes

SecureBlogAPI is a beginner-to-intermediate FastAPI project demonstrating:

- RESTful API development
- JWT-based authentication
- Password hashing
- SQLAlchemy ORM
- SQLite database integration
- Pydantic data validation
- Repository pattern
- Modular router-based architecture

## Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new feature branch.

   ```bash
   git checkout -b feature/your-feature
   ```

3. Make your changes.
4. Commit your changes.

   ```bash
   git commit -m "Add your feature"
   ```

5. Push your branch.

   ```bash
   git push origin feature/your-feature
   ```

6. Open a pull request.

## License

This project does not currently include a formal open-source license.

If you plan to distribute or reuse this project, consider adding a license such as the [MIT License](https://opensource.org/licenses/MIT).

## Contact

For questions, suggestions, or collaboration, visit the GitHub repository:

https://github.com/ashleythomas18/SecureBlogAPI


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
