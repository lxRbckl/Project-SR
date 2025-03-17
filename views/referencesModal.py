from dash import (html, dcc)
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_mantine_components import ActionIcon

from config import (iconTrash, iconMedia, iconUpload)


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
            children = [

                # upload <
                # images <
                dbc.Row(

                    justify = "start",
                    children = dbc.Col(

                        width = "auto",
                        className = "",
                        children = dcc.Upload(

                            children = dmc.Button(

                                size = "md",
                                children = "Upload",
                                leftSection = DashIconify(

                                    width = 30,
                                    icon = iconUpload

                                )

                            )

                        )

                    )

                ),
                dbc.Row(

                    children = None,
                    id = "referencesRowId",
                    className = "referencesImagesRow"

                )

                # >

            ]

        )


    def _buildReferenceCard(self, children, withBorder = True):
        """  """

        return dbc.Col(

            width = self.referenceWidth,
            className = "referencesCol",
            children = dmc.Card(

                children = children,
                withBorder = withBorder,
                className = "referencesCard"

            )

        )


    def addReference(self, name, reference):
        """  """

        return dbc.Col(

            width = self.referenceWidth,
            className = "referencesCol",
            children = dmc.Card(

                withBorder = True,
                className = "referencesCard",
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