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

            # > unclicked [{'prop_id': '{"index":"example112.png","type":"delete-btn"}.n_clicks', 'value': None}, {
            #     'prop_id': '{"index":"example2.png","type":"delete-btn"}.n_clicks', 'value': None}, {
            #     'prop_id': '{"index":"example212.png","type":"delete-btn"}.n_clicks', 'value': None}, {
            #     'prop_id': '{"index":"example22.png","type":"delete-btn"}.n_clicks', 'value': None}]
            #
            # > clicked [{'prop_id': '{"index":"example112.png","type":"delete-btn"}.n_clicks', 'value': 1}]

            # print('>', len(ctx.triggered), ctx.triggered) # remove
            # print() # remove

            if (len(ctx.triggered) == 1):

                print('ON PURPOSE') # remove

            return self._buildReferences()