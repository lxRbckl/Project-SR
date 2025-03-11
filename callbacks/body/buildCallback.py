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

            return [

               self.redirectTo,
               'insert algorithm above return',
               None

            ]

         except KeyError: return [accordionValue, stepsChildren, "There was an error."]


   def optionsOnLoadCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = False,
         inputs = Input("", ""),
         output = Output("", "")

      )
      def func(): return self.buildModel
      

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