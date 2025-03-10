from dash.dependencies import (Input, Output, State)
from config import (app, projectName, currentVersion)

class Header:


   def __init__(self):
      """  """

      self.titleOnLoadCallback()
      self.versionOnLoadCallback()
      self.versionOnClickCallback()


   def titleOnLoadCallback(self):
      """  """

      @app.callback(

         output = Output("headerTitleH1Id", "children"),
         inputs = Input("headerRowId", "children")

      )
      def func(rowValue): return projectName


   def versionOnLoadCallback(self):
      """  """

      @app.callback(

         output = Output("headerVersionButtonId", "children"),
         inputs = Input("headerRowId", "children")

      )
      def func(rowValue): return currentVersion


   def versionOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         output = Output("guideModalId", "opened"),
         inputs = Input("headerVersionButtonId", "n_clicks")

      )
      def func(versionClick): return True