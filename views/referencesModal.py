from config import iconTrash

from dash import (html, dcc)
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class References:


    def __init__(self):
        """  """

        self.referenceWidth = 4


    @property
    def build(self):
        """  """

        return dmc.Modal(

            size = "75%",
            opened = None,
            centered = True,
            title = "References",
            id = "referencesModalId",
            closeOnClickOutside = False,
            children = dbc.Row(children = None, id = "referencesRowId")

        )


    def addReference(self, name, reference):
        """  """

        return dbc.Col(

            id = f"reference{name}Id",
            width = self.referenceWidth,
            className = "referencesCol",
            children = dmc.Card(

                withBorder = True,
                children = [

                    dmc.CardSection(

                        withBorder = True,
                        className = "referencesCardHeader",
                        children = dmc.Group(

                            justify = "space-between",
                            children = [

                                html.Small(children = name),
                                dmc.ActionIcon(

                                    size = "sm",
                                    children = DashIconify(icon = iconTrash),
                                    id = {"type" : "delete-btn", "index" : name}

                                )

                            ]

                        )

                    ),
                    dmc.CardSection(children = dmc.Image(src = reference))

                ]

            )

        )


    def addDragNDrop(self):
        """  """

        return None