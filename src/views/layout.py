# we aren't doing the version functionality.
# in the header of the dashboard, it's going to say the project
# name and then the version of the project.

# follow fenaverat for basic functionality of UI
# think about how to implement backend algorithms <-
# view -> component -> callback -> controller(callback)


from .body import Body
from .header import Header
from .footer import Footer
from ..config import columnWidth

from dash import html
import dash_bootstrap_components as dbc


class Layout:

   
   def __init__(self):
      '''  '''

      self.body = Body()
      self.header = Header()
      self.footer = Footer()


   @property
   def Build(self):
      '''  '''

      return dbc.Row(

         justify = "center",
         className = "layoutRow",
         children = dbc.Col(

            width = columnWidth,
            children = [

               self.header.Build,
               self.body.Build,
               self.footer.Build

            ]

         )

      )