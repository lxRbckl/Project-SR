from dash import (html, dcc)
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_mantine_components import ActionIcon

from config import (iconTrash, iconUpload, iconCopy)


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
                    children = self.addDragNDrop()

                ),
                dbc.Row(

                    children = None,
                    id = "referencesRowId",
                    className = "referencesImagesRow"

                )

                # >

            ]

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

                                # (copy, title), delete <
                                dmc.Group(

                                    gap = 5,
                                    children = [

                                        dmc.ActionIcon(

                                            size = "sm",
                                            children = DashIconify(icon = iconCopy),
                                            id = {"type" : "copy-btn", "index" : name}

                                        ),
                                        html.Small(children = name)

                                    ]

                                ),
                                dmc.ActionIcon(

                                    size = "sm",
                                    children = DashIconify(icon = iconTrash),
                                    id = {"type" : "delete-btn", "index" : name}

                                )

                                # >

                            ]

                        )

                    ),
                    dmc.CardSection(children = dmc.Image(src = reference))

                ]

            )

        )


    def addDragNDrop(self):
        """  """

        return dbc.Col(

            width = 12,
            children = dcc.Upload(

                contents = None,
                multiple = True,
                id = "referencesUploadId",
                children = dmc.Button(

                    size = "md",
                    fullWidth = True,
                    children = "Upload",
                    loaderProps = {"type": "dots"},
                    id = "referencesUploadButtonId",
                    leftSection = DashIconify(width = 25, icon = iconUpload)

                )

            )

        )