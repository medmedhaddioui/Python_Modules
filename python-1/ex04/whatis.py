import sys

try:
    if len(sys.argv) == 2:
        number = int (sys.argv[1])
        assert isinstance(number, int)
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"
except AssertionError as e:
    print(e)
except:
    print("AssertionError: argument is not an integer")
