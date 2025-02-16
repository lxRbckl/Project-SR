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

         children = self.items,
         id = "bodyAccordionId",
         className = "bodyAccordion"

      )