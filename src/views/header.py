import dash_bootstrap_components as dbc

from ..config import currentVersion

from dash import html


class Header:


   def __init__(self):
      '''  '''

      pass


   @property
   def Build(self):
      '''  '''

      return dbc.Row(

         align = "end",
         justify = "between",
         children = [

            # (title, version, breaker) <
            dbc.Col(

               width = "auto",
               children = None,
               id = "headerTitle",
               className = "headerTitle"

            ),
            dbc.Col(

               width = "auto",
               children = None,
               id = "headerVersion",
               className = "headerVersion"

            ),
            html.Hr()

            # >

         ]

      )