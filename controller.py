

from time import sleep
from pygetwindow import getAllWindows
from pyautogui import (click, moveTo, scroll, screenshot, write)

class Controller:


    def __init__(self):
        """
        - _findImage(image)
        - _findText(text)
        DONE - wait(?duration)
        - find(text/image)
        - date(m, d, y)
        DONE - scroll(?direction)
        - mouse(text/image)
        DONE - click(?multiple)
        - keyboard(message)
        DONE - setWindow()
        DONE - getWindows()
        DONE - takeScreenshot()
        """

        self.directionTop = 10
        self.directionLeft = 10
        self.directionRight = 10
        self.directionBottom = 10

        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.screenshot = None
        self.screenshotFilename = "screenshot.png"
        self.excludedWindows = ["", ".", "Settings"]


    def keyboard(self, message):
        """  """

        write(message = message)


    def wait(self, duration):
        """  """

        sleep(seconds = int(duration))


    def scroll(self, direction):
        """  """

        scroll(clicks = int(direction))


    def click(self, multiple):
        """  """

        click(clicks = int(multiple))


    def mouse(self):
        """  """

        # moveTo(x = x, y = y)
        pass


    def setWindow(self, window):
        """  """

        x, y, w, h = window.split(' ')[:-1]

        self.x = int(x)
        self.y = int(y)
        self.width = int(w)
        self.height = int(h)


    def getWindows(self):
        """  """

        windows = {}
        for c, w in enumerate(getAllWindows()):

            if (w.title not in self.excludedWindows):

                # if (existing) <
                # else (then new) <
                if (w.title in windows):

                    windows[w.title]["count"] += 1
                    continue

                else: windows[w.title] = {

                    "count" : 1,
                    "label" : w.title,
                    "value" : f"{w.left} {w.top} {w.width} {w.height} {c}"

                }

                # >

        return list(windows.values())


    def takeScreenshot(self):
        """  """

        self.screenshot = screenshot(

            imageFilename = self.screenshotFilename,
            region = (self.x, self.y, self.width, self.height)

        )




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