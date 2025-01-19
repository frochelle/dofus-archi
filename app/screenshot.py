import os
import cv2
import numpy as np
import pyautogui
import pytesseract
from settings import ROOT_PATH


class Screenshot:

    def __init__(self):
        screenshot = pyautogui.screenshot()
        self.image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
        self.coordinates_image = np.array(screenshot.crop((0, 75, 150, 110)))
        self.x, self.y = self.get_coordinates()
        self.archi = cv2.imread(os.path.join(ROOT_PATH, 'data', 'picto_archi.PNG'), cv2.IMREAD_GRAYSCALE)

    def get_coordinates(self):
        # Process image
        lower_bound = np.array([240, 240, 240], dtype="uint8")
        upper_bound = np.array([255, 255, 255], dtype="uint8")
        color_mask = cv2.inRange(self.coordinates_image, lower_bound, upper_bound)
        result = cv2.bitwise_and(self.coordinates_image, self.coordinates_image, mask=color_mask)
        coordinates_image = cv2.resize(result, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        # Extract text from processed image
        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789-,N'
        extracted_text = pytesseract.image_to_string(coordinates_image, config=custom_config)

        # Set coordinates as numbers
        coord_x, coord_y = None, None
        if extracted_text != '':
            coordinates = extracted_text.split(',')
            try:
                coord_x = int(coordinates[0])
                coord_y = int(coordinates[1].split('N')[0][:-1])
            except ValueError:
                print('Reading error...')

        return coord_x, coord_y

    def search_archi(self):
        # Perform template matching
        result = cv2.matchTemplate(self.image, self.archi, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        return max_val >= 0.7
