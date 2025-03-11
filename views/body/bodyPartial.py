from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Body:


   def __init__(self, items):
      """  """

      self.items = items


   @property
   def build(self):
      """  """

      return dmc.Accordion(

         value = None,
         id = "bodyAccordionId",
         className = "bodyAccordion",
         children = [

            dmc.AccordionItem(

               id = item.id,
               value = item.value,
               className = "bodyAccordionItem",
               children = [

                  dmc.AccordionControl(

                     children = item.value,
                     disabled = item.isDisabled,
                     className = "bodyAccordionControl"

                  ),
                  dmc.AccordionPanel(

                     children = item.build,
                     className = "bodyAccordionPanel"

                  )

               ]

            )

         for item in self.items]

      )