from PIL import Image, ImageDraw
import random
import os
image_width = int(input("Enter the Width for the Image___"))
image_height = int(input("Enter the Height for the Image___"))
power = float(input("Enter the Power for the variable__"))

random_colour1 = (random.randint(0, 100), random.randint(0, 50), random.randint(0, 50))
random_colour3 = (random.randint(0, 20), random.randint(200, 225), random.randint(50, 100))
random_colour2 = (random.randint(150, 200), random.randint(80, 100), random.randint(100, 150))
random_colour4 = (random.randint(200, 225), random.randint(200, 225), random.randint(200, 225))


foto = Image.new("RGB", (image_width, image_height), random_colour1)

for i in range(image_height):
    for j in range(int(image_width/2 - 5), int(image_width/2 + 5)):
        co_ordintates = j, i
        foto.putpixel(co_ordintates, random_colour2)

for i in range(image_width):
    for j in range(int(image_height/2 - 5), int(image_height/2 + 5)):
        co_ordintates = i, j
        foto.putpixel(co_ordintates, random_colour2)

x=0
y=0
x1, y1 = 0, 0
x2, y2 = 0, 0
y3 = 0
y4 = 0

while (x<image_width and y<image_height):
    if y == 0:
        y1 = y2 = y3 = y4 = int(image_height/2)

    position12 = x1, y1, x2, y2
    foto1 = ImageDraw.Draw(foto)
    foto1.line(position12, fill=random_colour3, width=5)


    position13 = x1, y3, x2, y4
    foto1 = ImageDraw.Draw(foto)
    foto1.line(position13, fill=random_colour3, width=5)

    x = pow(y, power)
    y += 1
    x1, y1 = x2, y2
    x2, y2 = x, y + int(image_height/2)
    y3 = y4
    y4 = int(image_height/2) - y

x = 0
y = 0
x1, y1 = 0, 0
x2, y2 = 0, 0
x3 = 0
x4 = 0

while (x<image_width and y<image_height):
    if x == 0:
        x1 = x2 = x3 = x4 = int(image_height/2)

    position12 = x1, y1, x2, y2
    foto1 = ImageDraw.Draw(foto)
    foto1.line(position12, fill=random_colour3, width=5)

    position13 = x3, y1, x4, y2
    foto1 = ImageDraw.Draw(foto)
    foto1.line(position13, fill=random_colour3, width=5)

    y = pow(x, power)
    x += 1
    x1, y1 = x2, y2
    x2, y2 = x + int(image_width/2), y
    x3 = x4
    x4 = int(image_width/2) - x


ImageDraw.floodfill(foto, (int(image_width/200), int(image_height/2) - int(image_height/500)), random_colour4)

foto.show()
