import numpy as np
import matplotlib.pyplot as plt


def display_axis(image: np.ndarray) -> None:
    """ Display the image array using matplotlib. """

    plt.imshow(image, cmap="grey")
    plt.show()


def ft_invert(array) -> np.ndarray:
    """ Invert the colors of an image. Allowed operators: =, +, -, * """

    new = array.copy()
    new[:, :, :] = 255 - new[:, :, :]
    display_axis(new)
    return new


def ft_red(array) -> np.ndarray:
    """ Keep only the red channel. Allowed operators: =, * """

    new = array.copy()
    new[:, :, 1:3] = new[:, :, 1:3] * 0
    display_axis(new)
    return new


def ft_green(array) -> np.ndarray:
    """ Keep only the green channel. Allowed operators: =, - """

    new = array.copy()
    new[:, :, 0] = new[:, :, 0] - new[:, :, 0]
    new[:, :, 2] = new[:, :, 2] - new[:, :, 2]
    display_axis(new)
    return new


def ft_blue(array) -> np.ndarray:
    """ Keep only the blue channel. Allowed operators: = """

    new = array.copy()
    new[:, :, 0:2] = 0
    display_axis(new)
    return new


def ft_grey(array) -> np.ndarray:
    """ Convert the image to greyscale. Allowed operators: =, / """

    new = array.copy()
    grey = new[:, :, :3].mean(axis=2)
    new[:, :, 0] = grey
    new[:, :, 1] = grey
    new[:, :, 2] = grey
    display_axis(new)
    return new
