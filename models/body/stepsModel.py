from re import split
from time import sleep

from config import (runCommands, runParameters, getReferences)


class Steps:


    def __init__(self):
        """
        RetryOnFailure
        WaitForInput
        Direction
        Override
        AlertMe
        Wait
        """

        self.wait = 10
        self.steps = []
        self.alertMe = False
        self.override = False
        self.direction = False
        self.waitForInput = False
        self.retryOnFailure = False
        self.resultsFailureMessage = "Invalid notation."
        self.checkAssetExists = lambda a: (a in getReferences())
        self.assetFailureMessage = lambda c: f"Asset {c} not recognized."
        self.commandFailureMessage = lambda c: f"Command {c} not recognized."
        self.parameterFailureMessage = lambda c: f"Parameter {c} not recognized."


    def addStep(self, step):
        """  """

        results = [s for s in split(r",\s*", step.lower().strip()) if s]

        if (len(results) > 0):

            if (results[0] in runCommands):

                self.steps.append({

                    "command" : results[0],
                    "parameters" : results[1:]

                })

            else: return self.commandFailureMessage(results[0])

        else: return self.resultsFailureMessage