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

      return dbc.Row(

         children = html.H1("Build")

      )