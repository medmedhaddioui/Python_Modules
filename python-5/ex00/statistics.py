def mean(args: tuple) -> float:
    """Calculate the mean of a sequence of numbers."""
    return sum(args) / len(args)


def median(args: tuple) -> float:
    """Calculate the median of a sequence of numbers."""
    sorted_args = sorted(args)
    index = (len(args) - 1) // 2
    if len(args) % 2 == 0:
        return mean((sorted_args[index], sorted_args[index + 1]))
    return sorted_args[index]


def quartile(args: tuple) -> list:
    sorted_args = sorted(args)
    q1_position = len(args) // 4
    q3_position = len(args) * 3 // 4
    if len(args) % 4 == 0:
        q1 = (sorted_args[q1_position - 1] + sorted_args[q1_position]) / 2
        q3 = (sorted_args[q3_position - 1] + sorted_args[q3_position]) / 2
    else:
        q1 = sorted_args[q1_position]
        q3 = sorted_args[q3_position]
    return [float(q1), float(q3)]


def var(args: tuple) -> float:
    mean_value = mean(args)
    length = len(args)
    distance = 0
    distance_total = 0
    for arg in args:
        distance = arg - mean_value
        square_distance = distance ** 2
        distance_total += square_distance
    return float(distance_total / length)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculate mean, median, quartile, std, and var."""

    for a in args:
        if not isinstance(a, (int, float)):
            print('ERROR')
            return
    for operation in kwargs.values():
        if len(args) == 0:
            print('ERROR')
            continue
        if operation == "mean":
            print(f"mean : {mean(args)}")

        elif operation == "median":
            print(f"median : {median(args)}")

        elif operation == "quartile":
            print(f"quartile : {quartile(args)}")
        elif operation == "std":
            print(f"std: {var(args) ** 0.5}")
        elif operation == "var":
            print(f"var: {var(args)}")
