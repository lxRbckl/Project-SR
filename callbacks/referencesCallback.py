from config import (app, projectDirectory)

from os import (listdir, remove)
from dash import (Input, Output, State, ctx, ALL)


class References:


    def __init__(self, notifier, referencesModal):
        """  """

        self.referencesOnClickCallback()
        self.referencesOnDeleteCallback()

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
            output = [

                Output("referencesModalId", "opened"),
                Output("referencesRowId", "children", allow_duplicate = True)

            ],
            inputs = Input("headerReferencesActionIconId", "n_clicks")

        )
        def func(referencesClick): return [True, self._buildReferences()]


    def referencesOnDeleteCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input({"type" : "delete-btn", "index" : ALL}, "n_clicks"),
            output = Output("referencesRowId", "children", allow_duplicate = True)

        )
        def func(deleteClick):
            print(ctx.triggered_id) # remove
            print() # remove

            if (ctx.triggered): print(ctx.triggered, "TRIGGERED") # remove

            return self._buildReferences()