from config import layoutColWidth

from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Layout:

   
   def __init__(self, guide, header, body, footer):
      """  """

      self.body = body
      self.guide = guide
      self.footer = footer
      self.header = header


   @property
   def build(self):
      """  """

      return dmc.MantineProvider(

         children = [

            dmc.NotificationProvider(),
            dmc.Center(

               className = "layoutCenter",
               children = dbc.Col(

                  width = layoutColWidth,
                  children = [

                     self.guide.build,
                     self.header.build,
                     self.body.build,
                     self.footer.build

                  ]

               )

            )

         ]

      )