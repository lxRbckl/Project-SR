from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Run:


   def __init__(self):
      '''  '''

      self.id = "runId"
      self.value = "Run"
      self.isPaused = False
      self.isDisabled = False


   @property
   def Build(self):
      '''  '''

      return [

         # (steps, controls) <
         dbc.Stack(

            children = None,
            id = "runStepsStackId",
            className = "runStepsStack"

         ),
         dbc.Row(

            justify = "between",
            className = "runControlsRow",
            children = [

               dbc.Col(

                  width = "auto",
                  className = "colExtended",
                  children = [

                     # (start, continue) <
                     dmc.Button(

                        size = "xs",
                        disabled = True,
                        children = "Start",
                        id = "runStartButtonId",
                        loaderProps = {"type" : "dots"}

                     ),
                     dmc.Button(

                        size = "xs",
                        disabled = True,
                        children = "Continue",
                        id = "runContinueButtonId",
                        className = "runContinueButton"

                     )

                     # >

                  ]

               ),
               dbc.Col(

                  width = "auto",
                  className = "colExtended",
                  children = [

                     # (stop) <
                     dmc.Button(

                        size = "xs",
                        disabled = True,
                        children = "Stop",
                        id = "runStopButtonId"

                     )

                     # >

                  ]

               )

            ]
            
         )

         # >

      ]