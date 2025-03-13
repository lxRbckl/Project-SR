from config import app
from dash.dependencies import (Input, Output, State)


class Body:


   def __init__(self):
      """  """

      self.accordionOnLoadCallback()
      self.defaultAccordionValue = "Build"


   def accordionOnLoadCallback(self):
      """  """

      @app.callback(

         output = Output("bodyAccordionId", "value"),
         inputs = Input("bodyAccordionId", "children")

      )
      def func(accordionValue): return self.defaultAccordionValue