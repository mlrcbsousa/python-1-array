from array2D import slice_me


def main():
    """
    Main function to test the slicing on a predefined 2D list.
    """

    print("Subject:")
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    print("Family type:")
    family = "hi"
    print(slice_me(family, 0, 2))

    print("Dimensions:")
    family = [1.80, 78.4, 33]
    print(slice_me(family, 0, 2))

    print("Element dimensions:")
    family = [[1.80, 78.4], [[19, 23], [123, 33]], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))

    print("Element shape:")
    family = [[1.80, 78.4], [34, 4.3, 3.5], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))

    print("Invalid args:")
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 's'))
    print(slice_me(family, "sldkf", 2))


if __name__ == "__main__":
    main()
