from dash.dependencies import (Input, Output)
from ..config import (app, projectName, currentVersion)

class Header:


   def __init__(self):
      '''  '''

      self.titleCallback()
      self.versionCallback()


   def titleCallback(self):
      '''  '''

      @app.callback(

         inputs = [Input("headerColTitleId", "children")],
         output = Output("headerTitle", "children")

      )
      def func(arg): return projectName


   def versionCallback(self):
      '''  '''

      @app.callback(

         inputs = [Input("headerColVersionId", "children")],
         output = Output("headerVersion", "children")

      )
      def func(arg): return currentVersion