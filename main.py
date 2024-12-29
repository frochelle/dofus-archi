import time
import pytesseract
import pygame
from screenshot import Screenshot
from controller import Controller

# Settings
time.sleep(2)
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

# Init Controller object
controller = Controller('Otomai')

# Loop until archi is found
while True:
    # Init Screenshot object
    screenshot = Screenshot()

    # Search if there is an archi on image
    is_archi = screenshot.search_archi()

    # If archi found, warn user
    if is_archi:
        print('Archi found')
        break
    # Else move to next position if position successfully read
    elif screenshot.x and screenshot.y:
        controller.move(screenshot.x, screenshot.y)

    # Wait a second
    time.sleep(0.7)

# Alert user with shrek song
pygame.mixer.init()
pygame.mixer.music.load('shrek.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

