from config import referencesFilepath # or complete file path

from time import sleep
from pygetwindow import getAllWindows
from pyautogui import (click, moveTo, scroll, screenshot, write, locate)

class Controller:


    def __init__(self):
        """
        DONE - setWindow()
        DONE - getWindows()
        DONE - takeScreenshot()

        DONE - wait(?duration)
        TODO - date(m, d, y)
        TODO - _findText(text)
        TODO - _findImage(image)
        TODO - find(asset<text/image>, ?confidence)
        DONE - scroll(direction, ?distance)
        DONE - mouse(asset<text/image>)
        DONE - click(?multiple)
        DONE - keyboard(message)
        """

        self.mouseX = 0
        self.mouseY = 0
        self.windowX = 0
        self.windowY = 0
        self.windowWidth = 0
        self.windowHeight = 0
        self.screenshot = None
        self.useGrayscale = True
        self.excludedWindows = ["", ".", "Settings"]

        self.defaultWaitDuration = 3
        self.defaultClickMultiple = 1
        self.defaultMouseDistance = 10
        self.defaultScrollDistance = 10
        self.defaultFindConfidence = 0.9
        self.defaultScreenshotName = "screenshot.png"


    def findText(self, text):
        """  """

        pass


    def findImage(self, image, confidence):
        """  """

        x = locate(

            needleImage = image,
            confidence = confidence,
            grayscale = self.useGrayscale,
            haystackImage = self.screenshot

        )
        print('findImage()', x) # remove


    def find(self, asset, confidence = None):
        """  """

        confidence = float(confidence) if confidence else self.defaultFindConfidence


    def setWindow(self, window):
        """  """

        x, y, w, h = window.split(' ')[:-1]

        self.windowX = int(x)
        self.windowY = int(y)
        self.windowWidth = int(w)
        self.windowHeight = int(h)


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

            imageFilename = self.defaultScreenshotName,
            region = (self.windowX, self.windowY, self.windowWidth, self.windowHeight)

        )


    def keyboard(self, message):
        """  """

        write(message = message)


    def wait(self, duration = None):
        """  """

        sleep(seconds = int(duration) if duration else self.defaultWaitDuration)


    def scroll(self, direction, distance = None):
        """  """

        try:

            clicks = {

                "up" : int(distance) if distance else self.defaultScrollDistance,
                "down" : -int(distance) if distance else -self.defaultScrollDistance

            }[direction]

            scroll(clicks = clicks)

        except KeyError: return False


    def click(self, multiple = None):
        """  """

        click(clicks = int(multiple) if multiple else self.defaultClickMultiple)


    def mouse(self, direction, distance = None):
        """  """

        try:

            distance = int(distance) if distance else self.defaultMouseDistance
            x, y = {

                "up" : (self.mouseX, (distance + self.mouseY)),
                "left" : ((self.mouseX - distance), self.mouseY),
                "down" : (self.mouseX, (self.mouseY - distance)),
                "right" : ((self.mouseX + distance), self.mouseY)

            }[direction]

            # drift?
            moveTo(x = x, y = y)

        except KeyError: return False




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