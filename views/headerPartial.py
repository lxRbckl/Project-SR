from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (projectName, iconGuide, iconMedia, iconSettings)


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
                  className = "headerGroup",
                  children = [

                     # (settings, references, guide) <
                     dmc.ActionIcon(

                        disabled = True,
                        id = "headerSettingsActionIconId",
                        children = DashIconify(icon = iconSettings, width = 20)

                     ),
                     dmc.ActionIcon(

                        id = "headerReferencesActionIconId",
                        className = "headerReferencesActionIcon",
                        children = DashIconify(icon = iconMedia, width = 20)

                     ),
                     dmc.ActionIcon(

                        id = "headerGuideActionIconId",
                        className = "headerGuideActionIcon",
                        children = DashIconify(icon = iconGuide, width = 20)

                     )

                     # >

                  ]

               )

            )

         ]

      )