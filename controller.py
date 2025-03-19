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
        DONE - _findText(text, ?index)
        DONE - _findImage(image, ?index)
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
        self.defaultImageFormats = [".png", ".jpg", ".jpeg"]

        pytesseract.pytesseract.tesseract_cmd = tesseractCMD

        self.errorWaitDuration = "Unable to wait. Is duration set correctly?"
        self.errorFindIndex = "Unable to convert index. Is index set correctly?"
        self.errorClickMultiple = "Could not click. Consider adjusting multiple."
        self.errorImageDNE = "Image does not exist in folder. Has reference been added?"
        self.errorMouseDistance = "Unable to convert distance. Is distance set correctly?"
        self.errorFindConfidence = "Unable to convert confidence. Is confidence set correctly?"
        self.errorTextNotFound = "Could not find text in window. Consider adjusting confidence."
        self.errorImageNotFound = "Could not find image in window. Consider adjusting confidence."
        self.errorMouseDirection = "Mouse direction does not exist. Consider adjusting direction."
        self.errorScrollDirection = "Scroll direction does not exist. Consider adjusting direction."


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


    def _findText(self, text, confidence):
        """  """

        # try:

        data = pytesseract.image_to_data(

            lang = "eng",
            output_type = "dict",
            image = self.screenshot

        )

        results = []
        for e, (conf, content) in enumerate(zip(data["conf"], data["text"])):

            if ((conf >= confidence) and (text in content)):

                results.append((

                    data["left"][e],
                    data["top"][e],
                    data["width"][e],
                    data["height"][e]

                ))

        # if (found) <
        # else (then missing) <
        if (len(results) > 0): return results
        else: return self.errorTextNotFound

        # >

        # except ValueError: return self.errorTextNotFound


    def _findImage(self, image, confidence):
        """  """

        try:

            results = list(locateAll(

                confidence = confidence,
                grayscale = self.useGrayscale,
                haystackImage = self.screenshot,
                needleImage = f"{referencesCompleteFilepath}/{image}"

            ))

            return results

        except IOError: return self.errorImageDNE
        except ImageNotFoundException: return self.errorImageNotFound


    def find(self, asset, index = None, confidence = None):
        """  """

        try: index = int(index) if index else self.defaultFindIndex
        except ValueError: return self.errorFindIndex
        try: confidence = int(confidence) if confidence else self.defaultFindConfidence
        except ValueError: return self.errorFindConfidence

        # if (image) <
        # else (then text) <
        for f in self.defaultImageFormats:

            if (f in asset):

                results = self._findImage(image = asset, confidence = confidence)
                break

        else: results = self._findText(text = asset, confidence = confidence)

        # >

        try:

            # if (failure) <
            # if (success) <
            if (isinstance(results, str)): return results
            if (isinstance(results, list)): return results[index]

            # >

        except IndexError: return self.errorFindIndex


    def keyboard(self, message):
        """  """

        write(message = message)


    def wait(self, duration = None):
        """  """

        try: sleep(seconds = int(duration) if duration else self.defaultWaitDuration)
        except ValueError: return self.errorWaitDuration


    def scroll(self, direction, distance = None):
        """  """

        try:

            clicks = {

                "up" : int(distance) if distance else self.defaultScrollDistance,
                "down" : -int(distance) if distance else -self.defaultScrollDistance

            }[direction]

            scroll(clicks = clicks)

        except KeyError: return self.errorScrollDirection


    def click(self, multiple = None):
        """  """

        try: click(clicks = int(multiple) if multiple else self.defaultClickMultiple)
        except ValueError: return self.errorClickMultiple


    def mouse(self, direction, distance = None):
        """  """

        try:

            try: distance = int(distance) if distance else self.defaultMouseDistance
            except ValueError: return self.errorMouseDistance
            x, y = {

                "up" : (self.mouseX, (distance + self.mouseY)),
                "left" : ((self.mouseX - distance), self.mouseY),
                "down" : (self.mouseX, (self.mouseY - distance)),
                "right" : ((self.mouseX + distance), self.mouseY)

            }[direction]

            # drift?
            moveTo(x = x, y = y)

        except KeyError: return self.errorMouseDirection


    def date(self, month, day, year):
        """  """

        pass