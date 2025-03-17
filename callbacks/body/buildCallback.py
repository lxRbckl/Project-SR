from time import sleep
from clipboard import (copy, paste)

from dash.dependencies import (Input, Output, State)
from config import (app, emptyValue, iconCopy, iconPaste, iconWarning)


class Build:


    def __init__(self, notifier, controller, stepsModel, stepsComponent):
        """  """

        self.clearOnClickCallback()
        self.createOnClickCallback()
        self.clearOnDisabledCallback()
        self.textareaOnInputCallback()
        self.clipboardOnClickCallback()

        self.notifier = notifier
        self.controller = controller
        self.stepsModel = stepsModel
        self.stepsComponent = stepsComponent

        self.redirectTo = "Run"
        self.clipboardPause = 0.3
        self.clipboardNotifyDuration = 5000
        self.createInputErrorMessage = "Invalid notation."
        self.clipboardCopiedMessage = "Text was copied from input."
        self.clipboardPastedMessage = "Text was pasted from input."
        self.createOnClickMessage = "Make sure the correct window is selected!"


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
            state = [

                State("bodyAccordionId", "value"),
                State("runStepsStackId", "children"),
                State("buildInputTextareaId", "value")

            ],
            running = [

                (Output("buildCreateButtonId", "loading"), True, False),
                (Output("buildClearButtonId", "disabled"), True, False),
                (Output("runWindowSelectId", "disabled"), True, False)

            ],
            output = [

                Output("bodyAccordionId", "value", allow_duplicate = True),
                Output("runWindowSelectId", "value", allow_duplicate = True),
                Output("runStepsStackId", "children", allow_duplicate = True),
                Output("notificationDiv", "children", allow_duplicate = True),
                Output("buildInputTextareaId", "error", allow_duplicate = True)

            ]

        )
        def func(createClick, accordionValue, stepsChildren, textareaValue):

            rInputError = None
            rNotificationChildren = None
            rStepsChildren = stepsChildren
            rAccordionValue = accordionValue
            try:

                # iterate (steps) <
                # else (then success) <
                for step in [s for s in textareaValue.split("\n") if (len(s) > 0)]:

                    response = self.stepsModel.addStep(step)

                    if (response):

                        rInputError = response
                        break

                else:

                    rAccordionValue = self.redirectTo
                    rStepsChildren = self.stepsComponent.build
                    rNotificationChildren = self.notifier.notify(

                        duration = 1000, # remove

                        color = "yellow",
                        icon = iconWarning,
                        message = self.createOnClickMessage

                    )

                # >

            except ValueError: rInputError = self.createInputErrorMessage
            finally: return [rAccordionValue, None, rStepsChildren, rNotificationChildren, rInputError]



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

            sleep(self.clipboardPause)

            # if (copy) <
            # else (then paste) <
            if (copyClick):

                icon = iconCopy
                copy(inputValue)
                text = inputValue
                message = self.clipboardCopiedMessage

            else:

                text = paste()
                icon = iconPaste
                message = self.clipboardPastedMessage

            # >

            return [

                self.notifier.notify(icon = icon, duration = self.clipboardNotifyDuration, message = message),
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
