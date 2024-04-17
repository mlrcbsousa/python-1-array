import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load
from PIL import Image

GRAYSCALE = [0.2989, 0.5870, 0.1140]


def zoom(img: np.ndarray) -> np.ndarray:
    """Zoom and display the image."""

    # [..., :3] used to remove the alpha channel if it exists
    # [..., np.newaxis] used to add new axis to the array
    sliced = img[100:500, 450:850]
    gray_2D = np.dot(sliced[..., :3], GRAYSCALE)
    gray_3D = gray_2D[..., np.newaxis]

    # Set the ellipsis threshold to 6, and floats as integers
    np.set_printoptions(
        threshold=6,
        formatter=dict(float=lambda x: f"{x:.0f}")
    )
    print(f"New shape after slicing: {gray_3D.shape} or {gray_2D.shape}")
    print(gray_3D[:1])

    plt.imshow(Image.fromarray(gray_2D))
    plt.axis('on')
    plt.show()

    return gray_2D


def main():
    """
    Main function that loads an image, slices it, converts it to grayscale,
    and displays the grayscale image.
    """

    img = ft_load("animal.jpeg")

    try:
        assert img is not None, "Image loading failed."

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    print(img[:1])

    try:
        zoom(img)

    except Exception:
        print("Image zooming failed.")


if __name__ == "__main__":
    main()
