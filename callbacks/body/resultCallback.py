from config import app
from dash.dependencies import (Input, Output, State)


class Result:


   def __init__(self, notifier, stepsModel):
      """  """

      self.notifier = notifier
      self.stepsModel = stepsModel