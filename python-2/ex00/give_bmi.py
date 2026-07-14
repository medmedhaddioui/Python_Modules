def validate_numeric_list(lst: list[int | float], name: str) -> None:
    """Ensure `lst` is a list of ints or floats."""
    if not isinstance(lst, list):
        raise TypeError(f"{name} must be a list")
    for value in lst:
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must contain only int or float")


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Compute BMIs from height (m) and weight (kg)."""
    validate_numeric_list(height, "height")
    validate_numeric_list(weight, "weight")
    if len(height) != len(weight):
        raise ValueError("height and weight must be the same size")

    return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return booleans indicating BMI > limit."""
    validate_numeric_list(bmi, "bmi")
    if not isinstance(limit, (int, float)):
        raise TypeError("limit must be an int or float")

    return [value > limit for value in bmi]
