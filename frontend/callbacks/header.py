from dash.dependencies import (Input, Output, State)
from ..config import (app, projectName, currentVersion)

class Header:


   def __init__(self):
      '''  '''

      self.titleCallback()
      self.versionCallback()


   def titleCallback(self):
      '''  '''

      @app.callback(

         output = Output("headerTitle", "children"),
         inputs = [Input("headerColTitleId", "children")]

      )
      def func(arg): return projectName


   def versionCallback(self):
      '''  '''

      @app.callback(

         output = Output("headerVersion", "children"),
         inputs = [Input("headerColVersionId", "children")]

      )
      def func(arg): return currentVersion