def ft_tqdm(lst: range) -> None:
    """Yields items from a range while displaying a terminal progress bar."""
    total = len(lst)
    bar_length = 55
    for i, item in enumerate(lst, 1):
        progress = int((i / total) * 100)
        filled = int(bar_length * i / total)
        bar = '=' * filled + '>' + ' ' * (bar_length - filled)
        print(f"\r{progress}%|{bar}| {i}/{total}", end="", flush=True)
        yield item
    print()
