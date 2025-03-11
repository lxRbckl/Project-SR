from config import app

from time import sleep
from dash.dependencies import (Input, Output, State)


class Run:


   def __init__(self, stepsModel):
      """  """

      self.stopOnClickCallback()
      self.stackOnInputCallback()
      self.startOnClickCallback()

      self.isRunning = True
      self.redirectTo = "Result"
      self.stepsModel = stepsModel


   def stackOnInputCallback(self):
      """  """
   
      @app.callback(

         prevent_initial_call = False,
         inputs = Input("runStepsStackId", "children"),
         output = Output("runStartButtonId", "disabled")

      )
      def func(stackValue): return (stackValue == None)


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

            sleep(1)
         
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