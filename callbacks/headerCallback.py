from config import app
from dash.dependencies import (Input, Output, State)


class Header:


   def __init__(self):
      """  """

      self.guideOnClickCallback()
      self.referencesOnClickCallback()


   def referencesOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("headerReferencesButtonId", "n_clicks"),
         output = Output("referencesModalId", "opened", allow_duplicate = True)

      )
      def func(referencesClick): return True


   def guideOnClickCallback(self):
      """  """

      @app.callback(

         prevent_initial_call = True,
         inputs = Input("headerGuideButtonId", "n_clicks"),
         output = Output("guideModalId", "opened", allow_duplicate = True)

      )
      def func(guideClick): return True