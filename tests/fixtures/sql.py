import sqlite3
import pytest

@pytest.fixture
def fxt_db():
    db = sqlite3.connect("tests/testPytest.db")
    yield db
    db.close()
    
@pytest.fixture
def fxt_cursor(fxt_db):
    cursor = fxt_db.cursor()
    cursor.execute("DELETE FROM personas")
    yield cursor
    cursor.close()

@pytest.fixture
def fake_persona():
    return "Facundo", "Padilla", 1234