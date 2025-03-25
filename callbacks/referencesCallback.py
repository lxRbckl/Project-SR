from time import sleep
from json import loads
from os.path import join
from clipboard import copy
from base64 import b64decode
from os import (remove, listdir, makedirs)
from dash import (Input, Output, State, ctx, ALL)

from config import (app, iconCopy, iconTrash, iconSuccess, referencesChildDir, referencesParentDir)


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
        self.uploadMessageSuccess = lambda u: f"Reference {u} was uploaded successfully."
        self.parseContext = lambda c: loads(c.triggered[0]["prop_id"].replace(".n_clicks", ""))


    def _buildReferences(self):
        """  """

        return [

            self.referencesModal.addReference(

                name = ref,
                ref = join(referencesChildDir, ref)

            )

        for ref in listdir(referencesChildDir)]


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
        def func(referencesClick):

            makedirs(referencesChildDir, exist_ok = True)
            return [True, self._buildReferences()]


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

            input('deleteOnClickCallback()')

            rNotificationChildren = []
            for i, dc in enumerate(deleteClick):

                if (dc):

                    file = self.parseContext(ctx)["index"]
                    remove(join(referencesChildDir, file))

                    print('removed', file) # remove

                    rNotificationChildren.append(self.notifier.notify(

                        duration = 4000,
                        icon = iconTrash,
                        message = self.deleteMessageSuccess

                    ))

            return [self._buildReferences(), rNotificationChildren]



            # if (len(ctx.triggered) == 1):
            #
            #     file = self.parseContext(ctx)["index"]
            #     remove(join(referencesChildDir, file))
            #
            #     sleep(self.onDeleteSleep)
            #     return [
            #
            #         self._buildReferences(),
            #         self.notifier.notify(
            #
            #             duration = 4000,
            #             icon = iconTrash,
            #             message = self.deleteMessageSuccess
            #
            #         )
            #
            #     ]
            #
            # return [referencesChildren, None]


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

            input('uploadOnContentCallback()')

            returnNotifications = []
            for file, content in zip(uploadFilenames, uploadContents):

                data = content.encode("utf-8").split(b";base64,")[1]
                with open(join(referencesChildDir, file), "wb") as f:

                    f.write(b64decode(data))

                returnNotifications.append(self.notifier.notify(

                    duration = 4000,
                    icon = iconSuccess,
                    message = self.uploadMessageSuccess(file)

                ))

            sleep(self.onUploadSleep)
            return [self._buildReferences(), returnNotifications]