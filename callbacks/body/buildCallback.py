from time import sleep
from clipboard import copy

from config import (app, emptyValue)
from dash.dependencies import (Input, Output, State)


class Build:


   def __init__(self, notifier, stepsModel, stepsComponent):
      """  """

      self.copyOnClickCallback()
      self.clearOnClickCallback()
      self.createOnClickCallback()
      self.clearOnDisabledCallback()
      self.textareaOnInputCallback()

      self.redirectTo = "Run"
      self.notifier = notifier
      self.stepsModel = stepsModel
      self.stepsComponent = stepsComponent


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

               print(type(stepsChildren)) # remove
               print(type(self.stepsComponent.build)) # remove

               if (response): return [accordionValue, stepsChildren, response]
               else: return [self.redirectTo, self.stepsComponent.build, None]

         except ValueError: return [accordionValue, stepsChildren, "Invalid notation."]


   def clearOnDisabledCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("buildCreateButtonId", "disabled"),
         output = [

            Output("buildCopyButtonId", "disabled", allow_duplicate=True),
            Output("buildInputTextareaId", "error", allow_duplicate = True),
            Output("buildClearButtonId", "disabled", allow_duplicate = True)

         ]

      )
      def func(createDisabled): return [createDisabled, None, createDisabled]


   def copyOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         state=State("buildInputTextareaId", "value"),
         inputs = Input("buildCopyButtonId", "n_clicks"),
         output = Output("buildInputTextareaId", "value", allow_duplicate = True)

      )
      def func(copyClick, copyValue):
         print(copyClick, copyValue) # remove

         sleep(0.5)
         copy(copyValue)


         return copyValue


   def clearOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("buildClearButtonId", "n_clicks"),
         output = Output("buildInputTextareaId", "value", allow_duplicate = True)

      )
      def func(clearClick): return emptyValue