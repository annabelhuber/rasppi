import pygame
import numpy as np
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import text, textsize
from luma.core.legacy.font import CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT, proportional
from datetime import date, datetime
import time

import date_time_messages as dt
import birthday_list 
import holidays


def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=mx_width // 32, block_orientation=-90, rotate=0, blocks_arranged_in_reverse_order=False)
    # mx_width, mx_height = 128, 8

    # device = pygame(width=mx_width, height=mx_height, rotate=0, mode="1", scale=8, transform="identity")

    print_str= dt.return_text(2026,10,31)

    if len(print_str) > 23:
        my_font = TINY_FONT
    else:
        my_font = SINCLAIR_FONT
    #msg_width = len(print_str*6)
    #virtual = viewport(device, width=msg_width + 64, height=8)

    try:
        while True:
            if len(print_str) < 32:
                with canvas(device) as draw:
                    #get dimensions of text
                    text_width, text_height = textsize(print_str, font=proportional(my_font))

                    #get center coords
                    x = (device.width - text_width) // 2
                    y = (device.height - text_height) // 2

                    text(draw,(x,y), print_str, fill="white", font=proportional(my_font))
                time.sleep(1)

            else:
                #get current time/date
                now = datetime.now()
                formatted_date = now.strftime("%Y, %m, %d")
                year=int(now.strftime("%Y"))
                month=int(now.strftime("%m"))
                day=int(now.strftime("%d"))

                #set holidays and birthday lists
                birthdays = birthday_list.get_birthdays()
                us_holidays = holidays.US(years=year)

                #split into 2 strings
                first_str = dt.birthday_return_str(birthdays,year,month,day)
                second_str = dt.holidays_return_str(us_holidays,year,month,day)

                #get start time and start by displaying first string
                start_time = time.time()
                show_first_half = True

                while True:
                    # 2. Check if 10 seconds have elapsed
                    current_time = time.time()

                    if current_time - start_time >= 10.0:
                        show_first_half = not show_first_half  # Toggle the boolean state
                        start_time = current_time              # Reset the baseline timer
            
                    # 3. Choose which half to print based on the toggle state
                    current_display_text = first_str if show_first_half else second_str

                    with canvas(device) as draw:
                        #center text
                        text_width, text_height = textsize(current_display_text, font=proportional(my_font))
                        x = (device.width - text_width) // 2
                        y = (device.height - text_height) // 2
                        #set font size based on string size
                        if len(current_display_text) > 23:
                            my_font = TINY_FONT
                        else:
                            my_font = SINCLAIR_FONT

                        # Render the current static slice at coordinates (0, 1)
                        text(draw, (x,y), current_display_text, fill="white", font=proportional(my_font))

                    # Keep a low sleep interval so the 10-second timer check is responsive
            
                    time.sleep(0.1)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()