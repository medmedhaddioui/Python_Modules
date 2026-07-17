from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def display_axis(image: np.ndarray) -> None:
    """ Display the image array using matplotlib. """
    plt.imshow(image, cmap="gray")
    plt.show()


def zoom(old_shape: np.ndarray) -> np.ndarray:
    """ Slice and return a zoomed-in region of the image array. """
    new_shape = old_shape[100:500, 450:850, 0:1]
    return new_shape


def main():
    """ Load, zoom, and display the animal image. """
    try:
        image_as_array = ft_load("animal.jpeg")
        print(image_as_array)
        new_shape_image = zoom(image_as_array)
        print(f"New shape after slicing: {new_shape_image.shape} "
              f"or {new_shape_image.shape[:2]}")
        print(new_shape_image)
        display_axis(new_shape_image)

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
