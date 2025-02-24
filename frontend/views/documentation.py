from dash import (html, dcc)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Documentation:


   def __init__(self):
      '''  '''

      self.value = None
      self.filepath = "frontend/assets/data/documentation.md"

      with open(self.filepath, 'r') as fin:
         self.value = fin.read()


   @property
   def Build(self):
      '''  '''

      return dmc.Modal(

         size = "85%",
         opened = True,
         centered = True,
         title = "Documentation",
         id = "documentationModalId",
         className = "documentationModal",
         children = [

            dcc.Markdown(

               children = self.value,
               className = "documentationMarkdown"

            )

         ]

      )