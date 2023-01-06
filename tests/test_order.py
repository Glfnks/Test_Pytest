import pytest


@pytest.mark.run(order=2)
def test_method_1():
    print("Method_1")


@pytest.mark.run(order=1)
def test_method_2():
    print("Method_2")


@pytest.mark.run(order=4)
def test_method_3():
    print("Method_3")


@pytest.mark.run(order=5)
def test_method_4():
    print("Method_4")


@pytest.mark.run(order=3)
def test_method_5():
    print("Method_5")


@pytest.mark.run(order=6)
def test_method_6():
    print("Method_6")
