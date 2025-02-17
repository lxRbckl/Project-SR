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

            justify = "between",
            children = [

               dbc.Col(

                  className = "buildSubmitCol",
                  children = dmc.Button(

                     size = "xs",
                     children = "Submit",
                     id = "buildSubmitButtonId"

                  )

               )

            ]

         )

         # >

      ]