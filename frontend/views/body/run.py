from dash import html
from dash_iconify import DashIconify
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

            justify = "start",
            className = "runControlsRow",
            children = [

               # (run, continue, reset) <
               dbc.Col(

                  width = "auto",
                  children = dmc.Button(

                     size = "xs",
                     children = "Run",
                     id = "runRunButtonId"

                  )

               ),
               dbc.Col(

                  width = "auto",
                  children = dmc.Button(

                     size = "xs",
                     disabled = True,
                     children = "Continue",
                     id = "runContinueButtonId"

                  )

               ),
               dbc.Col(

                  width = "auto",
                  children = dmc.Button(

                     size = "xs",
                     id = "runResetButtonId",
                     children = DashIconify(

                        width = 15,
                        icon = "carbon:reset"

                     )

                  )

               )

               # >

            ]
            
         )

         # >

      ]