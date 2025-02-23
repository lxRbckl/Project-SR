from ...config import app
from dash.dependencies import (Input, Output, State)


class Run:


   def __init__(self):
      '''  '''

      self.stopCallback()
      self.startCallback()
   

   def startCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = [

            Input("runStartButtonId", "n_clicks")

         ],
         output = [

            Output("runStopButtonId", "disabled", allow_duplicate = True),
            Output("runStartButtonId", "children", allow_duplicate = True),
            Output("runStartButtonId", "disabled", allow_duplicate = True),
            Output("buildCreateButtonId", "disabled", allow_duplicate = True)

         ]

      )
      def func(*args):
         print(args)
         return [False, "...", True, True]
      
   
   def stopCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = [

            Input("runStopButtonId", "n_clicks")

         ],
         output = [

            Output("runStopButtonId", "disabled", allow_duplicate = True),
            Output("runStartButtonId", "children", allow_duplicate = True),
            Output("runStartButtonId", "disabled", allow_duplicate = True),
            Output("buildCreateButtonId", "disabled", allow_duplicate = True)

         ]

      )
      def func(*args): return [True, "Start", False, False]