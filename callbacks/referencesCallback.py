from time import sleep
from json import loads
from os.path import join
from clipboard import copy
from base64 import b64decode
from dash import (Input, Output, State, ctx, ALL)
from os import (remove, listdir, makedirs, startfile)

from config import (

    app,
    iconCopy,
    iconError,
    iconTrash,
    iconSuccess,
    referencesParentDir,
    referencesChildSubDir,
    referencesChildFullDir

)


class References:


    def __init__(self, notifier, referencesModal):
        """  """

        self.folderOnClickCallback()
        self.exportOnClickCallback()
        self.importOnClickCallback()

        self.copyOnClickCallback()
        self.deleteOnClickCallback()
        self.uploadOnContentCallback()
        self.referencesOnClickCallback()

        self.notifier = notifier
        self.referencesModal = referencesModal

        self.onUploadSleep = 0.5
        self.onDeleteSleep = 0.5
        self.referenceTitles = []
        self.exportMessageSuccess = "Export was successful."
        self.importMessageSuccess = "Import was successful."
        self.copyMessageSuccess = "Reference was copied to clipboard."
        self.deleteMessageSuccess = "Reference was deleted from folder."
        self.uploadMessageFailure = lambda r: f"The reference {r} already exists!"
        self.uploadMessageSuccess = lambda r: f"The reference {r} was uploaded successfully."
        self.parseContext = lambda c: loads(c.triggered[0]["prop_id"].replace(".n_clicks", ""))["index"]


    def _parentHasReferences(self): return (len(listdir(referencesParentDir)) > 0)
    def _childHasReferences(self): return (len(listdir(referencesChildFullDir)) > 0)


    def _buildReferences(self):
        """  """

        self.referenceTitles = listdir(referencesChildFullDir)
        return [

            self.referencesModal.addReference(

                name = ref,
                ref = join(referencesChildSubDir, ref)

            )

        for ref in self.referenceTitles]


    def referencesOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input("headerReferencesActionIconId", "n_clicks"),
            output = [

                Output("referencesImportButtonId", "n_clicks", allow_duplicate = True),
                Output("referencesExportButtonId", "n_clicks", allow_duplicate = True),
                Output("referencesRowId", "children", allow_duplicate = True),
                Output("referencesModalId", "opened")
            ]

        )
        def func(referencesClick):

            makedirs(referencesChildFullDir, exist_ok = True)
            makedirs(referencesParentDir, exist_ok = True)
            return [0, 0, self._buildReferences(), True]


    def copyOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input({"type" : "copy-btn", "index" : ALL}, "n_clicks"),
            output = Output("notificationDiv", "children", allow_duplicate = True)

        )
        def func(copyClick):

            rNotificationChildren = None

            if ((len(ctx.triggered) == 1) and (copyClick.count(True) > 0)):

                reference = self.parseContext(ctx)
                copy(reference)

                rNotificationChildren = self.notifier.notify(

                    icon = iconCopy,
                    message = self.copyMessageSuccess

                )

            return rNotificationChildren


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

            rNotificationChildren = []

            if ((len(ctx.triggered) == 1) and (deleteClick.count(True) > 0)):

                file = self.parseContext(ctx)
                remove(join(referencesChildFullDir, file))
                rNotificationChildren.append(self.notifier.notify(

                    icon = iconTrash,
                    message = self.deleteMessageSuccess

                ))

            return [self._buildReferences(), rNotificationChildren]


    def uploadOnContentCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            state = State("referencesUploadId", "filename"),
            inputs = Input("referencesUploadId", "contents"),
            output = [

                Output("referencesRowId", "children", allow_duplicate = True),
                Output("notificationDiv", "children", allow_duplicate = True)

            ],
            running = (Output("referencesLoadingOverlayId", "visible"), True, False)


        )
        def func(uploadContents, uploadFilenames):

            returnNotifications = []
            for filename, content in zip(uploadFilenames, uploadContents):

                if (filename not in self.referenceTitles):

                    data = content.encode("utf-8").split(b";base64,")[1]
                    with open(join(referencesChildFullDir, filename), "wb") as f:

                        f.write(b64decode(data))

                    returnNotifications.append(self.notifier.notify(

                        icon = iconSuccess,
                        message = self.uploadMessageSuccess(filename)

                    ))

                else: returnNotifications.append(self.notifier.notify(

                    color = "red",
                    icon = iconError,
                    message = self.uploadMessageFailure(filename)

                ))

            sleep(self.onUploadSleep)
            return [self._buildReferences(), returnNotifications]


    def folderOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input("referencesFolderButtonId", "n_clicks"),
            output = Output("referencesFolderButtonId", "disabled")

        )
        def func(folderClick):

            startfile(referencesParentDir)
            return False


    def importOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            state = State("referencesRowId", "children"),
            inputs = Input("referencesImportButtonId", "n_clicks"),
            running = (Output("referencesLoadingOverlayId", "visible"), True, False),
            output = [

                Output("notificationDiv", "children", allow_duplicate = True),
                Output("referencesRowId", "children", allow_duplicate = True),
                Output("referencesImportButtonId", "disabled", allow_duplicate = True)

            ]

        )
        def func(importClick, referencesChildren):

            rNotificationChidlren = None
            rReferencesChildren = referencesChildren
            print('import', ctx.triggered, importClick, 'end')

            if (len(ctx.triggered) == 1 and importClick > 0):

                print('IMPORT EXECUTING')
                rReferencesChildren = self._buildReferences()
                rNotificationChidlren = self.notifier.notify(self.importMessageSuccess)

            return [rNotificationChidlren, rReferencesChildren, (not self._parentHasReferences())]


    def exportOnClickCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input("referencesExportButtonId", "n_clicks"),
            running = (Output("referencesLoadingOverlayId", "visible"), True, False),
            output = [

                Output("notificationDiv", "children", allow_duplicate = True),
                Output("referencesExportButtonId", "disabled", allow_duplicate = True)

            ]

        )
        def func(exportClick):

            rNotificationChildren = None
            print('export', ctx.triggered, exportClick, 'end')

            if (len(ctx.triggered) == 1 and exportClick > 0):

                print('EXPORT EXECUTING')
                rNotificationChildren = self.notifier.notify(self.exportMessageSuccess)

            return [rNotificationChildren, (not self._childHasReferences())]


# import shutil
# import os
#
# # Define the source and destination paths
# source_path = '/path/to/source/folder/file.txt'
# destination_path = '/path/to/destination/folder/file.txt'
#
# # Copy the file
# shutil.copy(source_path, destination_path)