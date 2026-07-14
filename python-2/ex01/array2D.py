import numpy as np


def validate_list(family: list) -> None:
    """Ensure all rows in family have the same length."""
    if not family:
        raise ValueError("lists are not the same size")
    first_row_len = len(family[0])
    for row in family:
        if len(row) != first_row_len:
            raise ValueError("lists are not the same size")


def slice_me(family: list, start: int, end: int) -> list:
    """Return a slice of family from start to end, with shape info."""
    try:
        if not isinstance(family, list):
            raise TypeError("family must be a list type")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("start or end must be integer")
        validate_list(family)
        if not all(isinstance(row, list) for row in family):
            raise TypeError("All rows in family must be lists")

        arr = np.array(family)
        print(f"My shape is: ({arr.shape})")
        new_shape = arr[start:end]
        print(f"My new shape is : ({new_shape.shape})")
        return new_shape.tolist()

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
