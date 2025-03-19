from re import split
# from config import (runCommands, runParameters)


class Steps:


    def __init__(self):
        """

        """

        self.ignoreAlerts = False
        self.overrideAlerts = False
        self.overrideInputs = False

        self.steps = []
        self.alert = False
        self.waitForInput = False
        self.retryOnFailure = False
        self.messageResultsFailure = "Invalid notation."
        self.messageCommandFailure = lambda c: f"Command {c} not recognized."

        self.commands = [



        ]
        self.parameters = [

            "parameter"

        ]


    def addStep(self, step):
        """  """

        results = [s for s in split(r",\s*", step.lower().strip()) if s]

        if (len(results) > 0):

            if (results[0] in self.commands):

                self.steps.append({

                    "command" : results[0],
                    "parameters" : results[1:]

                })

            else: return self.messageCommandFailure(results[0])

        else: return self.messageResultsFailure