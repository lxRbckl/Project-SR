from dash.dependencies import (Input, Output, State)
from config import (app, emptyValue, runCommands, runParameters)


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

         # try:

         # print('textareaValue', textareaValue) # remove
         # print('tvr', textareaValue.split('\n')) # remove
         # for step in textareaValue:
         #
         #    print('step', step) # remove
         #    command, text, *parameters = step.split(",")
         #
         #    print(command, text, parameters) # remove
         #
         #    # if (command not in runCommands): raise commandError
         #    # for (parameter in parameters.split(""))
         #    #
         #    # self.stepsModel.addStep(
         #    #
         #    #    text=text,
         #    #    command = command,
         #    #    parameters = parameters
         #    #
         #    # )

         textareaError = "There was an error."
         try:

            for step in textareaValue.split('\n'):

               command, text, *parameters = step.split(',')

               if (command not in runCommands):
                  raise
               else: pass

            return [

               self.redirectTo,
               'insert algorithm above return',
               None

            ]

         except incorrectCommand as e: textareaError = f"{e}"
         finally: return [accordionValue, stepsChildren, textareaError]


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