# we aren't doing the version functionality.
# in the header of the dashboard, it's going to say the project
# name and then the version of the project.

# follow fenaverat for basic functionality of UI
# think about how to implement backend algorithms <-
# view -> component -> callback -> controller(callback)


from dash import html
import dash_bootstrap_components as dbc

from ..config import columnWidth
from .body.body import Body as bodyView
from .header import Header as headerView
from .footer import Footer as footerView
from ..callbacks.body.body import Body as bodyCallback
from ..callbacks.header import Header as headerCallback
from ..callbacks.footer import Footer as footerCallback

class Layout:

   
   def __init__(self):
      '''  '''

      self.colChildren = None


   def RegisterViews(self):
      '''  '''

      self.colChildren = [

         headerView().Build,
         bodyView().Build,
         footerView().Build

      ]


   def RegisterCallbacks(self):
      '''  '''

      headerCallback()
      bodyCallback()
      footerCallback()


   @property
   def Build(self):
      '''  '''

      return dbc.Row(

         justify = "center",
         className = "layoutRow",
         children = dbc.Col(

            width = columnWidth,
            children = self.colChildren

         )

      )