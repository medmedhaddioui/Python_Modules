import sys


def text_to_morse(argument):
    """Encodes a string into Morse Code."""
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
        ' ': '/'
    }
    is_valid = [False for c in argument if not c.isalnum() and not c.isspace()]
    if is_valid:
        raise AssertionError("the arguments are bad")
    else:
        morse_result = []
        for c in argument:
            c = c.upper()
            if c not in morse_code:
                raise AssertionError("the arguments are bad")
            morse_result.append(morse_code[c])
        print(" ".join(morse_result))


def main():
    """Validates the input arguments and invokes text_to_morse."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        argument = sys.argv[1]
        text_to_morse(argument)

    except AssertionError as error:
        print("AssertionError:", error)
        sys.exit(1)


if __name__ == "__main__":
    main()
