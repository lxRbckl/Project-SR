from ...config import app
from dash.dependencies import (Input, Output, State)


class Run:


   def __init__(self):
      '''  '''

      self.startCallback()
   

   def startCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         state = [
            State("runStartButtonId", "disabled")
         ],
         output = [
            Output("runStopButtonId", "disabled"),
            Output("runStartButtonId", "children"),
            Output("buildCreateButtonId", "disabled")
         ],
         inputs = [
            Input("runStartButtonId", "n_clicks")

         ]

      )
      def func(*args):
         print(args)
         return [False, "...", True]