import sys
import ft_filter


def ft_filterstring(s, argv2):
    """Filters words in string s that have a length greater than argv2."""
    try:
        n = int(argv2)
    except ValueError:
        raise AssertionError("the arguments are bad")
    is_valid = [True for c in s if not c.isalpha() and c != ' ']
    if len(is_valid) > 0:
        raise AssertionError("the arguments are bad")

    splited_string = s.split()
    print(ft_filter.ft_filter(lambda x: len(x) > n, splited_string))


def main():
    """Validates the input arguments and invokes ft_filterstring."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        ft_filterstring(sys.argv[1], sys.argv[2])
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
