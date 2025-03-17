from config import (app, projectDirectory)

from os import (listdir, remove)
from dash import (Input, Output, State, ctx, ALL)


class References:


    def __init__(self, notifier, referencesModal):
        """  """

        self.referencesOnClickCallback()
        self.ReferencesOnDeleteCallback()

        self.notifier = notifier
        self.referencesModal = referencesModal

        self.referencesFilepath = "/assets/references"


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
            inputs = Input("headerReferencesActionIconId", "n_clicks"),
            output = [

                Output("referencesRowId", "children", allow_duplicate = True),
                Output("referencesModalId", "opened", allow_duplicate = True)

            ]

        )
        def func(referencesClick): return [self._buildReferences(), True]


    def ReferencesOnDeleteCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input({"type" : "delete-btn", "index" : ALL}, "n_clicks"),
            output = Output("referencesRowId", "children", allow_duplicate = True)

        )
        def func(delete):

            print(ctx.triggered_id) # remove

            return self._buildReferences()