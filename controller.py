import pytesseract
from time import sleep
from os.path import join
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

from config import (tesseract, referencesChildSubDir)


class Controller:


    def __init__(self):
        """
        DONE - setWindow()
        DONE - getWindows()
        DONE - takeScreenshot()

        DONE - wait(?duration)
        DONE - click(?multiple)
        DONE - keyboard(message)
        TODO - date(month, day, year)
        DONE - _findText(text, ?index)
        DONE - mouse(asset<text/image>)
        DONE - _findImage(image, ?index)
        DONE - scroll(direction, ?distance)
        DONE - find(asset<text/image>, ?index)
        """

        pytesseract.pytesseract.tesseract_cmd = tesseract

        self.allWindows = []
        self.screenshot = None
        self.useGrayscale = True
        self.selectedWindow = None
        self.excludedWindows = ["", ".", "Settings"]

        self.defaultFindIndex = 0
        self.defaultWaitDuration = 3
        self.defaultClickMultiple = 1
        self.defaultMouseDistance = 10
        self.defaultScrollDistance = 10
        self.defaultScreenshotName = "screenshot.png"
        self.defaultImageFormats = [".png", ".jpg", ".jpeg"]

        self.errorWindowDNE = "Unable to find window. Is window open?"
        self.errorWaitDuration = "Unable to wait. Is duration set correctly?"
        self.errorFindIndex = "Unable to convert index. Is index set correctly?"
        self.errorClickMultiple = "Could not click. Consider adjusting multiple."
        self.errorTextNotFound = "Could not find text in window. Is it case sensitive?"
        self.errorImageDNE = "Image does not exist in folder. Has reference been added?"
        self.errorMouseDistance = "Unable to convert distance. Is distance set correctly?"
        self.errorFindConfidence = "Unable to convert confidence. Is confidence set correctly?"
        self.errorImageNotFound = "Could not find image in window. Consider refining screenshot."
        self.errorMouseDirection = "Mouse direction does not exist. Consider adjusting direction."
        self.errorScrollDirection = "Scroll direction does not exist. Consider adjusting direction."

        self.flags = {

            "alert" : False,
            "pause" : False,
            "skip" : False

        }
        self.commands = {

            # "date": self.date,
            "find" : self.find,
            "wait" : self.wait,
            "click" : self.click,
            "mouse" : self.mouse,
            "scroll" : self.scroll,
            "keyboard" : self.keyboard,
            "update": self.takeScreenshot

        }


    def setWindow(self, title):
        """  """

        # if (window exists) <
        # else (then window DNE) <
        for w in self.allWindows:

            if (title == w.title):

                self.selectedWindow = w
                break

        else: return self.errorWindowDNE

        # >


    def getWindows(self):
        """  """

        returnWindows = {}
        self.allWindows = getAllWindows()
        for w in [w for w in self.allWindows if (w.title not in self.excludedWindows)]:

            # if (existing) <
            # else (then new) <
            if (w.title in returnWindows.keys()):

                windowCount = (returnWindows[w.title]["count"] + 1)

                returnWindows[w.title]["title"] = f"{w.title}-{windowCount}"
                returnWindows[w.title]["count"] = windowCount
                continue

            else: returnWindows[w.title] = {

                "count" : 1,
                "label" : w.title,
                "title" : f"{w.title}-1"

            }

            # >

        return list(returnWindows.values())


    def takeScreenshot(self, *args):
        """  """

        self.screenshot = screenshot(

            imageFilename = self.defaultScreenshotName,
            region = (

                self.selectedWindow.left,
                self.selectedWindow.top,
                self.selectedWindow.width,
                self.selectedWindow.height

            )

        )


    def _findText(self, text):
        """  """

        data = pytesseract.image_to_data(

            lang = "eng",
            config = r'--psm 11',
            output_type = "dict",
            image = self.screenshot,

        )

        results = []
        for i, (conf, content) in enumerate(zip(data["conf"], data["text"])):

            # print(conf, content) # remove

            if (text in content):

                results.append((

                    data["left"][i],
                    data["top"][i],
                    data["width"][i],
                    data["height"][i]

                ))

        # if (found) <
        # else (then missing) <
        if (len(results) > 0): return results
        else: return self.errorTextNotFound

        # >


    def _findImage(self, image):
        """  """

        try:

            results = list(locateAll(

                grayscale = self.useGrayscale,
                haystackImage = self.screenshot,
                needleImage = join(referencesChildSubDir, image)

            ))

            return results

        except IOError: return self.errorImageDNE
        except ImageNotFoundException: return self.errorImageNotFound


    def find(self, asset, index = None, *args):
        """  """

        try: index = int(index) if index else self.defaultFindIndex
        except ValueError: return self.errorFindIndex

        # if (image) <
        # else (then text) <
        for f in self.defaultImageFormats:

            if (f in asset):

                results = self._findImage(image = asset)
                break

        else: results = self._findText(text = asset)

        # >

        try:

            # if (failure) <
            # else (then success) <
            if (isinstance(results, str)): return results
            else:

                x, y = center(results[index])
                x += self.selectedWindow.left
                y += self.selectedWindow.top

                moveTo(x = x, y = y)

        except IndexError: return self.errorFindIndex


    def keyboard(self, message, *args):
        """  """

        write(message = message)


    def wait(self, duration = None, *args):
        """  """

        try: sleep(seconds = int(duration) if duration else self.defaultWaitDuration)
        except ValueError: return self.errorWaitDuration


    def scroll(self, direction, distance = None, *args):
        """  """

        try:

            clicks = {

                "up" : int(distance) if distance else self.defaultScrollDistance,
                "down" : -int(distance) if distance else -self.defaultScrollDistance

            }[direction]

            scroll(clicks = clicks)

        except KeyError: return self.errorScrollDirection


    def click(self, multiple = None, *args):
        """  """

        try: click(clicks = int(multiple) if multiple else self.defaultClickMultiple)
        except ValueError: return self.errorClickMultiple


    def mouse(self, direction, distance = None, *args):
        """  """

        try:

            try: distance = int(distance) if distance else self.defaultMouseDistance
            except ValueError: return self.errorMouseDistance
            x, y = {

                "up" : (self.selectedWindow.left, (distance + self.selectedWindow.top)),
                "left" : ((self.selectedWindow.left - distance), self.selectedWindow.top),
                "down" : (self.selectedWindow.left, (self.selectedWindow.top - distance)),
                "right" : ((self.selectedWindow.left + distance), self.selectedWindow.top)

            }[direction]

            moveTo(x = x, y = y)

        except KeyError: return self.errorMouseDirection


    def date(self, month, day, year, *args):
        """  """

        pass