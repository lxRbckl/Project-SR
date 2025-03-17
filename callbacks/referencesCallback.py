from config import (app, projectDirectory)

from os import (listdir, remove)
from dash.dependencies import (Input, Output, State)


class References:


    def __init__(self, referencesModal):
        """  """

        self.referencesModal = referencesModal

        self.references = []
        self.referencesOnLoadCallback()
        self.referencesFilepath = "/assets/references"


    def referencesOnLoadCallback(self):
        """  """

        @app.callback(

            prevent_initial_call = False,
            output = Output("referencesRowId", "children"),
            inputs = Input("referencesModalId", "children")

        )
        def func(referencesChildren):

            self.references = []
            returnReferences = []
            for r in listdir(projectDirectory + self.referencesFilepath):

                name = r
                ref = f"{self.referencesFilepath}/{name}"

                self.references.append(r)
                returnReferences.append(self.referencesModal.addReference(name = name, reference = ref))

            return returnReferences

