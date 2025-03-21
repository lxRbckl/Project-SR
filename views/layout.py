from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Layout:

   
   def __init__(

       self,
       body,
       guide,
       header,
       footer,
       notifier,
       references

   ):
      """  """

      self.layoutColWidth = 9

      self.body = body
      self.guide = guide
      self.footer = footer
      self.header = header
      self.notifier = notifier
      self.references = references


   @property
   def build(self):
      """  """

      return dmc.MantineProvider(

         children = [

            dmc.Center(

               className = "layoutCenter",
               children = dbc.Col(

                  width = self.layoutColWidth,
                  children = [

                     self.notifier.build,
                     self.guide.build,
                     self.references.build,

                     self.header.build,
                     self.body.build,
                     self.footer.build

                  ]

               )

            )

         ]

      )