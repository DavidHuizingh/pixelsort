import random

from time import time
import concurrent.futures
from PIL import Image
from itertools import repeat
import os
from math import floor
import numpy as np


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
    y_res = int(size[1])
    #max_workers = os.cpu_count()
    #divisor = y_res / max_workers

    sublist_target = 20
    y_all = list([y for y in range(0, y_res)])

    y_sections = []
    for x in range(0, len(y_all), sublist_target):
        y_section = (y_all[x: x + sublist_target])
        y_sections.append(y_section)
    
    # take Y size and divide it into "lists"
    # pass Y sections into workers

    #image_data_array = np.array(image_data)
    #mask_data_array = np.array(mask_data)
    

    #with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        #future_to_index = dict((executor.submit(sort_row, y, ("PUT ARGS HERE")), y) for y in range(size[1]))
        
        future_to_index = {}          # key: future, value: index         
        for indx, y_section in enumerate(y_sections, 0):
            gross_test = [sort_row, y_section, intervals, size, mask_data, image_data, randomness, sorting_function]
            future = executor.submit(sort_row, y_section, intervals, size, mask_data, image_data, randomness, sorting_function)
            future_to_index[future] = indx, y_section

        for future in concurrent.futures.as_completed(future_to_index):
            indx, y_section = future_to_index[future]
            # y_section not used :)
            result = future.result()
            sorted_rows_dict[indx] = result
    
    #while concurrent.futures.ALL_COMPLETED
    print("Started Sorting Pixels (hopefully executors are done!!!")
    sorted_pixels = []
    for i in range(len(sorted_rows_dict.keys())):
        row_chunk = sorted_rows_dict[i]
        sorted_pixels.extend(row_chunk)
    
    t2 = time()
    print(f"Completed sort_image in {round(t2-t1, 3)} seconds")
    img_sorted = Image.fromarray(sorted_pixels)
    return img_sorted

def sort_row(y_section, intervals, size, mask_data, image_data, randomness, sorting_function):
    section_name = f"{y_section[0]}-{y_section[-1]}"
    print(f"Started working on section {section_name}")

    row_chunk = []
    for y in y_section:
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
        row_chunk.append(row)
    print(f"Completed work on {section_name}")
    return row_chunk

def sort_interval(interval, sorting_function):
    return [] if interval == [] else sorted(interval, key=sorting_function)
