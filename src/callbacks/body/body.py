from ...config import (app)
from dash.dependencies import (Input, Output)


class Body:


   def __init__(self):
      '''  '''

      self.accordionCallback()


   def accordionCallback(self):
      '''  '''

      @app.callback(

         inputs = [Input("bodyAccordionId", "children")],
         outputs = Output("bodyAccordionId", "value")

      )
      def func(arg): return None