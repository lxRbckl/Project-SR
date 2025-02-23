from ...config import app

from time import sleep
from dash.dependencies import (Input, Output, State)


class Build:


   def __init__(self):
      '''  '''

      self.redirectTo = "Run"

      self.clearOnClickCallback()
      self.createOnClickCallback()
      self.textareaOnInputCallback()
      self.clearOnDisabledCallback()


   def textareaOnInputCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = False,
         inputs = [

            Input("buildTextareaId", "value")

         ],
         output = [

            Output("buildCreateButtonId", "disabled")

         ],
         state = [



         ]

      )
      def func(textareaValue):

         isEmpty = (textareaValue == "")

         return [isEmpty]


   def createOnClickCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = [
            
            Input("buildCreateButtonId", "n_clicks")
            
         ],
         output = [

            Output("bodyAccordionId", "value", allow_duplicate = True),
            Output("runOutputStackId", "children", allow_duplicate = True)

         ],
         state = [

            State("buildTextareaId", "value")

         ]

      )
      def func(createClick, textareaValue): 

         commands = []
         for c in textareaValue:

            print(c)
            commands.append(c)

            # here we are going to want to import the command view
            # and build the row component to display what's going on
            # from here.
            # then we will have a event listener/callback section that
            # will send commands to run->controllers based on what is
            # currently running (command-wise)
            # once we have MADE all the callbacks (above may change now)
            # then in RUN they will be ran. in ran's callback we will control
            # the continue button accordingly, and that will control the   
            # runtime of each command that is generated

            # TD;DR
            # insert and send views here. IDs:callback will be an issue (dynamic?)
            # then in the run callback we will control the runtime and execution of these
            # commands we decipher from build should follow a hierchy of important approach

         return [self.redirectTo, commands]
      

   def clearOnDisabledCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = [

            Input("buildCreateButtonId", "disabled")

         ],
         output = [

            Output("buildClearButtonId", "disabled", allow_duplicate = True)

         ],
         state = [



         ]

      )
      def func(createDisabled): return [createDisabled]


   def clearOnClickCallback(self):
      '''  '''

      @app.callback(

         prevent_initial_call = True,
         inputs = [

            Input("buildClearButtonId", "n_clicks")

         ],
         output = [

            Output("buildTextareaId", "value", allow_duplicate = True)

         ],
         state = [

            

         ]

      )
      def func(clearClick): return [""]