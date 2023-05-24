from PIL import Image
from statistics import mean

curve = Image.open("curve.png")

size = width, height = curve.size
total_pixels = width * height

x_check_interval = 30
y_check_interval = 30

rotation_interval = 4
x_check_rotation_interval = x_check_interval * 2
y_check_rotation_interval = x_check_interval * 2

strip_origin = 0
strip_width = int(width/50)
strip_interval = int(strip_width/10)
check_interval_across_strip = 10
check_interval_along_strip = 15

check_interval_across_strip_for_final_strip = 2
check_interval_along_strip_for_final_strip = 4

def key_extractor(value, dict):
    for keys, values in dict.items():
        if value == values:
            return keys
def frequency_from_list(value, list):
    number = 0
    for item in list:
        if value == item:
            number += 1
    return number



def pixel_extraction():
    pixel_dict = {}
    for x in range(0, width, x_check_interval):
        for y in range(0, height, y_check_interval):
            co_ordinates = x, y
            pixel_color = curve.getpixel(co_ordinates)
            pvalue = str(pixel_color[0]) + str(pixel_color[1]) + str(pixel_color[2])
            list_secondary = [x, pvalue]
            list_primary = []
            if pixel_dict.get(y) is None:
                list_primary = [list_secondary]
                pixel_dict[y] = list_primary
            else:
                list_primary = pixel_dict[y]
                list_primary.append(list_secondary)
                pixel_dict[y] = list_primary

    return pixel_dict
def pixel_count(pixel_dict):
    pixel_count = {}
    pixel_count_rev = {}
    for key, value in pixel_dict.items():
        for secondary_list in value:
            if pixel_count.get(secondary_list[1]) is None:
                pixel_count[secondary_list[1]] = 1
            else:
                pixel_count[secondary_list[1]] = pixel_count[secondary_list[1]] + 1

    for sorted_key in sorted(pixel_count, key=pixel_count.get, reverse=True):
        pixel_count_rev[sorted_key] = pixel_count[sorted_key]

    return pixel_count_rev
def pixel_range(pixel_count):
    bg_pixel = []
    point_pixel = []

    pixel_list = list(pixel_count.keys())
    bg_pixel.append(pixel_list[0])
    point_pixel.append(pixel_list[1])

    return bg_pixel, point_pixel
def photo_orientation(point_pixel):
    return 1000

    orient_dict = {}
    appropriate_angle = 0
    appropriate_pixel = 0
    appropriate_number_max = 0
    for rotation_angle in range(-45, 45, rotation_interval):
        rotated_curve = curve.rotate(rotation_angle)
        dict_y = {}
        for y in range(0, height, y_check_rotation_interval):
            pixel_number = {}
            pixel_number_rev = {}

            for x in range(0, width, x_check_rotation_interval):
                co_ordinates = x, y
                pixel_color = rotated_curve.getpixel(co_ordinates)
                pvalue = str(pixel_color[0]) + str(pixel_color[1]) + str(pixel_color[2])
                for item in point_pixel:
                    if item == pvalue:
                        if pixel_number.get(pvalue) is None:
                            pixel_number[pvalue] = 1
                        else:
                            pixel_number[pvalue] = pixel_number[pvalue] + 1
                            if appropriate_number_max <= pixel_number[pvalue]:
                                appropriate_angle = rotation_angle
                                appropriate_pixel = pvalue
                                appropriate_number_max = pixel_number[pvalue]


            for value in sorted(pixel_number, key=pixel_number.get, reverse=True):
                pixel_number_rev[value] = pixel_number[value]
            dict_y[y] = pixel_number_rev

        orient_dict[rotation_angle] = dict_y


    print(orient_dict)
    print(appropriate_angle)
    print(appropriate_pixel)
    print(appropriate_number_max)

def x_axis_extration(point_pixel):
    global strip_origin

    appropriate_pixel = 0
    appropriate_number_max = 0
    appropriate_strip_origin = 0

    while (strip_origin + strip_width) <= width:
        pixel_set = {}
        list_frequency = []
        for strip_x in range(strip_origin, strip_origin + strip_width,
                             check_interval_across_strip):  # x value of the Strip
            for strip_y in range(0, height, check_interval_along_strip):  # y vlaue of the Strip
                co_ordinates = strip_x, strip_y
                value = curve.getpixel(co_ordinates)
                pvalue = str(value[0]) + str(value[1]) + str(value[2])
                for item in point_pixel:
                    if pvalue == item:
                        if pixel_set.get(pvalue) is None:
                            pixel_set[pvalue] = 1
                        else:
                            pixel_set[pvalue] += 1
                    else:
                        pixel_set[pvalue] = 0
        strip_origin += strip_interval


        for key, value in pixel_set.items():
            if value is not None:
                list_frequency.append(value)
        maximum_number = max(list_frequency)
        maximum_pixel = key_extractor(maximum_number, pixel_set)
        if appropriate_number_max < maximum_number:
            appropriate_pixel = maximum_pixel
            appropriate_number_max = maximum_number
            appropriate_strip_origin = strip_origin


    pixel_number_in_x = {}  #Consists as: pixel_number_strip = {x = number of certain Pixel Value, ...}

    for strip_x in range(appropriate_strip_origin, appropriate_strip_origin + strip_width, check_interval_across_strip_for_final_strip):
        for strip_y in range(0, height, check_interval_along_strip_for_final_strip):
            co_ordinates = strip_x, strip_y
            value = curve.getpixel(co_ordinates)
            pvalue = str(value[0]) + str(value[1]) + str(value[2])

            if pvalue == appropriate_pixel:
                if pixel_number_in_x.get(strip_x) is None:
                        pixel_number_in_x[strip_x] = 1
                else:
                        pixel_number_in_x[strip_x] += 1

    for key, value in pixel_number_in_x.items():
        if value != 0:
            sum_total = key * value

    appropriate_y_value = int(sum_total/strip_width)

    return appropriate_y_value









pixel_dict = pixel_extraction()       # Returns the dictionary pixel_dict = {'y-axis value1' = [[x-axis value 1, pixel_color_value 1], ...], ...}
pixel_count = pixel_count(pixel_dict) # Consists the dictionary of the pixels in the photo in descending order of their occurance
bg_pixel, point_pixel = pixel_range(pixel_count) # Returns the list of appropriate pixel for background and Points of Curve
y_value = photo_orientation(point_pixel)
x_value = x_axis_extration(point_pixel)

