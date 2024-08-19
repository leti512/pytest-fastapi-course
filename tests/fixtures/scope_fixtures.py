import pytest

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0

# Function: cuando se usa una vez, o contiene una operación muy ligera,
@pytest.fixture(scope="function")
def fixture_1():
    global c1
    c1 += 1
    return f"fixture con el scope en class - rep: {c1}"

@pytest.fixture(scope="class")
def fixture_2():
    global c2
    c2 += 1
    return f"fixture con el scope en class - rep: {c1}"

@pytest.fixture(scope="module")
def fixture_3():
    global c3
    c3 += 1
    return f"fixture con el scope en module - rep: {c3}"

@pytest.fixture(scope="package")
def fixture_4():
    global c4
    c4 += 1
    return f"fixture con el scope en module - rep: {c4}"

@pytest.fixture(scope="session")
def fixture_5():
    global c5
    c5 += 1
    return f"fixture con el scope en module - rep: {c5}"


