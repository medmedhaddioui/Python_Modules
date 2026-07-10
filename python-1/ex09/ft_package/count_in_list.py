def count_in_list(lst: list, target) -> int:
    found_count = [True for c in lst if c is target]
    result = len(found_count)
    return result

