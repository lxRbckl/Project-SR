from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Result:


   def __init__(self):
      '''  '''

      self.id = "resultId"
      self.value = "Result"
      self.isDisabled = True


   @property
   def Build(self):
      '''  '''

      return html.Div(id = "result")