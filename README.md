# Auth API FastAPI JWT

Authentication API built with **FastAPI**, **JWT**, **SQLAlchemy**, and **role-based access control**.

## Features

- User registration
- User login with JWT access token
- Password hashing with bcrypt
- Protected route to get current user
- Admin-only protected route
- SQLite database for easy local setup
- Automated tests with pytest

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT
- Passlib
- Pytest

## Project Structure

```text
auth-api-fastapi-jwt/
├── app/
│   ├── api/
│   │   └── routes_auth.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   ├── token.py
│   │   └── user.py
│   └── main.py
├── tests/
│   └── test_auth.py
├── .env.example
├── requirements.txt
└── README.md
```

## Endpoints

- `POST /auth/register` → create a new user
- `POST /auth/login` → get JWT access token
- `GET /auth/me` → get current authenticated user
- `GET /auth/admin` → admin-only route

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Create `.env`

Copy `.env.example` to `.env` and keep the default values or customize them.

### 3. Run the API

```bash
uvicorn app.main:app --reload
```

### 4. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

## Example Credentials

You can register your own user from Swagger or with the endpoint below.

### Register

```json
{
  "email": "admin@example.com",
  "full_name": "Admin User",
  "password": "admin123",
  "role": "admin"
}
```

### Login

Use form data in Swagger:

- username: `admin@example.com`
- password: `admin123`

## Environment Variables

Example:

```env
SECRET_KEY=change-this-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=60
ALGORITHM=HS256
DATABASE_URL=sqlite:///./auth_api.db
```

## Running Tests

```bash
pytest
```

## Use Case

This project simulates a real-world authentication service with protected routes and role-based access control, a common requirement in backend systems.

## Author

Developed by Franco Tissera as part of a backend portfolio focused on practical APIs and real-world business logic.
