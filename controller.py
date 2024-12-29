import os
import keyboard
import pandas as pd


class Controller:

    def __init__(self, sheet):
        df = pd.read_excel(os.path.join(os.getcwd(), 'maps.xlsx'), sheet_name=sheet, index_col=0)
        self.map = df.replace({'↑': '5', '↓': '2', '→': '3', '←': '1'})
        self.previous_position = [None, None]

    def move(self, x, y):
        # If position has changed, press a new input
        if [x, y] != self.previous_position:
            key = self.map.loc[y, x]
            keyboard.press_and_release(key)
            print(x, y, key)
            self.previous_position = [x, y]
