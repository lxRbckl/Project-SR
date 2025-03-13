from pygetwindow import getAllWindows


class Controller:


    def __init__(self):
        """
        Find()
        TypeIn/Enter()
        Move/Navigate()
        Click()
        TakeScreenshot()
        DONE getWindows()
        Date()
        """

        pass


    @staticmethod
    def getWindows():
        """  """

        windows = {}
        for w in getAllWindows():

            if (len(w.title) > 0):

                # if (existing) <
                # else (then new) <
                if (w.title in windows):

                    windows[w.title]["count"] += 1
                    continue

                else: windows[w.title] = {

                    "count" : 1,
                    "label" : w.title,
                    "value" : f"{w.left} {w.top} {w.width} {w.height} {len(windows)}"

                }

                # >

        return list(windows.values())







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