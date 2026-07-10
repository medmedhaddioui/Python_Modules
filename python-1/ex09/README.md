# ft_package

Simple example package for the exercise. Provides a single helper:

- `count_in_list(lst, target)` — returns how many times `target` appears in `lst`.

Usage:

```py
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```

Build and install locally:

```bash
python -m pip install --upgrade build
python -m build
python -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

License: MIT
