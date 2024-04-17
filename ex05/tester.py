from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


def display_images(images, titles):
    """Display the images in a 2 by 3 display with their titles."""

    plt.figure(figsize=(18, 12))

    for i, (img, title) in enumerate(zip(images, titles), 1):
        plt.subplot(2, 3, i)
        plt.imshow(img)
        plt.title(
            f"Figure VIII.{i}: {title}",
            pad=10,
            fontdict={'font': 'Times New Roman', 'fontsize': 16}
        )
        plt.axis('off')

    plt.tight_layout(pad=3.0)
    plt.show()


def main():
    """Main function to test the image manipulation functions."""

    img = ft_load("landscape.jpg")

    try:
        assert img is not None
    except AssertionError:
        print("Image loading failed.")
        return

    print(f"The shape of image is: {img.shape}")
    print(img[:1])
    print('   ...')

    try:
        images = [
            img,
            ft_invert(img),
            ft_red(img),
            ft_green(img),
            ft_blue(img),
            ft_grey(img)
        ]
        titles = ["Original", "Invert", "Red", "Green", "Blue", "Grey"]
        display_images(images, titles)

    except Exception as e:
        print(f"Image processing failed: {e}")
        return

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
