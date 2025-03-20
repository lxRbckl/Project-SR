from config import (app, iconWarning)

from time import sleep
from dash import (Input, Output, State, ctx, ALL)


class Run:


   def __init__(self, notifier, controller, stepsModel, stepsComponent):
      """  """

      self.stopOnClickCallback()
      self.stepsOnInputCallback()
      self.windowOnValueCallback()
      # self.onStatusChangeCallback()
      # self.onResultChangeCallback()

      self.notifier = notifier
      self.stepsModel = stepsModel
      self.controller = controller
      self.stepsComponent = stepsComponent

      self.isRunning = True
      self.redirectTo = "Result"
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
         output = Output("runStartButtonId", "disabled", allow_duplicate = True)

      )
      def func(windowValue):

         if (windowValue): self.controller.setWindow(windowValue.split("-")[0])
         return (windowValue == None)


   def stopOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("runStopButtonId", "n_clicks"),
         output = Output("bodyAccordionId", "value", allow_duplicate = True)

      )
      def func(stopClick):

         self.isRunning = False
         return self.redirectTo














   def onStatusChangeCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         state = [

            State("buildOptionsMultiSelectId", "values")

         ],
         inputs = [

            Input("runStartButtonId", "n_clicks"),
            Input("runRetryButtonId", "n_clicks"),
            Input({"type" : "status-btn", "index" : ALL}, "children")

         ],
         output = [

            Output({"type" : "result-btn", "index" : ALL}, "children"),
            Output("runRetryButtonId", "disabled", allow_duplicate = True),
            Output("runContinueButtonId", "disabled", allow_duplicate = True)

         ]

      )
      def func(*args):

         # run controller command and record result to steps->result
         # document.getElementById("step-5").scrollIntoView({behavior: "smooth"})

         # self.stepsModel.ignoreAlerts = ("Ignore Alerts" in buildOptions)
         # self.stepsModel.overrideInputs = ("Override Inputs" in buildOptions)

         print('onStatusChangeCallback()', args) # remove

         while (self.isRunning):

            pass





























   def onResultChangeCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = [

            Input("runContinueButtonId", "n_clicks"),
            Input({"type" : "result-btn", "index" : ALL}, "children")

         ],
         output = [

            Output({"type": "status-btn", "index": ALL}, "children"),
            Output("runProgressId", "value", allow_duplicate = True),
            Output("bodyAccordionId", "value", allow_duplicate = True),
            Output("runStopButtonId", "disabled", allow_duplicate = True),
            Output("runContinueButtonId", "disabled", allow_duplicate = True)

         ]

      )
      def func(*args):

         # increment current step

         print('onResultChangeCallback()', args) # remove

         while (self.isRunning):

            pass















