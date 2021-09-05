import time
import neopixel

class strip:
    def __init__(self, pixel_pin, num_pixels, order):

        self.num_pixels = num_pixels

        self.strip = neopixel.NeoPixel(
            pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=order
        )

        red = (255, 0, 0, 0)
        yellow = (255, 150, 0, 0)
        green = (0, 255, 0, 0)
        cyan = (0, 255, 255, 0)
        blue = (0, 0, 255, 0)
        purple = (180, 0, 255, 0)
        white = (0, 255, 255, 255)
        off = (0, 0, 0, 0)

        self.colors = [red, yellow, green, cyan, blue, purple, white, off]

    def color_chase(self, wait, delay):
        for color in self.colors[:5]:
            for i in range(self.num_pixels):
                if i != self.num_pixels - 1:
                    self.strip[i] = color
                    time.sleep(wait)
                    self.strip.show()
                else:
                    time.sleep(delay)
