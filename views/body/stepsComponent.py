from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Steps:


    def __init__(self):
        """  """

        pass


    def _buildStep(self, step):
        """  """

        return dbc.Col(

            width = 12,
            children = html.H1("test")

        )


    def buildSteps(self, steps):
        """  """

        return [self._buildStep(s) for s in steps]
