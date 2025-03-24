from config import (app, iconWarning)

from dash import html
from time import sleep
from dash import (Input, Output, State, ctx, ALL)


class Run:


   def __init__(self, notifier, controller, stepsModel, stepsComponent):
      """  """

      self.stopOnClickCallback()
      # self.onStepChangeCallback() # <-
      self.stepsOnInputCallback()
      self.windowOnValueCallback()
      # self.onStatusChangeCallback() # <-
      # self.onResultChangeCallback() # <-

      self.notifier = notifier
      self.stepsModel = stepsModel
      self.controller = controller
      self.stepsComponent = stepsComponent

      self.redirectTo = "Result"
      self.stepsOnWarningMessage = lambda c, l: f"There are {c} windows of {l} open."

      self.run = {



      }


   def stepsOnInputCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("runStepsRowId", "children"),
         output = [

            Output("runWindowSelectId", "data", allow_duplicate = True),
            Output("notificationDiv", "children", allow_duplicate = True),
            Output("runWindowSelectId", "disabled", allow_duplicate = True)

         ]

      )
      def func(stepsChildren):

         windows = self.controller.getWindows()
         options = [{"label" : w["label"], "value" : w["title"]} for w in windows]
         notifications = [

            self.notifier.notify(

               color = "yellow",
               duration = 10000,
               icon = iconWarning,
               message = self.stepsOnWarningMessage(c = w["count"], l = w["label"])

            )

         for w in windows if (w["count"] > 1)]

         return [options, notifications, (stepsChildren is None)]


   def windowOnValueCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("runWindowSelectId", "value"),
         output = Output("runStartButtonId", "disabled", allow_duplicate = True)

      )
      def func(windowValue):

         if (windowValue): self.controller.setWindow(windowValue)
         return (windowValue == None)


   def stopOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("runStopButtonId", "n_clicks"),
         output = Output("bodyAccordionId", "value", allow_duplicate = True)

      )
      def func(stopClick):

         self.stepsModel.isRunning = False
         return self.redirectTo


   def onStepChangeCallback(self):
      """  """

      app.clientside_callback(

         """
         function scrollToStep(step) {

             const element = document.getElementById(`step-${step}`);

             if (element) {
                 element.scrollIntoView({behavior: "smooth"});
             }

         }
         """,
         Output("runProgressId", "value"),
         Input("runCountButtonId", "children")

      )


   def onStatusChangeCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         state = [

            State("runStartButtonId", "disabled"),
            State("buildOptionsMultiSelectId", "values"),
            State({"type" : "result-btn", "index" : ALL}, "children")

         ],
         inputs = [

            Input("runStartButtonId", "n_clicks"),
            Input("runRetryButtonId", "n_clicks"),
            Input({"type" : "status-btn", "index" : ALL}, "children")

         ],
         output = [

            Output("runRetryButtonId", "disabled", allow_duplicate = True),
            Output("runContinueButtonId", "disabled", allow_duplicate = True),
            Output({"type" : "result-btn", "index" : ALL}, "children", allow_duplicate = True)

         ]

      )
      def func(startClick, retryClick, statusChildren, startDisabled, optionsValues, resultChildren):

         # run controller command and record result to steps->result
         # self.stepsModel.ignoreAlerts = ("Ignore Alerts" in buildOptions)
         # self.stepsModel.overrideInputs = ("Override Inputs" in buildOptions)

         print('onStatusChangeCallback()')
         print(startClick, retryClick, statusChildren, optionsValues, resultChildren)
         print()

         rRetryDisabled = True
         rContinueDisabled = True
         rResutlChildren = resultChildren

         return [rRetryDisabled, rContinueDisabled, rResutlChildren]


   def onResultChangeCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         state = [

            State("runProgressId", "value"),
            State("bodyAccordionId", "value"),
            State({"type" : "step-row", "index" : ALL}, "children"),
            State({"type" : "status-btn", "index" : ALL}, "children"),

         ],
         inputs = [

            Input("runContinueButtonId", "n_clicks"),
            Input({"type" : "result-btn", "index" : ALL}, "children")

         ],
         output = [

            Output("runProgressId", "value", allow_duplicate = True),
            Output("bodyAccordionId", "value", allow_duplicate = True),
            Output("runStopButtonId", "disabled", allow_duplicate = True),
            Output("runContinueButtonId", "disabled", allow_duplicate = True),
            Output({"type" : "step-row", "index" : ALL}, "children", allow_duplicate = True),
            Output({"type" : "status-btn", "index" : ALL}, "children", allow_duplicate = True)

         ]

      )
      def func(continueClick, resultChildren, progressValue, accordionValue, stepChildren, statusChildren):

         # increment current step on success

         print('onResultChangeCallback()')
         print(continueClick, resultChildren, stepChildren, statusChildren)
         print()

         rStopDisabled = True
         rContinueDisabled = True
         rStepChildren = stepChildren
         rProgressValue = progressValue
         rStatusChildren = statusChildren
         rAccordionValue = accordionValue

         return [rProgressValue, rAccordionValue, rStopDisabled, rContinueDisabled, rStepChildren, rStatusChildren]