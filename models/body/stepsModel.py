from re import split
# from config import (runCommands, runParameters)


class Steps:


    def __init__(self):
        """
        TODO - RetryOnFailure
        TODO - WaitForInput
        TODO - Override
        TODO - Alert
        """

        self.steps = []
        self.alert = False
        self.override = False
        self.waitForInput = False
        self.retryOnFailure = False
        self.resultsFailureMessage = "Invalid notation."
        self.commandFailureMessage = lambda c: f"Command {c} not recognized."

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

            else: return self.commandFailureMessage(results[0])

        else: return self.resultsFailureMessage