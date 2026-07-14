from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def display_axis (image: np.ndarray) -> None:
    """ Display the image array using matplotlib. """
    plt.imshow(image, cmap="grey")
    plt.show()

def zoom(old_shape: np.ndarray) -> np.ndarray:
    """ Slice and return a zoomed-in region of the image array. """
    new_shape = old_shape[100:500, 450:850, 0:1]
    return new_shape

def rotate (image :np.ndarray) :
    return image
    pass

def main ():
    try:
        image_as_array = ft_load("animal.jpeg")
        new_shape_image = zoom(image_as_array)
        print(f"New shape after slicing: {new_shape_image.shape} or {new_shape_image.shape[:2]}")
        print(new_shape_image)
        rotate(new_shape_image)
    except:
        print("error")

if __name__ == "__main__":
    main()