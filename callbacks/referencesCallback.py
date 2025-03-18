from json import loads
from clipboard import copy
from os import (listdir, remove)
from dash import (Input, Output, State, ctx, ALL)

from config import (app, projectDirectory, iconCopy, iconTrash)


class References:


    def __init__(self, notifier, referencesModal):
        """  """

        self.referencesOnCopyCallback()
        self.referencesOnClickCallback()
        self.referencesOnDeleteCallback()

        self.notifier = notifier
        self.referencesModal = referencesModal

        self.referencesFilepath = "/assets/references"
        self.referencesCopyMessage = "Reference was copied to clipboard."
        self.referencesDeleteMessage = "Reference was deleted from folder."
        self.parseContext = lambda ctx: loads(ctx.triggered[0]["prop_id"].replace(".n_clicks", ""))


    def _buildReferences(self):
        """  """

        returnReferences = []
        for r in listdir(projectDirectory + self.referencesFilepath):

            name = r
            ref = f"{self.referencesFilepath}/{name}"

            returnReferences.append(self.referencesModal.addReference(name = name, reference = ref))

        return returnReferences


    def referencesOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            output = [

                Output("referencesModalId", "opened"),
                Output("referencesRowId", "children", allow_duplicate = True)

            ],
            inputs = Input("headerReferencesActionIconId", "n_clicks")

        )
        def func(referencesClick): return [True, self._buildReferences()]


    def referencesOnCopyCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input({"type" : "copy-btn", "index" : ALL}, "n_clicks"),
            output = Output("notificationDiv", "children", allow_duplicate = True)

        )
        def func(copyClick):

            if (len(ctx.triggered) == 1):

                reference = self.parseContext(ctx)["index"]
                copy(reference)

                return self.notifier.notify(

                    icon = iconCopy,
                    duration = 4000,
                    message = self.referencesCopyMessage

                )


    def referencesOnDeleteCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            state = State("referencesRowId", "children"),
            inputs = Input({"type" : "delete-btn", "index" : ALL}, "n_clicks"),
            output = [

                Output("referencesRowId", "children", allow_duplicate = True),
                Output("notificationDiv", "children", allow_duplicate = True)

            ]

        )
        def func(deleteClick, referencesChildren):

            if (len(ctx.triggered) == 1):

                file = self.parseContext(ctx)["index"]
                remove(f"{projectDirectory + self.referencesFilepath}/{file}")

                return [

                    self._buildReferences(),
                    self.notifier.notify(

                        duration = 4000,
                        icon = iconTrash,
                        message = self.referencesDeleteMessage

                    )

                ]


            return [referencesChildren, None]


    def referencesOnUploadCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input("referencesUploadId", "contents"),
            output = Output("notificationDiv", "children", allow_duplicate = True)

        )
        def func(uploadContent):

            print(uploadContent)