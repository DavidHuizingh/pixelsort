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
    sorted_rows_dict = {}

#ex = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        #for y in range(size[1]):

        future_to_url = dict((executor.submit(sort_row, y, ("PUT ARGS HERE")), y) for y in range(size[1]))
                            
        for future in concurrent.futures.as_completed(future_to_url):
            indx = future_to_url[future]
            sorted_rows_dict[indx] = future.result()

    sorted_pixels = []
    for i in range(len(sorted_rows_dict.keys())):
        row = sorted_rows_dict[i]
        sorted_pixels.append(row)
    
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
