from ...config import emptyValue

from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Build:


   def __init__(self, instruction):
      '''  '''

      self.id = "buildId"
      self.value = "Build"
      self.isDisabled = False

      self.instruction = instruction


   @property
   def Build(self):
      '''  '''

      return [

         # (input, controls) <
         dbc.Row(

            className = "buildInputRow",
            children = dmc.Textarea(

               minRows = 5,
               maxRows = 20,
               error = None,
               autosize = True,
               value = emptyValue,
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
                        id = "buildCreateButtonId",
                        loaderProps = {"type" : "dots"}

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