from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Result:


   def __init__(self, notifier):
      """  """

      self.id = "resultId"
      self.value = "Result"
      self.isDisabled = True
      self.notifier = notifier


   @property
   def build(self):
      """  """

      return html.Div(id = "result")