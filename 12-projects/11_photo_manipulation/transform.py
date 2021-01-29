from image import Image
import numpy as np


def make_image(image):
    x_pixels, y_pixels, num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    return new_img


def brighten(image, factor):
    # factor
    # < 1 darken , > 1 brighten
    new_img = make_image(image)

    # non-vectorized way
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_img.array[x, y, c] = image.array[x, y, c] * factor

    # vectorized way - is faster
    new_img.array = image.array * factor

    return new_img


def adjust_contrast(image, factor, mid=0.5):
    new_img = make_image(image)

    new_img.array = (image.array - mid) * factor + mid

    return new_img


def blur(image, kernel_size):
    x_pixels, y_pixels, num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    neighbor_range = kernel_size // 2

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0

                for x_i in range(max(0, x - neighbor_range), min(x_pixels - 1, x + neighbor_range) + 1):
                    for y_i in range(max(0, y - neighbor_range), min(y_pixels - 1, y + neighbor_range) + 1):
                        total += image.array[x_i, y_i, c]

                new_img.array[x, y, c] = total / (kernel_size ** 2)

    return new_img


def apply_kernel(image, kernel):
    x_pixels, y_pixels, num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    kernel_size = kernel.shape[0]
    neighbor_range = kernel_size // 2

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0

                for x_i in range(max(0, x - neighbor_range), min(x_pixels - 1, x + neighbor_range) + 1):
                    for y_i in range(max(0, y - neighbor_range), min(y_pixels - 1, y + neighbor_range) + 1):
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val

                new_img.array[x, y, c] = total

    return new_img


def combine_images(image1, image2):
    # image1 and image2 should be the same shape
    if image1.array.shape != image2.array.shape:
        return

    x_pixels, y_pixels, num_channels = image1.array.shape
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_img.array[x, y, c] = (image1.array[x, y, c] ** 2 + image2.array[x, y, c] ** 2) ** 0.5

    return new_img


if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    render = False

    # brighten
    if render:
        brightened_lake_im = brighten(lake, 1.7)
        brightened_lake_im.write_image('brightened_lake_im-vectorized.png')

        brightened_city_im = brighten(city, 5)
        brightened_city_im.write_image('brightened_city_im-vectorized.png')

    # darken
    if render:
        darkened_lake_im = brighten(lake, 0.3)
        darkened_lake_im.write_image('darkened_lake_im-vectorized.png')

        darkened_city_im = brighten(city, 0.8)
        darkened_city_im.write_image('darkened_city_im-vectorized.png')

    # contrast
    if render:
        contrast_lake_im = adjust_contrast(lake, 2, 0.3)
        contrast_lake_im.write_image('contrast_lake_im.png')

        contrast_city_im = adjust_contrast(city, 0.4, 0.6)
        contrast_city_im.write_image('contrast_city_im.png')

    # blur
    if render:
        blur_lake_im = blur(lake, 3)
        blur_lake_im.write_image('blur_lake_im.png')

        blur_city_im = blur(city, 15)
        blur_city_im.write_image('blur_city_im.png')

    # apply_kernel
    if  render:
        sobel_x_kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        sobel_y_kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

        sobel_lake_x = apply_kernel(lake, sobel_x_kernel)
        sobel_lake_x.write_image('sobel_lake_x.png')
        sobel_lake_y = apply_kernel(lake, sobel_y_kernel)
        sobel_lake_y.write_image('sobel_lake_y.png')

        sobel_city_x = apply_kernel(city, sobel_x_kernel)
        sobel_city_x.write_image('sobel_city_x.png')
        sobel_city_y = apply_kernel(city, sobel_y_kernel)
        sobel_city_y.write_image('sobel_city_y.png')

    # combine_images
    if render:
        sobel_x_kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        sobel_y_kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

        sobel_city_x = apply_kernel(city, sobel_x_kernel)
        sobel_city_y = apply_kernel(city, sobel_y_kernel)
        combine_images(sobel_city_x, sobel_city_x)
        sobel_xy = combine_images(sobel_city_x, sobel_city_x)
        sobel_xy.write_image('combined_city.png')

        sobel_lake_x = apply_kernel(lake, sobel_x_kernel)
        sobel_lake_y = apply_kernel(lake, sobel_y_kernel)
        sobel_xy = combine_images(sobel_lake_x, sobel_lake_x)
        sobel_xy.write_image('combined_lake.png')
