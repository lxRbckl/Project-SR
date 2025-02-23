from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Documentation:


   def __init__(self):
      '''  '''

      pass


   @property
   def Build(self):
      '''  '''

      return dmc.Modal(

         size = "85%",
         opened = None,
         centered = True,
         title = "Documentation",
         id = "documentationModalId",
         className = "documentationModal"

      )