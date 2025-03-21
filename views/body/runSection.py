from config import iconWindow

from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Run:


   def __init__(self):
      """  """

      self.id = "runId"
      self.value = "Run"
      self.isPaused = False
      self.isDisabled = False


   @property
   def build(self):
      """  """

      return dbc.Row(

         justify = "between",
         className = "rowExtended rowItemExtended",
         children = [

            dbc.Col(

               width = 12,
               className = "colExtended",
               children = [

                  # steps <
                  dbc.Row(

                     children = None,
                     id = "runStepsRowId",
                     className = "runStepsRow"

                  )

                  # >

               ]

            ),
            dbc.Col(

               width = "auto",
               className = "colExtended",
               children = dmc.Group(

                  gap = 0,
                  children = [

                     # (window, count, start, retry) <
                     dmc.Select(

                        size = "xs",
                        data = None,
                        value = None,
                        disabled = True,
                        clearable = True,
                        searchable = True,
                        placeholder = "Window",
                        id = "runWindowSelectId",
                        className = "runWindowSelect",
                        leftSection = DashIconify(icon =  iconWindow)

                     ),
                     dmc.Button(

                        size = "xs",
                        children = None,
                        disabled = True,
                        id = "runCountButtonId",
                        className = "runCountButton"

                     ),
                     dmc.Button(

                        size = "xs",
                        disabled = True,
                        children = "Start",
                        id = "runStartButtonId",
                        className = "runStartButton",
                        loaderProps = {"type" : "dots"}

                     ),
                     dmc.Button(

                        size = "xs",
                        disabled = True,
                        children = "Retry",
                        id = "runRetryButtonId",
                        className = "runRetryButton"

                     )

                     # >

                  ]

               )

            ),
            dbc.Col(

               width = "auto",
               className = "colExtended",
               children = [

                  # (continue, stop) <
                  dmc.Button(

                     size = "xs",
                     disabled = True,
                     children = "Continue",
                     id = "runContinueButtonId",
                     className = "runContinueButton"

                  ),
                  dmc.Button(

                     size = "xs",
                     disabled = True,
                     children = "Stop",
                     id = "runStopButtonId",
                     className = "runStopButton"

                  )

                  # >

               ]

            ),
            dbc.Col(

               width = 12,
               className = "colExtended",
               children = [

                  # progress <
                  dmc.Progress(

                     value = 0,
                     color = None,
                     id = "runProgressId",
                     className = "runProgress"

                  )

                  # >

               ]

            )

         ]

      )