from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (projectName, iconImage, iconGuide)


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
               children = [

                  html.H1(

                     children = projectName,
                     className = "headerTitleH1"

                  )

               ]

            ),
            dbc.Col(

               align = "end",
               width = "auto",
               className = "colExtended",
               children = dmc.Group(

                  gap = 0,
                  children = [

                     # (references, guide) <
                     dmc.Button(

                        size = "xs",
                        id = "headerReferencesButtonId",
                        className = "headerReferencesButton",
                        children = DashIconify(

                           width = 25,
                           icon = iconImage

                        )

                     ),
                     dmc.Button(

                        size = "xs",
                        id = "headerGuideButtonId",
                        className = "headerGuideButton",
                        children = DashIconify(

                           width = 25,
                           icon = iconGuide

                        )

                     )

                     # >

                  ]

               )

            )

         ]

      )