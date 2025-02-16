from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Run:


   def __init__(self):
      '''  '''

      self.id = "runId"
      self.value = "Run"


   @property
   def Build(self):
      '''  '''

      return dbc.Row(

         children = html.H1("Run")

      )