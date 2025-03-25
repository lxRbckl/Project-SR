from dash import (html, dcc)
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (iconTrash, iconUpload, iconCopy, iconMedia, loaderStyle, iconFolder)


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

                dbc.Row(

                    justify = "between",
                    children = [

                        # (upload, (icon, load, backup) <
                        dbc.Col(

                            width = "auto",
                            children = dcc.Upload(

                                contents = None,
                                multiple = True,
                                id = "referencesUploadId",
                                children = dmc.Button(

                                    size = "xs",
                                    children = "Upload",
                                    loaderProps = loaderStyle,
                                    id = "referencesUploadButtonId",
                                    leftSection = DashIconify(width = 20, icon = iconUpload)

                                )

                            )

                        ),
                        dbc.Col(

                            width = "auto",
                            children = dmc.Group(

                                gap = 0,
                                children = [

                                    dmc.Button(

                                        size = "xs",
                                        className = "referencesFolderButton",
                                        children = DashIconify(

                                            width = 16,
                                            icon = iconFolder

                                        )

                                    ),
                                    dmc.Button(

                                        size = "xs",
                                        children = "Load",
                                        loaderProps = loaderStyle,
                                        id = "referencesLoadButtonId",
                                        className = "referencesLoadButton"

                                    ),
                                    dmc.Button(

                                        size = "xs",
                                        children = "Backup",
                                        loaderProps = loaderStyle,
                                        id = "referencesBackupButtonId",
                                        className = "referencesBackupButton"

                                    )

                                ]

                            )

                        )

                        # >

                    ]

                ),
                dbc.Row(

                    children = None,
                    id = "referencesRowId",
                    className = "referencesImagesRow"

                )

                # >

            ]

        )


    def addReference(self, name, ref):
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

                                # (copy, title, delete) <
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
                    dmc.CardSection(children = dmc.Image(src = ref))

                ]

            )

        )