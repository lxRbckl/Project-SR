from re import split
from config import (runCommands, runParameters)


class Steps:


    def __init__(self):
        """  """

        self.steps = []


    def addStep(self, step):
        """  """

        # parse #
        command, text, *parameters = split(r",\s*", step.lower())

        # verify (command, (text/asset?), parameters) <
        if (command not in runCommands): return f"Command \"{command}\" not recognized."
        #
        for param in parameters:

            if (param not in runParameters): return f"Parameter \"{param}\" not recognized."

        # >

        # add <
        self.steps.append(

            {

                "command": command,
                "text": text,
                "parameters": parameters

            }

        )

        # >

        return None
