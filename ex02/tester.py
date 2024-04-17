from load_image import ft_load


def main():
    """Main function to test the ft_load function."""

    print("Valid file: ")
    print(ft_load("landscape.jpg"))
    print()

    print("Invalid file: ")
    print(ft_load("landscap.jpg"))
    print(ft_load(2))


if __name__ == "__main__":
    main()
