import board
from lights import strip

strip = strip(board.A1, 288, (1, 0, 2, 3))

while True:
    #strip.color_chase(0.0001, 5)
    
    #strip.strobe(0.001)
    strip.color_chase_bounce(0.001, 20)
    #strip.run()
