from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

class Header:


   def __init__(self):
      '''  '''

      pass


   @property
   def Build(self):
      '''  '''

      return dbc.Row(

         id = "headerRowId",
         justify = "between",
         className = "headerRow",
         children = [

            dbc.Col(

               width = "auto",
               className = "colExtended",
               children = [

                  # (title) <
                  html.H1(

                     children = None,
                     id = "headerTitle",
                     className = "headerTitleH1"

                  )

                  # >

               ]

            ),
            dbc.Col(

               align = "end",
               width = "auto",
               className = "colExtended",
               children = [

                  # (version) <
                  dbc.Label(

                     size = "sm",
                     children = None,
                     id = "headerVersion",
                     className = "headerVersionLabel"

                  )

                  # >

               ]

            )

         ]

      )