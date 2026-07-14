import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """ Load an image from `path` and return it as a NumPy array. """
    try:
        assert isinstance(path, str) and len(path) > 0, \
            "The path must be a string."
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        image = Image.open(path)
        image_as_array = np.array(image)
        print(f"The shape of image is: {image_as_array.shape}")
        return image_as_array

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
