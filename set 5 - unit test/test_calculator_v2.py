# Set 5 Class - Unit Test - Test Calculator

from calculator import square

def main():
    test_square()

def test_square(): # Run "pytest" to check code
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

if __name__ == "__main__":
    main()