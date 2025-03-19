import pyautogui

from config import (tesseractCMD, referencesCompleteFilepath)

import pytesseract
from time import sleep
from pygetwindow import getAllWindows
from pyautogui import (

    click,
    write,
    moveTo,
    scroll,
    center,
    locateAll,
    screenshot,
    ImageNotFoundException

)


class Controller:


    def __init__(self):
        """
        DONE - setWindow()
        DONE - getWindows()
        DONE - takeScreenshot()
        DONE - wait(?duration)
        TODO - date(m, d, y)
        TODO - _findText(text, ?index)
        TODO - _findImage(image, ?index)
        TODO - find(asset<text/image>, ?index)
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

        self.defaultFindIndex = 0
        self.defaultWaitDuration = 3
        self.defaultClickMultiple = 1
        self.defaultMouseDistance = 10
        self.defaultScrollDistance = 10
        self.defaultFindConfidence = 0.85
        self.defaultScreenshotName = "screenshot.png"

        pytesseract.pytesseract.tesseract_cmd = tesseractCMD



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


    def findText(self, text, index, confidence):
        """  """

        try:

            data = pytesseract.image_to_data(

                lang = "eng",
                output_type = "dict",
                image = self.screenshot

            )

            results = []
            for e, (conf, message) in enumerate(zip(data["conf"], data["text"])):

                if ((conf >= confidence) and (text in message)):

                    results.append(center((

                        data["left"][e],
                        data["top"][e],
                        data["width"][e],
                        data["height"][e]

                    )))

                return results[index]

            else: return False

        except ValueError: return False


    def findImage(self, image, index, confidence):
        """  """

        try:

            results = list(locateAll(

                confidence = confidence,
                grayscale = self.useGrayscale,
                haystackImage = self.screenshot,
                needleImage = f"{referencesCompleteFilepath}/{image}"

            ))

            return center(results[index])

        except ImageNotFoundException: return False


    def find(self, asset, index = None, confidence = None):
        """  """

        index = int(index) if index else self.defaultFindIndex
        confidence = int(confidence) if confidence else self.defaultFindConfidence


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