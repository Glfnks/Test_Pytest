import pytest


@pytest.fixture()
def login():
    print("Login - ok")
    yield
    print("Logout ok")


# @pytest.fixture(scope="module")
# def start():
#     print("Start")
#     yield
#     print("Finish")

@pytest.fixture(scope="function")
def start():
    print("Start")
    yield
    print("Finish")

