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

         # (steps, controls) <
         dbc.Row(

            children = None,
            id = "runStepsRowId",
            className = "runStepsRow"

         ),
         dbc.Row(

            justify = "between",
            className = "runControlsRow",
            children = [

               # (start, end) <
               dbc.Col(

                  width = "auto",
                  className = "runStartCol",
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
                  className = "runEndCol",
                  children = [

                     # (stop) <
                     dmc.Button(

                        size = "xs",
                        disabled = True,
                        children = "Stop",
                        id = "runStopButtonId",

                        className = "test"

                     )

                     # >

                  ]

               )

               # >

            ]
            
         )

         # >

      ]