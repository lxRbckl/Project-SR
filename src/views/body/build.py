from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Build:


   def __init__(self):
      '''  '''

      pass


   @property
   def Build(self):
      '''  '''

      return dmc.AccordionItem(

         id = "buildId",
         value = "Build",
         className = "bodyAccordionItem",
         children = [

            dmc.AccordionControl(
               
               children = "Build", 
               className = "bodyAccordionControl"
               
            ),
            dmc.AccordionPanel(

               children = [



               ]

            )

         ]

      )