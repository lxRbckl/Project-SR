from re import split
# from config import (runCommands, runParameters)


class Steps:


    def __init__(self):
        """

        """

        self.steps = []

        self.ignoreAlerts = False
        self.overrideAlerts = False
        self.overrideInputs = False

        self.errorInvalidFlag = lambda f: f"Flag {f} not recognized."
        self.errorInvalidCommand = lambda c: f"Command {c} not recognized."

        self.commands = [
            "command"

            "find",
            "wait",
            "click",
            "mouse",
            "scroll",
            "keyboard"

        ]
        self.flags = {

            "alert" : ["alert"],
            "input" : ["wfi", "input", "wait for input"],
            "retry" : ["rof", "retry", "retry on failure"]

        }


    def addStep(self, step):
        """  """

        flags = None
        command = None
        results = [s for s in split(r",\s*", step.lower().strip()) if s]

        # if (empty) <
        # elif (just command) <
        # else (then command and flag(s)) <
        if (len(results) == 0): raise IndexError
        elif (len(results) == 1): command = results[0]
        else: command, flags = results[0], results[1:]

        # >

        print('command', command, ':', 'flags', flags) # remove

        # if (len(results) > 0):
        #
        #     if (results[0] in self.commands):
        #
        #         self.steps.append({
        #
        #             "command" : results[0],
        #             "flags" : results[1:]
        #
        #         })
        #
        #     else: return self.messageCommandFailure(results[0])
        #
        # else: return self.messageResultsFailure