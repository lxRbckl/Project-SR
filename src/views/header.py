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

         justify = "between",
         className = "headerRow example2",
         children = [

            # (title, version) <
            dbc.Col(

               width = "auto",
               id = "headerColTitle",
               className = "headerColTitle",
               children = html.H1(

                  children = None,
                  id = "headerTitle",
                  className = "headerTitleH1"

               )

            ),
            dbc.Col(

               align = "end",
               width = "auto",
               id = "headerColVersion",
               className = "headerColVersion",
               children = dbc.Label(

                  size = "sm",
                  children = None,
                  id = "headerVersion",
                  className = "headerVersionLabel"

               )

            )

            # >

         ]

      )