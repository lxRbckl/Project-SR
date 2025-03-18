from dash import (html, dcc)
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (iconTrash, iconUpload, iconCopy, loaderStyle)


class References:


    def __init__(self):
        """  """

        self.referenceColWidth = 4


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

                # loader <
                dmc.LoadingOverlay(

                    visible = False,
                    loaderProps = loaderStyle,
                    id = "referencesLoadingOverlayId",
                    overlayProps = {"radius": "sm", "blur": 2}

                ),

                # >

                # upload <
                # images <
                dbc.Row(

                    justify = "start",
                    children = dbc.Col(

                        width = 12,
                        children = dcc.Upload(

                            contents = None,
                            multiple = True,
                            id = "referencesUploadId",
                            children = dmc.Button(

                                size = "md",
                                fullWidth = True,
                                loaderProps = loaderStyle,
                                children = "Upload file(s)",
                                id = "referencesUploadButtonId",
                                leftSection = DashIconify(width = 25, icon = iconUpload)

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


    def addReference(self, name, reference):
        """  """

        return dbc.Col(

            className = "referencesCol",
            width = self.referenceColWidth,
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