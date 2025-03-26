from config import (app, iconWarning)

from dash import html
from time import sleep
from dash import (Input, Output, State, ctx, ALL, callback_context)


class Run:


   def __init__(self, notifier, controller, stepsModel, stepsComponent):
      """  """


      self.startOnLoadingCallback()

      self.stopOnClickCallback()
      # self.onStepChangeCallback() # <-
      self.stepsOnInputCallback()
      self.windowOnValueCallback()
      self.onStatusChangeCallback() # <-
      self.onResultChangeCallback() # <-

      self.notifier = notifier
      self.stepsModel = stepsModel
      self.controller = controller
      self.stepsComponent = stepsComponent

      self.redirectTo = "Run"
      self.stepsOnWarningMessage = lambda c, l: f"There are {c} windows of {l} open."


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

         if (windowValue): self.controller.setWindow(windowValue)
         return [False, (windowValue == None)]


   def startOnLoadingCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("runStartButtonId", "loading"),
         output = [

            Output("runStopButtonId", "disabled", allow_duplicate = True),
            Output("runStartButtonId", "n_clicks", allow_duplicate = True)

         ]

      )
      def func(startLoading): return [(startLoading == False), 0]


   def stopOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("runStopButtonId", "n_clicks"),
         output = Output("runStartButtonId", "loading")

      )
      def func(stopClick): return False


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
            State({"type" : "result-btn", "index" : ALL}, "children"),

         ],
         inputs = [

            Input("runStartButtonId", "n_clicks"),
            Input("runRetryButtonId", "n_clicks"),
            Input({"type" : "status-btn", "index" : ALL}, "children")

         ],
         output = [

            Output("runStartButtonId", "loading", allow_duplicate = True),
            Output("runRetryButtonId", "disabled", allow_duplicate = True),
            Output("runContinueButtonId", "disabled", allow_duplicate = True),
            Output({"type" : "result-btn", "index" : ALL}, "children")

         ]

      )
      def func(startClick, retryClick, statusChildren, startLoading, resultChildren):

         # self.stepsModel.ignoreAlerts = ("Ignore Alerts" in buildOptions)
         # self.stepsModel.overrideInputs = ("Override Inputs" in buildOptions)

         rRetryDisabled = True
         rContinueDisabled = True
         rStartLoading = startLoading
         rResultChildren = resultChildren

         if (startClick == 0): self.stepsModel.currentStep = 0
         if ((startClick > 0) or rStartLoading):

            rStartLoading = True
            result = self.stepsModel.runStep()

            # if (failure) <
            # else (then success) <
            if (result):

               rRetryDisabled = False
               rContinueDisabled = False
               rResultChildren[self.stepsModel.currentStep] = "check"

               for i in range(len(rResultChildren)):

                  rResultChildren[i] = "check"

            else: pass

            # >

         print('status', len(rResultChildren), rResultChildren[0])
         return [rStartLoading, rRetryDisabled, rContinueDisabled, rResultChildren]


   def onResultChangeCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         state = [

            State("runStartButtonId", "loading"),
            State("buildOptionsMultiSelectId", "values"),
            State({"type" : "step-row", "index" : ALL}, "children"),
            State({"type" : "status-btn", "index" : ALL}, "children")

         ],
         inputs = [

            Input("runContinueButtonId", "n_clicks"),
            Input({"type" : "result-btn", "index" : ALL}, "children")

         ],
         output = [

            Output("runProgressId", "value", allow_duplicate = True),
            Output("notificationDiv", "children", allow_duplicate = True),
            Output("runStartButtonId", "loading", allow_duplicate = True),
            Output({"type" : "step-row", "index" : ALL}, "children", allow_duplicate = True),
            Output({"type" : "status-btn", "index" : ALL}, "children", allow_duplicate = True)

         ]

      )
      def func(continueClick, resultChildren, startLoading, optionsValues, stepChildren, statusChildren):

         print('result', len(resultChildren), resultChildren) # remove

         rStartLoading = startLoading
         rStepChildren = stepChildren
         rNotificationChildren = None
         rStatusChildren = statusChildren
         rProgressValue = self.stepsModel.currentStep

         if (startLoading):

            # print('RESULT TRIGGERED') # REMOVE

            flags = self.stepsModel.steps[self.stepsModel.currentStep]["flags"]


         return [rProgressValue, rNotificationChildren, rStartLoading, rStepChildren, rStatusChildren]