from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (layoutColWidth, notificationPosition)


class Layout:

   
   def __init__(self, notifier, guide, header, body, footer):
      """  """

      self.body = body
      self.guide = guide
      self.footer = footer
      self.header = header
      self.notifier = notifier


   @property
   def build(self):
      """  """

      return dmc.MantineProvider(

         children = [

            dmc.Center(

               className = "layoutCenter",
               children = dbc.Col(

                  width = layoutColWidth,
                  children = [

                     self.notifier.build,
                     self.guide.build,
                     self.header.build,
                     self.body.build,
                     self.footer.build

                  ]

               )

            )

         ]

      )