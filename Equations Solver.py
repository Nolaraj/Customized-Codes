from PIL import Image, ImageDraw
import random

constants_a = 2 #int(input("Enter the Value of a____"))
constants_b = -2 #int(input("Enter the Value of b____"))
constants_c = 8 #int(input("Enter the Value of c____"))
constants_d = 11 #int(input("Enter the Value of d____"))
constants_e = 1 #int(input("Enter the Value of e____"))
image_width = 2000 # int(input("Enter the Width for the Image___"))
image_height =  2000 #int(input("Enter the Height for the Image___"))


random_colour1 = (random.randint(0, 100), random.randint(0, 50), random.randint(0, 50))
random_colour3 = (random.randint(0, 20), random.randint(200, 225), random.randint(50, 100))
random_colour2 = (random.randint(150, 200), random.randint(80, 100), random.randint(100, 150))
random_colour4 = (random.randint(200, 225), random.randint(200, 225), random.randint(200, 225))

equation_image = Image.new("RGB",(image_width, image_height), random_colour1)

for i in range(image_width):
    for j in range(int(image_height/2) - int(image_height/400), int(image_height/2) + int(image_height/400)):
        co_ordinates = i, j
        equation_image.putpixel(co_ordinates, random_colour2)


for i in range(image_height):
    for j in range(int(image_width/2) - int(image_width/400), int(image_width/2) + int(image_width/400)):
        co_ordinates = j, i
        equation_image.putpixel(co_ordinates, random_colour2)


x=0
y=0
x1, y1 = 0, 0
x2, y2 = 0, 0
y3 = 0
y4 = 0
while (x < int(image_width/2) and y < int(image_height/2)):
    if x == 0:
        y1 = y2 = int(image_height/2)
        x1 = x2 = int(image_width/2)
    line12 = x1, y1, x2, y2
    draw = ImageDraw.Draw(equation_image)
    draw.line(line12, fill=random_colour3, width=int(image_width/400))
    y = constants_e + constants_d * pow(x, 1) + constants_c * pow(x, 2) + constants_b * pow(x, 3) + constants_a * pow(x, 4)
    x += 1
    x1, y1 = x2, y2
    x2, y2 = x + int(image_width/2), y + int(image_height/2)


equation_image.show()