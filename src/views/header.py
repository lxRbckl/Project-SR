from dash import html
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
         children = [

            # (title, version, breaker) <
            dbc.Col(

               width = "auto",
               id = "headerColTitle",
               className = "headerColTitle",
               children = html.H1(

                  children = None,
                  id = "headerTitle",
                  className = "card-title"

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
                  id = "headerVersion"

               )

            ),
            html.Hr()

            # >

         ]

      )