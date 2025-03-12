from time import sleep
from clipboard import (copy, paste)

from dash.dependencies import (Input, Output, State)
from config import (app, emptyValue, iconCopy, iconPaste)


class Build:

    def __init__(self, notifier, stepsModel, stepsComponent):
        """  """

        self.clearOnClickCallback()
        self.createOnClickCallback()
        self.clearOnDisabledCallback()
        self.textareaOnInputCallback()
        self.clipboardOnClickCallback()

        self.redirectTo = "Run"
        self.notifier = notifier
        self.stepsModel = stepsModel
        self.stepsComponent = stepsComponent

    def textareaOnInputCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = False,
            inputs = Input("buildInputTextareaId", "value"),
            output = Output("buildCreateButtonId", "disabled")

        )
        def func(textareaValue): return (textareaValue == emptyValue)

    def createOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input("buildCreateButtonId", "n_clicks"),
            output = [

                Output("bodyAccordionId", "value", allow_duplicate = True),
                Output("runStepsStackId", "children", allow_duplicate = True),
                Output("buildInputTextareaId", "error", allow_duplicate = True)

            ],
            state = [

                State("bodyAccordionId", "value"),
                State("runStepsStackId", "children"),
                State("buildInputTextareaId", "value")

            ],
            running = [

                (Output("buildCreateButtonId", "loading"), True, False),
                (Output("buildClearButtonId", "disabled"), True, False)

            ]

        )
        def func(createClick, accordionValue, stepsChildren, textareaValue):

            try:

                i = 0
                response = None
                textareaValues = [s for s in textareaValue.split("\n") if (len(s) > 0)]
                while ((response == None) and (len(textareaValues) != i)):

                    response = self.stepsModel.addStep(textareaValues[i])
                    i += 1

                    print(type(stepsChildren))  # remove
                    print(type(self.stepsComponent.build))  # remove

                    if (response):
                        return [accordionValue, stepsChildren, response]
                    else:
                        return [self.redirectTo, None, None]

            except ValueError: return [accordionValue, stepsChildren, "Invalid notation."]

    def clearOnDisabledCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input("buildCreateButtonId", "disabled"),
            output = [

                Output("buildCopyButtonId", "disabled", allow_duplicate = True),
                Output("buildInputTextareaId", "error", allow_duplicate = True),
                Output("buildClearButtonId", "disabled", allow_duplicate = True),
                Output("buildOptionsMultiSelectId", "disabled", allow_duplicate = True)

            ]

        )
        def func(createDisabled): return [createDisabled, None, createDisabled, createDisabled]

    def clipboardOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            state = State("buildInputTextareaId", "value"),
            inputs = [

                Input("buildCopyButtonId", "n_clicks"),
                Input("buildPasteButtonId", "n_clicks")

            ],
            running = [

                (Output("buildPasteButtonId", "disabled"), True, False),
                (Output("buildClearButtonId", "disabled"), True, False),
                (Output("buildCopyButtonId", "disabled"), True, False)

            ],
            output = [

                Output("notificationDiv", "children", allow_duplicate = True),
                Output("buildInputTextareaId", "value", allow_duplicate = True),
                Output("buildCopyButtonId", "n_clicks", allow_duplicate = True),
                Output("buildPasteButtonId", "n_clicks", allow_duplicate = True),

            ]

        )
        def func(copyClick, pasteClick, inputValue):

            sleep(0.3)

            # if (copy) <
            # else (then paste) <
            if (copyClick):

                icon = iconCopy
                copy(inputValue)
                text = inputValue
                message = "Text was copied from input."

            else:

                text = paste()
                icon = iconPaste
                message = "Text was pasted from input."

            # >

            return [

                self.notifier.notify(icon = icon, duration = 5000, message = message),
                text,
                None,
                None

            ]


    def clearOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input("buildClearButtonId", "n_clicks"),
            output = [

                Output("buildInputTextareaId", "value", allow_duplicate = True),
                Output("buildOptionsMultiSelectId", "value", allow_duplicate = True)

            ]

        )
        def func(clearClick): return [emptyValue, None]
