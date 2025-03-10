from config import (
   
   app, 
   accordionLoadTime,
   defaultAccordionItem

)

from time import sleep
from dash.dependencies import (Input, Output, State)


class Body:


   def __init__(self):
      """  """

      self.accordionOnLoadCallback()


   def accordionOnLoadCallback(self):
      """  """

      @app.callback(

         output = Output("bodyAccordionId", "value"),
         inputs = Input("bodyAccordionId", "children")

      )
      def func(accordionValue):

         sleep(accordionLoadTime)
         return defaultAccordionItem