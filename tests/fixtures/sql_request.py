import sqlite3
import pytest

@pytest.fixture
def fxt_db(request):
    db = sqlite3.connect("tests/testPytest.db")
    def finalize_connection():
        db.close()
    
    request.addfinalizar(finalize_connection)
    return db
    
    
@pytest.fixture
def fxt_cursor(fxt_db):
    cursor = fxt_db.cursor()
    cursor.execute("DELETE FROM personas")
    yield cursor
    cursor.close()

@pytest.fixture
def fake_persona():
    return "Facundo", "Padilla", 1234