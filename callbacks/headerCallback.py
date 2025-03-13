from config import app
from dash.dependencies import (Input, Output, State)


class Header:


   def __init__(self):
      """  """

      self.versionOnClickCallback()


   def versionOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         output = Output("guideModalId", "opened"),
         inputs = Input("headerVersionButtonId", "n_clicks")

      )
      def func(versionClick): return True