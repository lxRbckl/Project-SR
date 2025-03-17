from config import (app, projectDirectory)

from json import loads
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


    # def referencesOnCopyCallback(self):
    #     """  """
    #
    #     @app.callback(
    #
    #         prevent_initial_call = True,
    #         inputs = Input({}, "n_clicks"),
    #         output = Output("", "", allow_duplicate = True)
    #
    #     )


    def referencesOnDeleteCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = True,
            inputs = Input({"type" : "delete-btn", "index" : ALL}, "n_clicks"),
            output = Output("referencesRowId", "children", allow_duplicate = True)

        )
        def func(deleteClick):

            if (len(ctx.triggered) == 1):

                print(self.parseContext(ctx)) # remove

            return self._buildReferences()