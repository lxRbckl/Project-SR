from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Run:


   def __init__(self):
      '''  '''

      self.id = "runId"
      self.value = "Run"


   @property
   def Build(self):
      '''  '''

      return [

         # (output, controls) <
         dbc.Stack(

            children = None,
            id = "runOutputStackId",
            className = "runOutputStack"

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
                        children = "Start",
                        id = "runStartButtonId"

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