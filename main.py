# Title: Pixel Art
# Developer: Linyun Liu
# Date: August 12nd, 2023

from PIL import Image

image = Image.open('david.jpg')
pixels = image.load()
width, height = image.size
intensity = 60
W = width // intensity
H = height // intensity
data = []
new_data = []
img = Image.new('RGB', (W*intensity, H*intensity))


# Read a NxN square size of pixels from the image
# And add the data to the array
def read(x_start, y_start):
    cache = []
    y_end = y_start + intensity
    x_end = x_start + intensity
    for y in range(y_start, y_end):
        for x in range(x_start, x_end):
            cache.append(pixels[x, y])
    data.append(cache)


def read_all():
    print("reading image...")
    for y in range(H):
        for x in range(W):
            read(x*intensity, y*intensity)


def calculate():
    print("converting pixels...")
    for i in range(len(data)):
        square = data[i]
        red = green = blue = 0
        for p in square:
            red = red + p[0]
            green = green + p[1]
            blue = blue + p[2]
        new_val = (red//len(square), green//len(square), blue//len(square))
        new_data.append(new_val)


def put(x_start, y_start, rgb):
    y_end = y_start + intensity
    x_end = x_start + intensity
    for y in range(y_start, y_end):
        for x in range(x_start, x_end):
            img.putpixel((x, y), rgb)


def put_all():
    print("generating new image...")
    index = 0
    for y in range(H):
        for x in range(W):
            put(x*intensity, y*intensity, new_data[index])
            index = index+1


read_all()
calculate()
put_all()
img.save('new.jpeg')

