import board
import neopixel_spi as neopixel


RING_SIZE = 12
pixels = neopixel.NeoPixel_SPI(board.SPI(), RING_SIZE)


def set_led(pos, color):
    """Set the color of a specific LED in the ring.

    Args:
        pos (int): Position of the LED (0 to RING_SIZE-1).
        color (tuple): Color as an (R, G, B) tuple.
    """

    pos = pos % RING_SIZE
    pixels[pos] = (color[0] << 16) | (color[1] << 8) | color[2]
    pixels.show()


def set_tail(pos:int, length:int, color, direction=1):
    """Set a tail of LEDs starting from a specific position.

    Args:
        pos (int): Starting position of the tail (0 to RING_SIZE-1).
        length (int): Length of the tail.
        color (tuple): Color as an (R, G, B)
    """

    
    for i in range(length):
        led_color = (color[0] // (2 ** i), color[1] // (2 ** i), color[2] // (2 ** i))
        led_pos = (pos - i * direction) % RING_SIZE
        pixels[led_pos] = (led_color[0] << 16) | (led_color[1] << 8) | led_color[2]

    led_pos = (pos - length * direction) % RING_SIZE
    pixels[led_pos] = 0x000000


    pixels.show()


def clear():
    """
    Clear all LEDs in the ring.
    """
    pixels.fill(0x000000)
    pixels.show()


