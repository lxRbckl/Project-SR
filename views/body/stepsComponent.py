from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Steps:

    def __init__(self):
        """  """

        pass

    @property
    def build(self):
        """  """

        return list([html.Div(
            children = html.H1("step")
        )])
