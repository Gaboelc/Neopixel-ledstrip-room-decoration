import board
from lights import strip

strip = strip(board.A1, 288, (1, 0, 2, 3))

red = (255, 0, 0, 0)
yellow = (255, 150, 0, 0)
green = (0, 255, 0, 0)
cyan = (0, 255, 255, 0)
blue = (0, 0, 255, 0)
purple = (180, 0, 255, 0)
white = (0, 255, 255, 255)
off = (0, 0, 0, 0)

while True:
    strip.color_chase(red, 0.0001, 2)
    strip.color_chase(yellow, 0.0001, 2)
    strip.color_chase(green, 0.0001, 2)
    strip.color_chase(cyan, 0.0001, 2)
    strip.color_chase(blue, 0.0001, 2)
    strip.color_chase(purple, 0.0001, 2)
