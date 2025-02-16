from ...config import (
   
   app, 
   accordionLoadTime,
   defaultAccordionItem

)

from time import sleep
from dash.dependencies import (Input, Output)


class Body:


   def __init__(self):
      '''  '''

      self.accordionCallback()


   def accordionCallback(self):
      '''  '''

      @app.callback(

         output = Output("bodyAccordionId", "value"),
         inputs = [Input("bodyAccordionId", "children")]

      )
      def func(arg): 

         sleep(accordionLoadTime)
         return defaultAccordionItem