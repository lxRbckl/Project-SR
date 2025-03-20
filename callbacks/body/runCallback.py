from config import (app, iconWarning)

from time import sleep
from dash.dependencies import (Input, Output, State)


class Run:


   def __init__(self, notifier, controller, stepsModel, stepsComponent):
      """  """

      self.stopOnClickCallback()
      self.stepsOnInputCallback()
      self.startOnClickCallback()
      self.windowOnValueCallback()

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
         options = [{"label" : w["label"], "value" : w["value"]} for w in windows]
         notifications = [

            self.notifier.notify(

               duration = 1000, # remove when finished

               color = "yellow",
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


   def startOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = [

            Input("runStartButtonId", "n_clicks")

         ],
         output = [

            Output("result", "children", allow_duplicate = True)

         ],
         state = [

            State("buildOptionsMultiSelectId", "value")

         ],
         running = [

            (Output("runStartButtonId", "loading"), True, False),
            (Output("runStopButtonId", "disabled"), False, True),
            (Output("runWindowSelectId", "disabled"), True, False),
            (Output("buildCreateButtonId", "disabled"), True, False),
            (Output("buildInputTextareaId", "disabled"), True, False)

         ]

      )
      def func(startClick, buildOptions):

         print('startOnClickCallback()', startClick, buildOptions) # remove

         return None

         # self.isRunning = True
         # while (self.isRunning == True):
         #
         #    sleep(3)
         #
         # return None
      
   
   def stopOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("runStopButtonId", "n_clicks"),
         output = Output("result", "children", allow_duplicate = True)

      )
      def func(stopClick): 

         self.isRunning = False
         return None