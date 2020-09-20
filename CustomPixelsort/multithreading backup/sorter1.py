import random

from time import time
import concurrent.futures

from itertools import repeat

### Modified from original

def sort_image(
        size,
        image_data,
        mask_data,
        intervals,
        randomness,
        sorting_function):

    t1 = time()
    sorted_pixels = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        row_sorted = executor.map(sort_row, [y for y in range(size[1])], repeat(intervals), repeat(size), repeat(mask_data), repeat(image_data), repeat(randomness), repeat(sorting_function))
        row_listed = list(row_sorted)
        sorted_pixels.append(row_listed)

    t2 = time()
    print(f"Completed sort_image in {round(t2-t1, 3)} seconds")


    return sorted_pixels

def sort_row(y, intervals, size, mask_data, image_data, randomness, sorting_function):
    
    print(f"Thread started for Y = {y}")
    row = []
    x_min = 0
    for x_max in intervals[y] + [size[0]]:
        interval = []
        for x in range(x_min, x_max):
            if mask_data[x, y]:
                interval.append(image_data[x, y])
        if random.random() < randomness / 100:
            row += interval
        else:
            row += sort_interval(interval, sorting_function)
        x_min = x_max
    print(f"Thread completed for Y = {y}")
    return row

def sort_interval(interval, sorting_function):
    return [] if interval == [] else sorted(interval, key=sorting_function)
