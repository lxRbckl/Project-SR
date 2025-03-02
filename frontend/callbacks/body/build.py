from ...config import (app, emptyValue)
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
         inputs = Input("buildTextareaId", "value"),
         output = Output("buildCreateButtonId", "disabled")

      )
      def func(textareaValue): return (textareaValue == emptyValue)


   def createOnClickCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("buildCreateButtonId", "n_clicks"),
         output = [

            Output("buildTextareaId", "error", allow_duplicate = True),
            Output("bodyAccordionId", "value", allow_duplicate = True),
            Output("runOutputStackId", "children", allow_duplicate = True)

         ],
         state = [

            State("buildTextareaId", "value"),
            State("bodyAccordionId", "value"),
            State("runOutputStackId", "children")

         ],
         running = [

            (Output("buildCreateButtonId", "loading"), True, False),
            (Output("buildClearButtonId", "disabled"), True, False)

         ]

      )
      def func(createClick, textareaValue, stackChildren, accordionValue):

         try:

            pass
            # result = 

         except KeyError: errorMessage = "There was an error."
         finally: return [errorMessage, accordionValue, stackChildren]
      

   def clearOnDisabledCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("buildCreateButtonId", "disabled"),
         output = [

            Output("buildTextareaId", "error", allow_duplicate = True),
            Output("buildClearButtonId", "disabled", allow_duplicate = True)

         ]

      )
      def func(createDisabled): return [None, createDisabled]


   def clearOnClickCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("buildClearButtonId", "n_clicks"),
         output = Output("buildTextareaId", "value", allow_duplicate = True)

      )
      def func(clearClick): return emptyValue