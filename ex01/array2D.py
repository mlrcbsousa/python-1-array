import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D array and prints its shape before and after slicing.

    Parameters
    ----------
    family (list): A 2D list of numbers.
    start (int): The starting index for the slice.
    end (int): The ending index for the slice.

    Returns
    -------
    list: A list of lists representing the sliced array.

    Raises
    ------
    AssertionError:
        If the input is not a list of lists of numbers or indices are out of
        range.
    """

    try:
        assert isinstance(family, list), "Family must be a list."

        assert all(isinstance(row, list) for row in family), \
            "All elements must be lists."

        length = len(family[0])

        assert all(len(row) == length for row in family), \
            "All sub lists must have the same length."

        assert all(
            all(isinstance(num, (int, float)) for num in row) for row in family
            ), "All elements must be int or float."

        assert isinstance(start, int) and isinstance(end, int), \
            "Start and end have to be ints."

        np_array = np.array(family)

        assert np_array.ndim == 2, "Family must be a 2D list."

        assert start >= 0 and end <= np_array.shape[0], \
            "Slice indices are out of range."

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    print(f"My shape is : {np_array.shape}")

    sliced_array = np_array[start:end]

    print(f"My new shape is : {sliced_array.shape}")

    return sliced_array.tolist()
