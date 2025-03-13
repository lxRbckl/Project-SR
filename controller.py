from pygetwindow import getAllWindows


class Controller:


    def __init__(self):
        """  """

        pass


    @staticmethod
    def getWindows():
        """  """

        return {

            w.title : f"{w.left} {w.top} {w.width} {w.height}"

        for w in getAllWindows() if (len(w.title) > 0)}