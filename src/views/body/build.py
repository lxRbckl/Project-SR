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
               className = "buildTextarea",
               placeholder = "Insert Commands"

            )

         ),
         dbc.Row(

            justify = "between",
            className = "buildControlsRow",
            children = [

               # (Submit) <
               dbc.Col(

                  width = "auto",
                  className = "buildSubmitCol",
                  children = dmc.Button(

                     size = "xs",
                     children = "Submit",
                     id = "buildSubmitButtonId",
                     className = "buildSubmitButton"

                  )

               )

               # >

            ]

         )

         # >

      ]