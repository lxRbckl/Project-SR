# we aren't doing the version functionality.
# in the header of the dashboard, it's going to say the project
# name and then the version of the project.

# follow fenaverat for basic functionality of UI
# think about how to implement backend algorithms <-
# view -> component -> callback -> controller(callback)


from dash_bootstrap_components import (
   Container
)
from dash import html


class Layout:

   
   def __init__(self):
      '''  '''

      pass


   @property
   def Build(self):
      '''  '''

      return Container(

         fluid = True,
         className = "layoutContainer",
         children = [

            html.H1("test")

         ]

      )