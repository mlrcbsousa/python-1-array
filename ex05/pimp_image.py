import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""

    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only the red channel of the image received."""

    result = array.copy()
    result[:, :, 1] = 0
    result[:, :, 2] = 0
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep only the green channel of the image received."""

    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 2] = 0
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep only the blue channel of the image received."""

    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Grayscale the image received."""

    result = array.copy()
    result[:, :, 0] = result[:, :, 1]
    result[:, :, 2] = result[:, :, 1]
    return result
