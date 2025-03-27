from dash import (html, dcc)
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (iconTrash, iconUpload, iconCopy, loaderStyle, iconAlbum)


class References:


    def __init__(self):
        """  """

        self.referenceColWidth = 4
        self.folderMessage = "Reopen to fetch Import/Export updates"


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

                        # upload <
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

                        # >

                        # (import, folder, export) <
                        dbc.Col(

                            width = "auto",
                            children = dmc.Group(

                                gap = 0,
                                children = [

                                    dmc.Button(

                                        size = "xs",
                                        n_clicks = 0,
                                        disabled = None,
                                        children = "Import",
                                        loaderProps = loaderStyle,
                                        id = "referencesImportButtonId"

                                    ),
                                    dmc.Button(

                                        size = "xs",
                                        disabled = False,
                                        id = "referencesFolderButtonId",
                                        className = "referencesFolderButton",
                                        children = DashIconify(

                                            width = 20,
                                            icon = iconAlbum

                                        )

                                    ),
                                    dmc.Button(

                                        size = "xs",
                                        n_clicks = 0,
                                        disabled = None,
                                        children = "Export",
                                        loaderProps = loaderStyle,
                                        id = "referencesExportButtonId"

                                    )

                                ]

                            )

                        ),

                        # >

                        # description <
                        dbc.Col(

                            width = 12,
                            children = dmc.Text(

                                    size = "xs",
                                    children = self.folderMessage,
                                    className = "referencesDescriptionText"

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