import time
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
from random import choice as random_choice


class strip:
    def __init__(self, pixel_pin, num_pixels, order):

        self.num_pixels = num_pixels

        self.strip = neopixel.NeoPixel(
            pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=order, bpp=4
        )
        
        self.pallete = [(255, 0, 0, 0), # Red,
                        (255, 150, 0, 0), #Yellow
                        (0, 255, 0, 0), #Green
                        (0, 255, 255, 0), #Cyan
                        (0, 0, 255, 0), #Blue
                        (180, 0, 255, 0), #Purple
                        (0, 255, 255, 255), #White
                        (0, 0, 0, 0) #Off
                        ]

    def color_chase(self, wait, delay):
        for color in self.pallete[:5]:
            for i in range(self.num_pixels):
                if i != self.num_pixels - 1:
                    self.strip[i] = color
                    time.sleep(wait)
                    self.strip.show()
                else:
                    time.sleep(delay)

    def color_chase_bounce(self, wait, iteration):
        i = 0
        for a in range(iteration):
            color1 = random_choice(self.pallete[:5])
            color2 = random_choice(self.pallete[:5])
            while i <= self.num_pixels - 2:
                self.strip[i] = color1
                self.strip.show()
                i += 1
                time.sleep(wait)
            while i >= 0:
                self.strip[i] = color2
                self.strip.show()
                i = i - 1
                time.sleep(wait)

    def strobe(self, wait=0.2):
        for color in self.pallete[:5]:
            self.strip.fill(color)
            self.strip.show()
            time.sleep(wait)
            
    def run(self):
        for i in range(self.num_pixels):
            self.strip[0::2] = self.pallete[4]
            # self.strip[i+1] = self.pallete[4]
            # self.strip[i+2] = self.pallete[4]
            # self.strip[i+3] = self.pallete[4]
            self.strip[i-1] = self.pallete[7]
            self.strip.show()
            time.sleep(0.01)
