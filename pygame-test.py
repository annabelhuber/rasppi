import pygame
import numpy as np
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.emulator.device import pygame
from luma.core.legacy import text
from luma.core.legacy.font import CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT, proportional
import time

import dateTime as dt
import birthday_list 

birthdays = birthday_list.get_birthdays()

#pygame.init()


def main():
    mx_width, mx_height = 128, 8

    device = pygame(width=mx_width, height=mx_height, rotate=0, mode="1", scale=8, transform="identity")

    print_str= dt.return_text(2026,1,25)
    if len(print_str) > 25:
        my_font = TINY_FONT
    else:
        my_font = SINCLAIR_FONT
    #msg_width = len(print_str*6)
    #virtual = viewport(device, width=msg_width + 64, height=8)

    try:
        while True:
                # 2. Use the canvas context manager to draw frames
            with canvas(device) as draw:
                    # Clear the background
                #draw.rectangle(device.bounding_box, fill="black")
                    
                    # Draw a test rectangle boundary
                #draw.rectangle((5, 5, 58, 58), outline="blue")
                #print_str= dt.return_text(2026,8,20)    
                    # Draw test text
                draw.rectangle(device.bounding_box, fill="black")
                text(draw,(0, 0), print_str, fill="white", font=proportional(my_font))
                #draw.text((18, 36), "MATRIX", fill="green")

                # 3. Regulate the frame rate
            time.sleep(0.1)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
# #ROWS, COLS = 8, 8
# LED_SIZE = 40  # Size of each LED in pixels
# LED_GAP = 6  # Space between LEDs
# MARGIN = 20  # Border around the grid

# # Window dimensions
# WIDTH = mx_width * (LED_SIZE + LED_GAP) - LED_GAP + (2 * MARGIN)
# HEIGHT = mx_height * (LED_SIZE + LED_GAP) - LED_GAP + (2 * MARGIN)
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("LED Matrix Simulator")

# # Colors (RGB)
# BG_COLOR = (20, 20, 20)
# LED_OFF = (40, 0, 0)  # Dim dark red for off state
# LED_ON = (255, 0, 0)  # Bright red for on state

# # Initialize matrix state (0 = off, 1 = on)
# matrix = [[0 for _ in range(mx_width)] for _ in range(mx_height)]

# clock = pygame.time.Clock()
# running = True
# timer = 0

# while running:
#   screen.fill(BG_COLOR)

#   # Handle window closing
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       running = False

#   # Update LED states every 200 milliseconds
#   timer += clock.get_rawtime()
#   clock.tick(30)
#   if timer > 200:
#     r = np.random.randint(0, mx_height - 1)
#     c = np.random.randint(0, mx_width - 1)
#     matrix[r][c] = 1 - matrix[r][c]  # Toggle LED state
#     timer = 0

#   # Draw the LED matrix grid
#   for row in range(mx_height):
#     for col in range(mx_width):
#       x = MARGIN + col * (LED_SIZE + LED_GAP)
#       y = MARGIN + row * (LED_SIZE + LED_GAP)

#       # Pick color based on state
#       color = LED_ON if matrix[row][col] == 1 else LED_OFF

#       # Draw circular LED
#       center = (x + LED_SIZE // 2, y + LED_SIZE // 2)
#       pygame.draw.circle(screen, color, center, LED_SIZE // 2)

#   pygame.display.flip()

# pygame.quit()