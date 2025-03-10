from dash import (html, dcc)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Guide:


   def __init__(self):
      """  """

      self.value = None
      self.filepath = "./assets/data/guide.md"

      with open(self.filepath, 'r') as fin:
         self.value = fin.read()


   @property
   def build(self):
      """  """

      return dmc.Modal(

         size = "85%",
         opened = None,
         title = "Guide",
         centered = True,
         id = "guideModalId",
         closeOnClickOutside = False,
         children = [

            dcc.Markdown(

               children = self.value,
               className = "guideMarkdown"

            )

         ]

      )