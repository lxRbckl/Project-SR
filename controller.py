from pygetwindow import getAllWindows


class Controller:


    def __init__(self):
        """
        - Find()
        - Date()
        - Mouse()
        - Click()
        - Keyboard()
        - TakeScreenshot()
        DONE - getWindows()
        DONE - setWindow()
        """

        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.windows = {}
        self.excludedWindows = ["", ".", "Settings"]


    def setWindow(self, window):
        """  """

        if (window):

            x, y, w, h = window.split(' ')[:-1]
            self.x = int(x)
            self.y = int(y)
            self.width = int(w)
            self.height = int(h)


    def getWindows(self):
        """  """

        self.windows = {}
        for c, w in enumerate(getAllWindows()):

            if (w.title not in self.excludedWindows):

                # if (existing) <
                # else (then new) <
                if (w.title in self.windows):

                    self.windows[w.title]["count"] += 1
                    continue

                else: self.windows[w.title] = {

                    "count" : 1,
                    "label" : w.title,
                    "value" : f"{w.left} {w.top} {w.width} {w.height} {c}"

                }

                # >

        return list(self.windows.values())


    def TakeScreenshot(self):
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