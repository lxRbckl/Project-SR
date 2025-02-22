from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Build:


   def __init__(self):
      '''  '''

      self.id = "buildId"
      self.value = "Build"


   @property
   def Build(self):
      '''  '''

      return [

         # (commands, controls) <
         dbc.Row(

            className = "buildCommandsRow",
            children = dmc.Textarea(

               minRows = 5,
               maxRows = 20,
               error = None,
               autosize = True,
               id = "buildTextareaId",
               className = "buildTextarea"

            )

         ),
         dbc.Row(

            className = "buildControlsRow",
            children = [

               dbc.Col(

                  width = "auto",
                  className = "buildCol",
                  children = [

                     # (create) <
                     dmc.Button(

                        size = "xs",
                        children = "Create",
                        id = "buildCreateButtonId"

                     )

                     # >

                  ]

               )

            ]

         )

         # >

      ]