from ..config import layoutColWidth

from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Layout:

   
   def __init__(self, children):
      '''  '''

      self.children = children


   @property
   def Build(self):
      '''  '''

      return dmc.MantineProvider(

         children = dmc.Center(

            className = "layoutCenter",
            children = dbc.Col(

               width = layoutColWidth,
               children = self.children

            )

         )

      )