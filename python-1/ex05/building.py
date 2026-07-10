import sys


def check_is_punctuation(ch):
    """Return True if ch is a punctuation character."""
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return ch in punctuation


def count_characters(argument):
    """Count and display character categories in the given string."""
    print(f"The text contains {len(argument)} characters:")
    upper_count = 0
    lower_count = 0
    punct_count = 0
    digit_count = 0
    space_count = 0

    for char in argument:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif check_is_punctuation(char):
            punct_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1

    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """Handle command-line arguments and user input."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 2:
            count_characters(sys.argv[1])
        else:
            text = input("What is the text to count?\n")
            count_characters(text)
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
