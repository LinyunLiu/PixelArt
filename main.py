# Title: Pixel Art
# Developer: Linyun Liu
# Date: August 12nd, 2023

from Pixel import PixelArtConverter

image_path = 'mona_lisa.jpg'
output_path = 'new.jpeg'
INTENSITY = 50

converter = PixelArtConverter(image_path, INTENSITY)
converter.convert(output_path)
