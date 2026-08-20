import pygame
import numpy as np

pygame.init()

mx_width, mx_height = 64, 8

#ROWS, COLS = 8, 8
LED_SIZE = 40  # Size of each LED in pixels
LED_GAP = 6  # Space between LEDs
MARGIN = 20  # Border around the grid

# Window dimensions
WIDTH = mx_width * (LED_SIZE + LED_GAP) - LED_GAP + (2 * MARGIN)
HEIGHT = mx_height * (LED_SIZE + LED_GAP) - LED_GAP + (2 * MARGIN)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LED Matrix Simulator")

# Colors (RGB)
BG_COLOR = (20, 20, 20)
LED_OFF = (40, 0, 0)  # Dim dark red for off state
LED_ON = (255, 0, 0)  # Bright red for on state

# Initialize matrix state (0 = off, 1 = on)
matrix = [[0 for _ in range(mx_width)] for _ in range(mx_height)]

clock = pygame.time.Clock()
running = True
timer = 0

while running:
  screen.fill(BG_COLOR)

  # Handle window closing
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Update LED states every 200 milliseconds
  timer += clock.get_rawtime()
  clock.tick(30)
  if timer > 200:
    r = np.random.randint(0, ROWS - 1)
    c = np.random.randint(0, COLS - 1)
    matrix[r][c] = 1 - matrix[r][c]  # Toggle LED state
    timer = 0

  # Draw the LED matrix grid
  for row in range(mx_height):
    for col in range(mx_width):
      x = MARGIN + col * (LED_SIZE + LED_GAP)
      y = MARGIN + row * (LED_SIZE + LED_GAP)

      # Pick color based on state
      color = LED_ON if matrix[row][col] == 1 else LED_OFF

      # Draw circular LED
      center = (x + LED_SIZE // 2, y + LED_SIZE // 2)
      pygame.draw.circle(screen, color, center, LED_SIZE // 2)

  pygame.display.flip()

pygame.quit()