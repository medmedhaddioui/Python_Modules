"""Module to define the callLimit decorator."""


def callLimit(limit: int):
    """Decorator to limit function calls."""
    count = 0

    def callLimiter(function):
        """Decorator that wraps the target function."""
        def limit_function(*args: any, **kwds: any):
            """Wrapper function that tracks and limits external calls."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            function(*args, **kwds)
            count += 1
        return limit_function
    return callLimiter
