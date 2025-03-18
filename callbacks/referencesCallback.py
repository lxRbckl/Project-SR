import base64
from time import sleep
from json import loads
from clipboard import copy
from os import (remove, listdir)
from dash import (Input, Output, State, ctx, ALL)

from config import (

    app,
    iconCopy,
    iconTrash,
    iconSuccess,
    referencesFilepath,
    referencesCompleteFilepath

)


class References:


    def __init__(self, notifier, referencesModal):
        """  """

        self.copyOnClickCallback()
        self.deleteOnClickCallback()
        self.uploadOnContentCallback()
        self.referencesOnClickCallback()

        self.notifier = notifier
        self.referencesModal = referencesModal

        self.onUploadSleep = 0.5
        self.onDeleteSleep = 0.5
        self.copyMessageSuccess = "Reference was copied to clipboard."
        self.deleteMessageSuccess = "Reference was deleted from folder."
        self.getReferences = lambda : listdir(referencesCompleteFilepath)
        self.uploadMessageSuccess = lambda u: f"Reference {u} was uploaded successfully."
        self.parseContext = lambda c: loads(c.triggered[0]["prop_id"].replace(".n_clicks", ""))


    def _buildReferences(self):
        """  """

        returnReferences = []
        for r in getReferences():

            name = r
            ref = f"{referencesFilepath}/{name}"

            returnReferences.append(self.referencesModal.addReference(name = name, reference = ref))

        return returnReferences


    def referencesOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input("headerReferencesActionIconId", "n_clicks"),
            output = [

                Output("referencesModalId", "opened"),
                Output("referencesRowId", "children", allow_duplicate = True)

            ]

        )
        def func(referencesClick): return [True, self._buildReferences()]


    def copyOnClickCallback(self):
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
                    message = self.copyMessageSuccess

                )


    def deleteOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            state = State("referencesRowId", "children"),
            inputs = Input({"type" : "delete-btn", "index" : ALL}, "n_clicks"),
            running = [

                (Output("referencesLoadingOverlayId", "visible"), True, False)

            ],
            output = [

                Output("referencesRowId", "children", allow_duplicate = True),
                Output("notificationDiv", "children", allow_duplicate = True)

            ]

        )
        def func(deleteClick, referencesChildren):

            if (len(ctx.triggered) == 1):

                file = self.parseContext(ctx)["index"]
                remove(f"{referencesCompleteFilepath}/{file}")

                sleep(self.onDeleteSleep)
                return [

                    self._buildReferences(),
                    self.notifier.notify(

                        duration = 4000,
                        icon = iconTrash,
                        message = self.deleteMessageSuccess

                    )

                ]

            return [referencesChildren, None]


    def uploadOnContentCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            state = State("referencesUploadId", "filename"),
            inputs = Input("referencesUploadId", "contents"),
            running = [

                (Output("referencesLoadingOverlayId", "visible"), True, False)

            ],
            output = [

                Output("referencesRowId", "children", allow_duplicate = True),
                Output("notificationDiv", "children", allow_duplicate = True)

            ]

        )
        def func(uploadContents, uploadFilenames):

            returnNotifications = []
            for file, content in zip(uploadFilenames, uploadContents):

                data = content.encode("utf-8").split(b";base64,")[1]
                with open(f"{referencesCompleteFilepath}/{file}", "wb") as f:

                    f.write(base64.b64decode(data))

                returnNotifications.append(self.notifier.notify(

                    duration = 4000,
                    icon = iconSuccess,
                    message = self.uploadMessageSuccess(file)

                ))

            sleep(self.onUploadSleep)
            return [self._buildReferences(), returnNotifications]

