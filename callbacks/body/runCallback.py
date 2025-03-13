from config import (app, iconWarning)

from time import sleep
from dash.dependencies import (Input, Output, State)


class Run:


   def __init__(self, notifier, controller, stepsModel, stepsComponent):
      """  """

      self.stopOnClickCallback()
      self.stepsOnInputCallback()
      self.startOnClickCallback()

      self.isRunning = True
      self.notifier = notifier
      self.redirectTo = "Result"
      self.stepsModel = stepsModel
      self.controller = controller
      self.stepsComponent = stepsComponent


   def stepsOnInputCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("runStepsStackId", "children"),
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

               duration = 1000, # remove

               color = "yellow",
               icon = iconWarning,
               message = "There are {} windows of {}.".format(w["count"], w["label"])

            )

         for w in windows if (w["count"] > 1)]

         return [options, notifications, (stepsChildren is None)]


   def startOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("runStartButtonId", "n_clicks"),
         output = Output("result", "children", allow_duplicate = True),
         running = [

            (Output("runStartButtonId", "loading"), True, False),
            (Output("runStopButtonId", "disabled"), False, True),
            (Output("buildCreateButtonId", "disabled"), True, False),
            (Output("buildInputTextareaId", "disabled"), True, False)

         ]

      )
      def func(startClick):

         self.isRunning = True
         while (self.isRunning == True):

            sleep(3)
         
         return None
      
   
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