from dash import (html, dcc)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (guideFile, projectVersion)


class Guide:


   def __init__(self):
      """  """

      self.filedata = None
      with open(guideFile, 'r') as fin: self.filedata = fin.read()


   @property
   def build(self):
      """  """

      return dmc.Modal(

         size = "75%",
         opened = None,
         centered = True,
         id = "guideModalId",
         closeOnClickOutside = False,
         title = f"Guide - {projectVersion}",
         children = dcc.Markdown(children = self.filedata, className = "guideMarkdown")

      )