import pytest

@pytest.fixture
def fixture_nombre():
    return "Facundo"

@pytest.fixture
def fixture_apellido():
    return "Perez"

@pytest.fixture
def fixture_dni():
    return 1234