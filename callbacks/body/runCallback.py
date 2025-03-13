from config import app

from time import sleep
from dash.dependencies import (Input, Output, State)


class Run:


   def __init__(self, notifier, stepsModel, stepsComponent):
      """  """

      self.stopOnClickCallback()
      self.stepsOnInputCallback()
      self.startOnClickCallback()

      self.isRunning = True
      self.notifier = notifier
      self.redirectTo = "Result"
      self.stepsModel = stepsModel
      self.stepsComponent = stepsComponent


   def stepsOnInputCallback(self):
      """  """
   
      @app.callback(

         prevent_initial_call = False,
         output = [

            Output("runStartButtonId", "disabled"),
            Output("runWindowSelectId", "disabled")

         ],
         inputs = [

            Input("runWindowSelectId", "value"),
            Input("runStepsStackId", "children")

         ]
      )
      def func(windowValue, stepsChildren): return [(windowValue == None), (stepsChildren == None)]


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