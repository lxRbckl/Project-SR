from ...config import app
from dash.dependencies import (Input, Output, State)


class Run:


   def __init__(self):
      '''  '''

      self.stackOnInputCallback()
      self.startOnClickCallback()
      self.stopOnClickCallback()


   def stackOnInputCallback(self):
      '''  '''
   
      @app.callback(

         prevent_initial_call = False,
         inputs = [

            Input("runOutputStackId", "children")

         ],
         output = [

            Output("runStartButtonId", "disabled")

         ],
         state = [



         ]

      )
      def func(*args):
         print("stackOnInputCallback", args) # remove
         return [True]


   def startOnClickCallback(self):
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

         ],
         state = [

            State("runOutputRowId", "children")

         ]

      )
      def func(*args):
         print("startOnClickCallback", args) # remove
         return [False, "...", True, True]
      
   
   def stopOnClickCallback(self):
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

         ],
         state = [


            
         ]

      )
      def func(*args): 
         print("stopOnClickCallback", args) # remove
         return [True, "Start", False, False]