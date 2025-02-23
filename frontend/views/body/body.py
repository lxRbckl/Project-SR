from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Body:


   def __init__(self, items):
      '''  '''

      self.items = items


   @property
   def Build(self): 
      '''  '''

      return dmc.Accordion(

         value = None,
         id = "bodyAccordionId",
         transitionDuration = 300,
         children = [

            dmc.AccordionItem(

               id = item.id,
               value = item.value,
               className = "bodyAccordionItem",
               children = [

                  dmc.AccordionControl(

                     children = item.value,
                     className = "bodyAccordionControl"

                  ),
                  dmc.AccordionPanel(

                     children = item.Build,
                     className = "bodyAccordionPanel"

                  )

               ]

            )

         for item in self.items]

      )