from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def display_axis(image: np.ndarray) -> None:
    """ Display the image array using matplotlib. """

    plt.imshow(image, cmap="grey")
    plt.show()


def zoom(old_shape: np.ndarray) -> np.ndarray:
    """ Slice and return a zoomed-in region of the image array. """

    new_shape = old_shape[100:500, 450:850, 0:1]
    return new_shape


def rotate(image: np.ndarray) -> np.ndarray:
    """ Rotate the image 90 degrees by transposing rows and columns. """

    rows = image.shape[0]
    colums = image.shape[1]

    transposed = np.zeros((colums, rows), dtype=image.dtype)
    for i in range(rows):
        for j in range(colums):
            transposed[j][i] = image[i][j][0]

    return transposed


def main():
    """ Load image, zoom, rotate, and display it. """

    try:
        image_as_array = ft_load("animal.jpeg")
        zommed_image = zoom(image_as_array)
        print(
            f"The shape of image is: {zommed_image.shape}"
            f" or {zommed_image.shape[:2]}"
        )
        print(zommed_image)
        rotated_image = rotate(zommed_image)
        print(f"New shape after Transpose: {rotated_image.shape}")
        print(rotated_image)
        display_axis(rotated_image)

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
