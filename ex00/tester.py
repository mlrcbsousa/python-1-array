from give_bmi import give_bmi, apply_limit


def main():
    """Main function to test the BMI calculation and limit application."""

    try:
        print("Subject:")
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

    except Exception as e:
        print(f"Error: {e}")

    try:
        print("Negative:")
        height = [-2.71, 1.15]
        weight = [165.3, -38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

    except Exception as e:
        print(f"Error: {e}")

    try:
        print("Size:")
        height = [2.71, 1.15]
        weight = [165.3, 38.4, 2349]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

    except Exception as e:
        print(f"Error: {e}")

    try:
        print("Type:")
        height = [2.71, 1.15]
        weight = "string"
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

    except Exception as e:
        print(f"Error: {e}")

    try:
        print("None:")
        height = [2.71, 1.15]
        weight = None
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

    except Exception as e:
        print(f"Error: {e}")

    try:
        print("Element type:")
        height = [2.71, 1.15, 6.5]
        weight = [165.3, "sdf", 34]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

    except Exception as e:
        print(f"Error: {e}")

    try:
        print("Dimension:")
        height = [[2.71, 3], [1.15, 6]]
        weight = [[165.3, 34], [1.15, 6]]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

    except Exception as e:
        print(f"Error: {e}")

    try:
        print("Negative limit:")
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, -3))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
