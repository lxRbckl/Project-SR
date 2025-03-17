from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (projectName, iconVersion)


class Header:


   def __init__(self):
      """  """

      pass


   @property
   def build(self):
      """  """

      return dbc.Row(

         id = "headerRowId",
         justify = "between",
         className = "rowExtended",
         children = [

            dbc.Col(

               width = "auto",
               className = "colExtended",
               children = dmc.Group(

                  gap = 0,
                  className = "headerGroup",
                  children = [

                     # (icon, title) <
                     # dmc.Image(
                     #
                     #    src = "/assets/favicon.ico",
                     #    className = "headerIconImage"
                     #
                     # ),
                     html.H1(

                        children = projectName,
                        className = "headerTitleH1"

                     )

                     # >

                  ]

               )

            ),
            dbc.Col(

               align = "end",
               width = "auto",
               className = "colExtended",
               children = [

                  # version <
                  dmc.Button(

                     size = "xs",
                     id = "headerVersionButtonId",
                     className = "headerVersionButton",
                     children = DashIconify(

                        width = 25,
                        icon = iconVersion

                     )

                  )

                  # >

               ]

            )

         ]

      )