# Set 5 Class - Unit Test - Test Calculator

from calculator import square



def test_square():
    if square(2) != 4:
        print("2 square was not 4")
    if square(3) != 9:
        print("3 square was not 9") 