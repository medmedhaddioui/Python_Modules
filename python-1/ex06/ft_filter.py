def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return [i for i in iterable if i]
    return [i for i in iterable if function(i)]


def main():
    """Test ft_filter function."""
    print("Testing ft_filter's output:")
    my_list = [1, 2, 3, 4, 5, 0, False, True, "hello", ""]

    # Test with None
    print("ft_filter(None, my_list):", ft_filter(None, my_list))
    print("filter(None, my_list)   :", list(filter(None, my_list)))

    # Test with function
    def is_even(x):
        return isinstance(x, int) and not isinstance(x, bool) and x % 2 == 0

    print("ft_filter(is_even, my_list):", ft_filter(is_even, my_list))
    print("filter(is_even, my_list)   :", list(filter(is_even, my_list)))

    # Test docstring
    print("\nChecking docstring:")
    match = ft_filter.__doc__ == filter.__doc__
    print("ft_filter docstring match built-in:", match)


if __name__ == "__main__":
    main()
