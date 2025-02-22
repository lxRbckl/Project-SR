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

               # (left, right) <
               dbc.Col(

                  width = "auto",
                  className = "runLeftCol",
                  children = [

                     dmc.Button(

                        size = "xs",
                        children = "Run",
                        id = "runRunButtonId"

                     ),
                     dmc.Button(

                        size = "xs",
                        disabled = True,
                        children = "Continue",
                        id = "runContinueButtonId",
                        className = "runContinueButton"

                     )

                  ]

               ),
               dbc.Col(

                  width = "auto",
                  className = "runRightCol",
                  children = dmc.Button(

                     size = "xs",
                     disabled = True,
                     children = "Stop",
                     id = "runStopButtonId"

                  )

               )

               # >

            ]
            
         )

         # >

      ]