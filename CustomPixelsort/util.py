from colorsys import rgb_to_hsv
import time

def dec_time(func):
    def func_wrap(*args, **kwargs):
        t_start = time.time()
        func_return = func(*args, **kwargs)
        t_finish = time.time()
        t_elapsed = t_finish - t_start

        print(f'''Function "{func.__name__}" completed in {t_elapsed}''')

        return func_return
    return func_wrap


def id_generator():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    return timestr


def lightness(pixel):
    # For backwards compatibility with python2
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[2] / 255.0


def hue(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[0] / 255.0


def saturation(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[1] / 255.0


def crop_to(image_to_crop, reference_image):
    """
    Crops image to the size of a reference image. This function assumes that the relevant image is located in the center
    and you want to crop away equal sizes on both the left and right as well on both the top and bottom.
    :param image_to_crop
    :param reference_image
    :return: image cropped to the size of the reference image
    """
    reference_size = reference_image.size
    current_size = image_to_crop.size
    dx = current_size[0] - reference_size[0]
    dy = current_size[1] - reference_size[1]
    left = dx / 2
    upper = dy / 2
    right = dx / 2 + reference_size[0]
    lower = dy / 2 + reference_size[1]
    return image_to_crop.crop(
        box=(
            int(left),
            int(upper),
            int(right),
            int(lower)))


@dec_time
def silly_test(number):

    new_number = number + 100
    return new_number


if __name__ == "__main__":
    
    test_results = silly_test(100)
    print(f"Final output: {test_results}")