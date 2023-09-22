# Set 5 Class - Unit Test - Test Hello

from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == f"hello, David"