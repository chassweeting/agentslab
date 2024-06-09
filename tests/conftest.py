"""Conftest is automatically discovered by Pytest, usefulf for sharing fixtures."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.backend.db.database import Base, get_db
from src.backend.db.initial_data_loader import load_customers, load_regular_menus
from src.backend.db.models import Customer, MenuItem, Order, OrderItem  # noqa: imported to create tables
from src.backend.main import app

# In-memory SQLite for testing
# BUT note that it may be better to use a temporary file-based database instead due to risks of in-memory databases.
# Note: every time you connect to in-memory database, it creates new separate database !
# https://stackoverflow.com/questions/9999765/when-i-use-fixture-with-sqlalchemy-in-my-unit-tests-why-am-i-unable-to-confirm
DATABASE_URL = "sqlite:///:memory:"

# Setup the engine for an in-memory SQLite database.
test_engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})
TestSessionLocal = sessionmaker(bind=test_engine)


@pytest.fixture(scope="module")  # fixture is set up once per module (file) and reused for all tests in that module
def db_session():
    """Create a new database session for a test.  Used when testing DB models.
    Based on https://coderpad.io/blog/development/a-guide-to-database-unit-testing-with-pytest-and-sqlalchemy/
    """
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    session = TestSessionLocal()

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=test_engine)  # Clean up after tests


@pytest.fixture(scope="module")
def client(db_session):
    """TestClient is used to simulate requests to your API
    Reference https://stackoverflow.com/questions/67255653/how-to-set-up-and-tear-down-a-database-between-tests-in-fastapi
    """

    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    # Use dependency override to replace the database session with our test session
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    # Clean up the overrides after tests
    app.dependency_overrides.clear()

