import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculate the BMI from lists of heights and weights.

    Parameters
    ----------
    height (list[int | float]): A list of heights in meters.
    weight (list[int | float]): A list of weights in kilograms.

    Returns
    -------
    list[int | float]: A list of BMI values.

    Raises
    ------
    AssertionError:
        If the lists are not the same size or contain non-numeric items.
    """

    assert height is not None and weight is not None, "Can not be None."

    h = np.array(height)
    w = np.array(weight)

    assert h.ndim == w.ndim == 1, "Lists must be 1D."
    assert h.size == w.size, "Lists must be the same length."

    v = np.concatenate((h, w))

    assert np.isin(v.dtype, [int, float]), "All values must be ints or floats."
    assert np.all(v > 0), "All values must be positive."

    return (w / (h ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determine if each BMI in the list exceeds a specified limit.

    Parameters
    ----------
    bmi (list[float]): A list of BMI values.
    limit (int): The threshold BMI value.

    Returns
    -------
    list[bool]:
        A list where each element is True if the BMI exceeds the limit,
        False otherwise.

    Raises
    ------
    AssertionError:
        If the BMI list contains non-numeric items or the limit is not a number
    """

    assert bmi is not None and limit is not None, "Can not be None."

    b = np.array(bmi)

    assert np.isin(b.dtype, [int, float]), "All values must be ints or floats."
    assert np.all(b > 0), "All values must be positive."
    assert limit > 0, "Limit must be positive."

    return (b > limit).tolist()
