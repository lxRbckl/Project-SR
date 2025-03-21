from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (emptyValue, iconCopy, iconPaste, loaderStyle, iconOptions)


class Build:

    def __init__(self):
        """  """

        self.id = "buildId"
        self.value = "Build"
        self.isDisabled = False

        self.options = [

            "Ignore Alerts"

        ]


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
                            # value = emptyValue, # uncomment
                            value = "find text 3, alert, pause\nclick 2, pause\nkeyboard this is a message, alert\nfind text 3, alert, pause\nclick 2, pause\nkeyboard this is a message, alert\nfind text 3, alert, pause\nclick 2, pause\nkeyboard this is a message, alert\nfind text 3, alert, pause\nclick 2, pause\nkeyboard this is a message, alert\n", # remove
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
                                loaderProps = loaderStyle,
                                id = "buildCreateButtonId",
                                className = "buildCreateButton"

                            ),
                            dmc.MultiSelect(

                                value = [],
                                size = "xs",
                                disabled = None,
                                clearable = True,
                                searchable = True,
                                data = self.options,
                                placeholder = "Options",
                                id = "buildOptionsMultiSelectId",
                                className = "buildOptionsMultiSelect",
                                leftSection = DashIconify(icon = iconOptions)
                            )

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
                            children = "Copy",
                            id = "buildCopyButtonId",
                            loaderProps = loaderStyle,
                            className = "buildCopyButton",
                            leftSection = DashIconify(

                                width = 18,
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
                            children = "Paste",
                            id = "buildPasteButtonId",
                            loaderProps = loaderStyle,
                            className = "buildPasteButton",
                            rightSection = DashIconify(

                                width = 18,
                                icon = iconPaste

                            )

                        )

                        # >

                    ]

                )

                # >

            ]

        )
