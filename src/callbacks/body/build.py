from ...config import app

from time import sleep
from dash.dependencies import (Input, Output)


class Build:


   def __init__(self):
      '''  '''

      self.submitCallback()


   def submitCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = [Input("buildSubmitButtonId", "n_clicks")],
         output = [

            Output("bodyAccordionId", "value", allow_duplicate = True)

         ]

      )
      def func(arg):
         '''  '''

         return ["Run"]