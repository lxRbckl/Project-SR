from dash import html
import dash_bootstrap_components as dbc


class Body:


   def __init__(self, items):
      '''  '''

      self.items = items


   @property
   def Build(self): 
      '''  '''

      return dbc.Accordion(
         
         flush = True,
         children = self.items,
         className = "bodyAccordion"
         
      )
   

#    .section-expandable .section-expandable-title 

# padding:0;

# }