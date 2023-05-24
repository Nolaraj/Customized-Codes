from PIL import Image, ImageDraw
from statistics import mean


# -------------------------------------------Initialization ------------------------------------
curve = Image.open("curve.png")

size = width, height = curve.size
pixel = {}
total_pixels = width * height
multiplier = 1

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


# -------------------------------------------Initialization Ends ------------------------------------

# -------------------------------------------Pixel Check Frequency and Pixel Extractions -----------------------------------
if total_pixels>=500000:
    multiplier = int(total_pixels/1000000)
    print(multiplier)
for i in range(0, width, multiplier):
    for j in range(0, height, multiplier):
        co_ordintes = i, j
        getpixel = curve.getpixel(co_ordintes)
        kvalue = str(getpixel[0]) + str(getpixel[1]) + str(getpixel[2])
        try:
                a = pixel[kvalue]
                a += 1
                pixel[kvalue] = a
        except:
            pixel[kvalue] = 1


key_list = list(pixel.keys())
value_list = list(pixel.values())
rev_pixel = {}

for rkey in sorted(pixel, key = pixel.get, reverse=True):
    rev_pixel[rkey] = pixel[rkey]

key = key_extractor(3509, rev_pixel)
value_list.sort(reverse=True)
# -------------------------------------------Pixel Check Frequency and Pixel Extractions End -----------------------------------

# -------------------------------------------Pixel Concentration Checking -----------------------------------
line_coordinates = {}

width_interval = int(width/128)
height_interval = 2
for i in range(0, width, width_interval):
    y_coordinates = []

    for j in range(0, height, height_interval):
        co_ordintes = i, j
        pixel1 = curve.getpixel(co_ordintes)
        pixel1c = str(pixel1[0]) + str(pixel1[1]) + str(pixel1[2])
        if key_list[1] == pixel1c:
            y_coordinates.append(j)
    line_coordinates[i] = y_coordinates

print(line_coordinates)

line_coordinates_frequency = {}
for keys, values in line_coordinates.items():
    for value in values:
        try:
            a = line_coordinates_frequency[value]
            a += 1
            line_coordinates_frequency[value] = a
        except:
            line_coordinates_frequency[value] = 1
rev_line_coordinates_frequency = {}
for rkey in sorted(line_coordinates_frequency, key = line_coordinates_frequency.get, reverse=True):
    rev_line_coordinates_frequency[rkey] = line_coordinates_frequency[rkey]

line_coordinates_keys_list = list(rev_line_coordinates_frequency.keys())

line_coordinates_frequency_list = list(rev_line_coordinates_frequency.values())

maximum_pixel = max(line_coordinates_frequency_list)

#todo Before the commencement for the following line the image should be checked for the probable highest number of the pixels in certain line

number_maximum_pixel = frequency_from_list(maximum_pixel, line_coordinates_frequency_list)
co_ordinates_list_of_higher_pixels_in_line = []
for i in range(number_maximum_pixel):
    co_ordinates_list_of_higher_pixels_in_line.append(line_coordinates_keys_list[i])
appropriate_y_value = mean(co_ordinates_list_of_higher_pixels_in_line)

for value in line_coordinates_keys_list:
    if value is not range(appropriate_y_value - (number_maximum_pixel * height_interval), appropriate_y_value + (number_maximum_pixel * height_interval)):
        print("Coordinates Extraciton")
        #todo the operation of the coOrdinates extractions

# -------------------------------------------Pixel Concentration Checking End -----------------------------------


print(rev_line_coordinates_frequency)
print(line_coordinates_keys_list)
print(line_coordinates_frequency_list)
print(number_maximum_pixel ,"Hello")
print(appropriate_y_value)



