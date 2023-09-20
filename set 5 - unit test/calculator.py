# Set 5 Class - Unit Test

def main():
    x = int(input("What's x? "))
    print("x square is", square(x))

def square(n):
    return n * n
    # return n + n # Bug

if __name__ == "__main__":
    main()