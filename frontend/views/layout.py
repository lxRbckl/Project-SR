from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from ..config import columnWidth
from .body.run import Run as runView
from .body.body import Body as bodyView
from .header import Header as headerView
from .footer import Footer as footerView
from .body.build import Build as buildView
from ..callbacks.body.run import Run as runCallback
from ..callbacks.body.body import Body as bodyCallback
from ..callbacks.header import Header as headerCallback
from ..callbacks.footer import Footer as footerCallback
from ..callbacks.body.build import Build as buildCallback
from ..callbacks.body.instruction import Instruction as instructionCallback

class Layout:

   
   def __init__(self):
      '''  '''

      self.colChildren = None


   def RegisterViews(self):
      '''  '''

      self.colChildren = [

         headerView().Build,
         bodyView(items = [

            buildView(),
            runView()
            
         ]).Build,
         footerView().Build

      ]


   def RegisterCallbacks(self):
      '''  '''

      headerCallback()

      runCallback()
      bodyCallback()
      buildCallback()
      instructionCallback()
      
      footerCallback()


   @property
   def Build(self):
      '''  '''

      return dmc.MantineProvider(

         children = dbc.Row(

            justify = "center",
            className = "layoutRow",
            children = dbc.Col(

               width = columnWidth,
               children = self.colChildren

            )

         )

      )