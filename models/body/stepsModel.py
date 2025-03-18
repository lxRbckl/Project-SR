from re import split
from time import sleep

from config import (runCommands, runParameters)


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
        self.AlertMe = False
        self.Override = False
        self.Direction = False
        self.WaitForInput = False
        self.retryOnFailure = False


    def addStep(self, step):
        """  """

        # parse #
        command, text, *parameters = split(r",\s*", step.lower().strip())

        # verify (command, asset?, parameters) <
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
