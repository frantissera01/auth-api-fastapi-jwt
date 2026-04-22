import os
from pathlib import Path

os.environ["DATABASE_URL"] = "sqlite:///./test_auth_api.db"
os.environ["SECRET_KEY"] = "test-secret-key"

from fastapi.testclient import TestClient

from app.db.base import Base
from app.db.session import engine
from app.main import app

client = TestClient(app)


def setup_module() -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def teardown_module() -> None:
    Base.metadata.drop_all(bind=engine)
    db_file = Path("test_auth_api.db")
    if db_file.exists():
        db_file.unlink()


def test_register_login_and_access_protected_routes() -> None:
    register_payload = {
        "email": "admin@example.com",
        "full_name": "Admin User",
        "password": "admin123",
        "role": "admin",
    }

    register_response = client.post("/auth/register", json=register_payload)
    assert register_response.status_code == 201
    assert register_response.json()["email"] == "admin@example.com"

    login_response = client.post(
        "/auth/login",
        data={"username": "admin@example.com", "password": "admin123"},
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    me_response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert me_response.status_code == 200
    assert me_response.json()["role"] == "admin"

    admin_response = client.get(
        "/auth/admin",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert admin_response.status_code == 200
    assert "Welcome admin" in admin_response.json()["message"]
