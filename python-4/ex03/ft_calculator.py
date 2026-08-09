class calculator:
    """A class to perform vector operations (add, mul, sub, truediv)."""

    def __init__(self, list: list):
        """Initialize calculator with a list of numbers."""
        self.vector = list

    def __add__(self, object) -> None:
        """Add a scalar to each element in vector."""
        for index, i in enumerate(self.vector):
            self.vector[index] = i + object
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply each element in vector by a scalar."""
        for index, i in enumerate(self.vector):
            self.vector[index] = i * object
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a scalar from each element in vector."""
        for index, i in enumerate(self.vector):
            self.vector[index] = i - object
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide each element in vector by a scalar."""
        try:
            for index, i in enumerate(self.vector):
                if object == 0:
                    raise ZeroDivisionError("Division by zero not allowed.")
                self.vector[index] = i / object
            print(self.vector)
        except ZeroDivisionError as e:
            print("ZeroDivisionError:", e)
