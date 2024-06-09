"""Conftest is automatically discovered by Pytest, usefulf for sharing fixtures."""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient


from src.backend.main import app
from src.backend.db.database import Base, get_db
from src.backend.db.models import MenuItem, Customer, Order, OrderItem   # noqa: imported to create tables
from src.backend.db.initial_data_loader import load_regular_menus, load_customers


# In-memory SQLite for testing
DATABASE_URL = "sqlite:///:memory:"

# Setup the engine for an in-memory SQLite database.
# Note: every time you connect to in-memory database, it creates new separate database !
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


#
# @pytest.fixture(scope="session")
# def db_engine():
#     """Create a single engine instance for the session."""
#     # Create tables in the in-memory database
#     Base.metadata.create_all(bind=test_engine)
#     yield test_engine
#     # Drop tables after the session
#     Base.metadata.drop_all(bind=test_engine)
#
#
# @pytest.fixture(scope="session")
# def db_connection(db_engine):
#     """Create a single connection for the session."""
#     connection = db_engine.connect()
#     yield connection
#     connection.close()
#
#
# @pytest.fixture(scope="function")
# def db_session(db_connection):
#     """Create a new database session for a test. Used when testing DB models."""
#     # Start a transaction and use the connection
#     transaction = db_connection.begin()
#     session = TestSessionLocal(bind=db_connection)
#
#     try:
#         yield session
#     finally:
#         # Rollback the transaction after each test
#         transaction.rollback()
#         session.close()
#
#
# @pytest.fixture(scope="function")
# def client(db_session):
#     """TestClient is used to simulate requests to your API."""
#     # Override the default get_db dependency with the session used in tests
#     def override_get_db():
#         try:
#             yield db_session
#         finally:
#             db_session.close()
#
#     app.dependency_overrides[get_db] = override_get_db
#
#     with TestClient(app) as test_client:
#         yield test_client
#
