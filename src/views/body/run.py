from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Run:


   def __init__(self):
      '''  '''

      pass


   @property
   def Build(self):
      '''  '''

      return dmc.AccordionItem(

         id = "runId",
         value = "Run",
         className = "bodyAccordionItem",
         children = [

            dmc.AccordionControl(
               
               children = "Run",
               className = "bodyAccordionControl"
               
            ),
            dmc.AccordionPanel(
               
               children = [



               ]
               
            )

         ]

      )