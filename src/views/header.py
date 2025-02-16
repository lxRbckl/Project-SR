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

         className = "",
         justify = "end",
         children = [

            # title <
            # version <
            dbc.Col(

               children = html.H1("Project")

            ),
            dbc.Col(

               children = html.H3("version")

            ),

            # >

            html.Hr()

         ]

      )