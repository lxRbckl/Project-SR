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
      self.onStatusChangeCallback() # <-
      # self.onResultChangeCallback() # <-

      self.notifier = notifier
      self.stepsModel = stepsModel
      self.controller = controller
      self.stepsComponent = stepsComponent

      self.redirectTo = "Run"
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
         output = [

            Output("runStartButtonId", "loading", allow_duplicate = True),
            Output("runStartButtonId", "disabled", allow_duplicate = True)

         ]

      )
      def func(windowValue):

         print('windowOnValueCallback()', windowValue) # remove

         if (windowValue): self.controller.setWindow(windowValue)
         return [False, (windowValue == None)]


   def stopOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("runStopButtonId", "n_clicks"),
         output = [

            Output("runStopButtonId", "disabled", allow_duplicate = True),
            Output("runStartButtonId", "loading", allow_duplicate = True),
            Output("bodyAccordionId", "value", allow_duplicate = True)
         ]

      )
      def func(stopClick): return [True, False, self.redirectTo]


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

            State("runStartButtonId", "loading"),
            State("runStopButtonId", "disabled"),
            State("runRetryButtonId", "disabled"),
            State("runContinueButtonId", "disabled"),
            State("buildOptionsMultiSelectId", "values"),
            State({"type" : "result-btn", "index" : ALL}, "children"),

         ],
         inputs = [

            Input("runStartButtonId", "n_clicks"),
            Input("runRetryButtonId", "n_clicks"),
            Input({"type" : "status-btn", "index" : ALL}, "children")

         ],
         output = [

            Output("runStopButtonId", "disabled", allow_duplicate = True),
            Output("runStartButtonId", "loading", allow_duplicate = True),
            Output("runRetryButtonId", "disabled", allow_duplicate = True),
            Output("runContinueButtonId", "disabled", allow_duplicate = True),
            Output({"type" : "result-btn", "index" : ALL}, "children", allow_duplicate = True)

         ]

      )
      def func(startClick, retryClick, statusChildren, startLoading, stopDisabled, retryDisabled, continueDisabled, optionsValues, resultChildren):

         # run controller command, record results back to stepsModel object
         # self.stepsModel.ignoreAlerts = ("Ignore Alerts" in buildOptions)
         # self.stepsModel.overrideInputs = ("Override Inputs" in buildOptions)

         rStopDisabled = stopDisabled
         rStartLoading = startLoading
         rRetryDisabled = retryDisabled
         rResutlChildren = resultChildren
         rContinueDisabled = continueDisabled

         print('onStatusChangeCallback()')
         print(

            '\nstartClick', startClick,
            '\nretryClick', retryClick,
            '\nstatusChildren', statusChildren,
            '\noptionsValue', optionsValues,
            '\nresultChildren', resultChildren,
            '\n---\n'

         )

         if (startClick > 0):

            rStartLoading = True
            rStopDisabled = False

         return [rStopDisabled, rStartLoading, rRetryDisabled, rContinueDisabled, rResutlChildren]


   def onResultChangeCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         state = [

            State("runProgressId", "value"),
            State("bodyAccordionId", "value"),
            State("runStartButtonId", "loading"),
            State({"type" : "step-row", "index" : ALL}, "children"),
            State({"type" : "status-btn", "index" : ALL}, "children")

         ],
         inputs = [

            Input("runContinueButtonId", "n_clicks"),
            Input({"type" : "result-btn", "index" : ALL}, "children")

         ],
         output = [

            Output("runProgressId", "value", allow_duplicate = True),
            Output("bodyAccordionId", "value", allow_duplicate = True),
            Output("runStopButtonId", "disabled", allow_duplicate = True),
            Output("runStartButtonId", "loading", allow_duplicate = True),
            Output("runContinueButtonId", "disabled", allow_duplicate = True),
            Output({"type" : "step-row", "index" : ALL}, "children", allow_duplicate = True),
            Output({"type" : "status-btn", "index" : ALL}, "children", allow_duplicate = True)

         ]

      )
      def func(continueClick, resultChildren, startLoading, progressValue, accordionValue, stepChildren, statusChildren):

         # increment current step on success

         rStopDisabled = True
         rContinueDisabled = True
         rStartLoading = startLoading
         rStepChildren = stepChildren
         rProgressValue = progressValue
         rStatusChildren = statusChildren
         rAccordionValue = accordionValue

         print('onResultChangeCallback()')
         print(

            '\ncontinueClick', continueClick,
            '\nresultChildren', resultChildren,
            '\nstepChildren', stepChildren,
            '\nstatusChildren', statusChildren,
            '\n---\n'

         )

         return [rProgressValue, rAccordionValue, rStopDisabled, rStartLoading, rContinueDisabled, rStepChildren, rStatusChildren]