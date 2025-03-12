from config import (app, emptyValue)
from dash.dependencies import (Input, Output, State)


class Build:


   def __init__(self, stepsModel):
      """  """

      self.redirectTo = "Run"
      self.stepsModel = stepsModel

      self.clearOnClickCallback()
      self.createOnClickCallback()
      self.textareaOnInputCallback()
      self.clearOnDisabledCallback()


   def textareaOnInputCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = False,
         inputs = Input("buildInputTextareaId", "value"),
         output = Output("buildCreateButtonId", "disabled")

      )
      def func(textareaValue): return (textareaValue == emptyValue)


   def createOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("buildCreateButtonId", "n_clicks"),
         output = [

            Output("bodyAccordionId", "value", allow_duplicate = True),
            Output("runStepsStackId", "children", allow_duplicate = True),
            Output("buildInputTextareaId", "error", allow_duplicate = True)

         ],
         state = [

            State("bodyAccordionId", "value"),
            State("runStepsStackId", "children"),
            State("buildInputTextareaId", "value")

         ],
         running = [

            (Output("buildCreateButtonId", "loading"), True, False),
            (Output("buildClearButtonId", "disabled"), True, False)

         ]

      )
      def func(createClick, accordionValue, stepsChildren, textareaValue):

         try:

            i = 0
            response = None
            textareaValues = [s for s in textareaValue.split("\n") if (len(s) > 0)]
            while ((response == None) and (len(textareaValues) != i)):

               response = self.stepsModel.addStep(textareaValues[i])
               i += 1

            return [self.redirectTo, "insert steps", response]

         except ValueError: return [accordionValue, stepsChildren, "Invalid notation."]


   def clearOnDisabledCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("buildCreateButtonId", "disabled"),
         output = [

            Output("buildInputTextareaId", "error", allow_duplicate = True),
            Output("buildClearButtonId", "disabled", allow_duplicate = True)

         ]

      )
      def func(createDisabled): return [None, createDisabled]


   def clearOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("buildClearButtonId", "n_clicks"),
         output = Output("buildInputTextareaId", "value", allow_duplicate = True)

      )
      def func(clearClick): return emptyValue