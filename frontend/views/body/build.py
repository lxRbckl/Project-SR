from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Build:


   def __init__(self, instruction):
      '''  '''

      self.id = "buildId"
      self.value = "Build"

      self.instruction = instruction


   @property
   def Build(self):
      '''  '''

      return [

         # (input, controls) <
         dbc.Row(

            className = "buildInputRow",
            children = dmc.Textarea(

               value = "",
               minRows = 5,
               maxRows = 20,
               error = None,
               autosize = True,
               autoComplete = "on",
               id = "buildTextareaId",
               className = "buildTextarea"

            )

         ),
         dbc.Row(

            justify = "between",
            className = "buildControlsRow",
            children = [

               dbc.Col(

                  width = "auto",
                  className = "colExtended",
                  children = [

                     # (create) <
                     dmc.Button(

                        size = "xs",
                        disabled = None,
                        children = "Create",
                        id = "buildCreateButtonId"

                     )

                     # >

                  ]

               ),
               dbc.Col(

                  width = "auto",
                  className = "colExtended",
                  children = [

                     # (clear) <
                     dmc.Button(

                        size = "xs",
                        disabled = None,
                        children = "Clear",
                        id = "buildClearButtonId"

                     )

                     # >

                  ]

               )

            ]

         )

         # >

      ]