from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (emptyValue, buildOptions, iconCopy, iconPaste)


class Build:

    def __init__(self):
        """  """

        self.id = "buildId"
        self.value = "Build"
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

                        # input <
                        dmc.Textarea(

                            minRows = 5,
                            maxRows = 20,
                            error = None,
                            autosize = True,
                            disabled = False,
                            value = emptyValue,
                            autoComplete = "on",
                            id = "buildInputTextareaId",
                            className = "buildInputTextarea"

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

                            # (create, options) <
                            dmc.Button(

                                size = "xs",
                                disabled = None,
                                children = "Create",
                                id = "buildCreateButtonId",
                                loaderProps = {"type": "dots"},
                                className = "buildCreateButton"

                            ),
                            dmc.MultiSelect(

                                value = [],
                                size = "xs",
                                disabled = None,
                                clearable = True,
                                searchable = True,
                                data = buildOptions,
                                placeholder = "Options",
                                className = "buildMultiSelect",
                                id = "buildOptionsMultiSelectId"
                            ),

                            # >

                        ]

                    )

                ),
                dbc.Col(

                    width = "auto",
                    className = "colExtended",
                    children = [

                        # (copy, clear, paste) <
                        dmc.Button(

                            size = "xs",
                            disabled = None,
                            id = "buildCopyButtonId",
                            className = "buildCopyButton",
                            loaderProps = {"type": "dots"},

                            children = "Copy",
                            leftSection = DashIconify(

                                width = 20,
                                icon = iconCopy

                            )

                        ),
                        dmc.Button(

                            size = "xs",
                            disabled = None,
                            children = "Clear",
                            id = "buildClearButtonId",
                            className = "buildClearButton"

                        ),
                        dmc.Button(

                            size = "xs",
                            disabled = False,
                            id = "buildPasteButtonId",
                            className = "buildPasteButton",
                            loaderProps = {"type": "dots"},

                            children = "Paste",
                            rightSection = DashIconify(

                                width = 20,
                                icon = iconPaste

                            )

                        )

                        # >

                    ]

                )

                # >

            ]

        )
