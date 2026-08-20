import pygame
import numpy as np
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.emulator.device import pygame
from luma.core.legacy import text, textsize
from luma.core.legacy.font import CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT, proportional
from datetime import date, datetime
from PIL import Image, ImageDraw
import time

import date_time_messages as dt
import birthday_list 
import holidays

def build_image(print_str):
    #print_str= dt.return_text()
    #split the phrase into 2
    midpoint = len(print_str) // 2
    space_indices = [i for i, char in enumerate(print_str) if char == " "]

    if space_indices:
        closest_space = min(space_indices, key=lambda x: abs(x - midpoint))

        print_str1 = print_str[:closest_space]
        print_str2 = print_str[closest_space + 1:]

    if len(print_str1) > 11:
        my_font = TINY_FONT
    elif len(print_str2) > 11:
        my_font = TINY_FONT
    else:
        my_font = SINCLAIR_FONT
    
    img = Image.new("1", (64,16))
    draw = ImageDraw.Draw(img)
    #get dimensions of text
    text_width1, text_height1 = textsize(print_str1, font=proportional(my_font))
    text_width2, text_height2 = textsize(print_str2, font=proportional(my_font))
    #get center coords
    x1 = (64/2 - text_width1) // 2
    y1 = (8/2 - text_height1) // 2

    x2 = (64+64/2 - text_width2) // 2
    y2 = (8/2 - text_height2) // 2

    text(draw,(0,0), print_str1, fill="white", font=proportional(my_font))
    text(draw,(0,8), print_str2, fill="white", font=proportional(my_font))

    return img

def map_to_chain(image):
    raw = Image.new("1", (128,8))

    board1 = image.crop((0,0,32,8))
    raw.paste(board1, (0,0))

    board2 - image.crop((32,0,64,8))
    raw.paste(board2, (32,0))

    board3 = image.crop((32,8,64,16)).rotate(180)
    raw.paste(board3, (64,0))

    board4 = image.crop((0,8,32,16)).rotate(180)
    raw.paste(board4, (96,0))

    return raw

def simulate_image(print_str, scale=10):
    device = pygame(
        width=64,
        height=16,
        rotate=0,
        mode="1",
        scale=scale,
        transform="identity",
    )
 
    logical = build_image(print_str)
    device.display(logical)
 
    import time
    time.sleep(10)

def run_on_hardware(print_str, block_orientation=-90, blocks_arranged_in_reverse_order=False):
    from luma.led_matrix.device import max7219
    from luma.core.interface.serial import spi, noop
 
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(
        serial,
        cascaded=16,  # 4 boards x 4 modules each
        block_orientation=block_orientation,
        rotate=0,
        blocks_arranged_in_reverse_order=blocks_arranged_in_reverse_order,
    )
 
    logical = build_logical_image(print_str)
    raw = remap_to_chain(logical)
    device.display(raw)


# def main():
#     mx_width, mx_height = 128, 8

#     device = pygame(width=mx_width, height=mx_height, rotate=0, mode="1", scale=8, transform="identity")
#     #device_bottom = pygame(width=mx_width, height=mx_height, rotate=0, mode="1", scale=8, transform="identity")

#     print_str= dt.return_text()
#     #split the phrase into 2
#     midpoint = len(print_str) // 2
#     space_indices = [i for i, char in enumerate(print_str) if char == " "]

#     if space_indices:
#         closest_space = min(space_indices, key=lambda x: abs(x - midpoint))

#         print_str1 = print_str[:closest_space]
#         print_str2 = print_str[closest_space + 1:]

#     if len(print_str) > 23:
#         my_font = TINY_FONT
#     else:
#         my_font = SINCLAIR_FONT

#     try:
#         while True:
#             if len(print_str) < 32:
#                 with canvas(device) as draw:
#                     #get dimensions of text
#                     text_width1, text_height1 = textsize(print_str1, font=proportional(my_font))
#                     text_width2, text_height2 = textsize(print_str2, font=proportional(my_font))
#                     #get center coords
#                     x1 = (device.width/2 - text_width1) // 2
#                     y1 = (device.height/2 - text_height1) // 2

#                     x2 = (device.width/2 - text_width2) // 2
#                     y2 = (device.height/2 - text_height2) // 2

#                     text(draw,(x1,y1), print_str1, fill="white", font=proportional(my_font))
#                     text(draw,(x2,y2), print_str2, fill="white", font=proportional(my_font), rotate=2)

#                 time.sleep(1)

#             else:
#                 #get current time/date
#                 now = datetime.now()
#                 formatted_date = now.strftime("%Y, %m, %d")
#                 year=int(now.strftime("%Y"))
#                 month=int(now.strftime("%m"))
#                 day=int(now.strftime("%d"))

#                 #set holidays and birthday lists
#                 birthdays = birthday_list.get_birthdays()
#                 us_holidays = holidays.US(years=year)

#                 #split into 2 strings
#                 first_str = dt.birthday_return_str(birthdays,year,month,day)
#                 second_str = dt.holidays_return_str(us_holidays,year,month,day)

#                 #get start time and start by displaying first string
#                 start_time = time.time()
#                 show_first_half = True

#                 while True:
#                     # 2. Check if 10 seconds have elapsed
#                     current_time = time.time()

#                     if current_time - start_time >= 10.0:
#                         show_first_half = not show_first_half  # Toggle the boolean state
#                         start_time = current_time              # Reset the baseline timer
            
#                     # 3. Choose which half to print based on the toggle state
#                     current_display_text = first_str if show_first_half else second_str

#                     with canvas(device) as draw:
#                         #center text
#                         text_width, text_height = textsize(current_display_text, font=proportional(my_font))
#                         x = (device.width - text_width) // 2
#                         y = (device.height - text_height) // 2
#                         #set font size based on string size
#                         if len(current_display_text) > 23:
#                             my_font = TINY_FONT
#                         else:
#                             my_font = SINCLAIR_FONT

#                         # Render the current static slice at coordinates (0, 1)
#                         text(draw, (x,y), current_display_text, fill="white", font=proportional(my_font))

#                     # Keep a low sleep interval so the 10-second timer check is responsive
            
#                     time.sleep(0.1)

#     except KeyboardInterrupt:
#         pass


if __name__ == "__main__":
    line1 = "It's Annabel's 25th B-day!"

    simulate_image(line1)

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