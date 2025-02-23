from dash.dependencies import (Input, Output, State)
from ..config import (app, projectName, currentVersion)

class Header:


   def __init__(self):
      '''  '''

      self.titleOnLoadCallback()
      self.versionOnLoadCallback()


   def titleOnLoadCallback(self):
      '''  '''

      @app.callback(

         output = Output("headerTitle", "children"),
         inputs = Input("headerRowId", "children")

      )
      def func(titleValue): return projectName


   def versionOnLoadCallback(self):
      '''  '''

      @app.callback(

         output = Output("headerVersion", "children"),
         inputs = Input("headerRowId", "children")

      )
      def func(versionValue): return currentVersion