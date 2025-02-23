from ...config import app

from time import sleep
from dash.dependencies import (Input, Output, State)


class Build:


   def __init__(self):
      '''  '''

      self.redirectTo = "Run"

      self.clearOnClickCallback()
      self.createOnClickCallback()
      self.textareaOnInputCallback()
      self.clearOnDisabledCallback()


   def textareaOnInputCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = False,
         inputs = [

            Input("buildTextareaId", "value")

         ],
         output = [

            Output("buildCreateButtonId", "disabled")

         ],
         state = [



         ]

      )
      def func(textareaValue):

         isEmpty = (textareaValue == "")

         return [isEmpty]


   def createOnClickCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = [
            
            Input("buildCreateButtonId", "n_clicks")
            
         ],
         output = [

            Output("bodyAccordionId", "value", allow_duplicate = True),
            Output("runOutputStackId", "children", allow_duplicate = True)

         ],
         state = [

            State("buildTextareaId", "value")

         ]

      )
      def func(createClick, textareaValue): 

         commands = []
         for c in textareaValue:

            print(c)
            commands.append(c)

         return [self.redirectTo, commands]
      

   def clearOnDisabledCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = [

            Input("buildCreateButtonId", "disabled")

         ],
         output = [

            Output("buildClearButtonId", "disabled", allow_duplicate = True)

         ],
         state = [



         ]

      )
      def func(createDisabled): return [createDisabled]


   def clearOnClickCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = [

            Input("buildClearButtonId", "n_clicks")

         ],
         output = [

            Output("buildTextareaId", "value", allow_duplicate = True)

         ],
         state = [

            

         ]

      )
      def func(clearClick): return [""]