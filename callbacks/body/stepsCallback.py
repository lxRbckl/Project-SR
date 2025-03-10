from config import app
from dash.dependencies import (Input, Output, State)


class Steps:


   def __init__(self):
      """  """

      pass

















# from time import sleep
# import pyautogui
# import pytesseract
# from PIL import Image
#
#
# # Set path for tesseract if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
#
# def locate_and_click_text(target_text):
#    # Take a screenshot of the screen
#    screenshot = pyautogui.screenshot()
#
#    # Convert screenshot to grayscale
#    screenshot = screenshot.convert('L')
#
#    screenshot.show()
#
#    # Use pytesseract to detect text in the screenshot
#    text = pytesseract.image_to_data(
#       # lang='eng',
#       image = screenshot,
#       output_type=pytesseract.Output.DICT
#    )
#
#    print(text['text']) # remove
#    print(text['text'].count(target_text))
#
#
#    # indexFromName = text['text'].index(target_text)
#
#    # x = text['left'][indexFromName]
#    # y = text['top'][indexFromName]
#
#    # print('RESULT:', x, y) # remove
#
#
#    # pyautogui.move(x, y)
#
#
#    # while True:
#    #    print(pyautogui.position())
#    #    sleep(2)
#
#
#
#
#
# # Example usage
# locate_and_click_text('EXAMPLE')