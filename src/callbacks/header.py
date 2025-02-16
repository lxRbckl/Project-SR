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

         inputs = [Input("headerColTitle", "children")],
         output = Output("headerTitle", "children")

      )
      def func(arg): return projectName


   def versionCallback(self):
      '''  '''

      @app.callback(

         inputs = [Input("headerColVersion", "children")],
         output = Output("headerVersion", "children")

      )
      def func(arge): return currentVersion