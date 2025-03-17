from config import app
from dash.dependencies import (Input, Output, State)


class Guide:


    def __init__(self):
        """  """

        self.guideOnClickCallback()


    def guideOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input("headerGuideActionIconId", "n_clicks"),
            output = Output("guideModalId", "opened", allow_duplicate = True)

        )
        def func(guideClick): return True