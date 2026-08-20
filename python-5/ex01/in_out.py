"""Module for closure/generator sequence operations."""


def square(x: int | float) -> int | float:
    """Return the square of a number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return a number raised to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return an inner function that maintains state and applies function."""
    count = 0

    def inner() -> float:
        """Inner function to apply function and update the state."""
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count
    return inner
