
import board
import neopixel_spi as neopixel
import time


pixels = neopixel.NeoPixel_SPI(board.SPI(), 12)


pixels.fill(0x010101)
time.sleep(1)


pixels[0] = 0x00ff00
pixels.show()
time.sleep(1)

pixels[0] = 0x000000
pixels[1] = 0x00ff00
pixels.show()


time.sleep(5)
pixels.fill(0x000000)




