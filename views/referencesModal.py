from config import currentVersion

from dash import (html, dcc)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class References:


    def __init__(self):
        """  """

        pass


    @property
    def build(self):
        """  """

        return dmc.Modal(

            size = "65%",
            opened = None,
            children = None,
            centered = True,
            title = f"References",
            id = "referencesModalId",
            closeOnClickOutside = False

        )