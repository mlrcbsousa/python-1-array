from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the specified path and returns its RGB pixel data.

    Parameters
    ----------
    path : str
        The file path to the image.

    Returns
    -------
    np.ndarray
        The image data in RGB format as a NumPy array.

    Raises
    ------
    FileNotFoundError:
        If the image file does not exist at the specified path.
    """

    try:
        assert isinstance(path, str), "The path has to be a string"

        img = Image.open(path)
        data = np.array(img)

    except (FileNotFoundError, IOError, AttributeError, AssertionError) as e:
        print(f"Error: {e}")
        return

    return data
