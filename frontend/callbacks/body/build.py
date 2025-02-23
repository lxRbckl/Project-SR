from ...config import app

from time import sleep
from dash.dependencies import (Input, Output, State)


class Build:


   def __init__(self):
      '''  '''

      self.textareaCallback()
      self.submitCallback()
      self.clearCallback()


   def textareaCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = [

            Input("buildTextareaId", "children")

         ],
         output = [

            Output("buildCreateButtonId", "disabled")

         ],
         state = [



         ]

      )
      def func(arg):
         print("textareaCallback", arg)
         return [False]


   def submitCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = [
            
            Input("buildCreateButtonId", "n_clicks")
            
         ],
         output = [

            Output("bodyAccordionId", "value", allow_duplicate = True)

         ],
         state = [

            

         ]

      )
      def func(arg):

         return ["Run"]
      

   def clearCallback(self):
      '''  '''

      @app.callback(

         precent_initial_call = True,
         inputs = [

            Input("buildCreateButtonId", "disabled")

         ],
         output = [

            Output("buildClearButtonId", "disabled")

         ],
         state = [



         ]

      )
      def func(arg): return [arg]