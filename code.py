import board
from lights import strip

strip = strip(board.A1, 288, (1, 0, 2, 3))

while True:
    #strip.color_chase(0.0001, 2)
    #strip.strobe()
    strip.color_chase_bounce(0.001, 5)
