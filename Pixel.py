from PIL import Image


class PixelArtConverter:
    def __init__(self, path, intensity):
        self.image = Image.open(path)
        self.pixels = self.image.load()
        self.width, self.height = self.image.size
        self.intensity = intensity
        self.W = self.width // self.intensity
        self.H = self.height // self.intensity
        self.data = []
        self.new_data = []
        self.new_image = Image.new('RGB', (self.W * self.intensity, self.H * self.intensity))

    def read(self, x_start, y_start):
        cache = []
        y_end = y_start + self.intensity
        x_end = x_start + self.intensity
        for y in range(y_start, y_end):
            for x in range(x_start, x_end):
                cache.append(self.pixels[x, y])
        self.data.append(cache)

    def read_all(self):
        for y in range(self.H):
            for x in range(self.W):
                self.read(x * self.intensity, y * self.intensity)

    def calculate(self):
        for i in range(len(self.data)):
            square = self.data[i]
            red = green = blue = 0
            for p in square:
                red += p[0]
                green += p[1]
                blue += p[2]
            new_val = (red // len(square), green // len(square), blue // len(square))
            self.new_data.append(new_val)

    def put(self, x_start, y_start, rgb):
        y_end = y_start + self.intensity
        x_end = x_start + self.intensity
        for y in range(y_start, y_end):
            for x in range(x_start, x_end):
                self.new_image.putpixel((x, y), rgb)

    def put_all(self):
        index = 0
        for y in range(self.H):
            for x in range(self.W):
                self.put(x * self.intensity, y * self.intensity, self.new_data[index])
                index += 1

    def convert(self, path):
        print("converting...")
        self.read_all()
        self.calculate()
        self.put_all()
        self.new_image.save(path)
