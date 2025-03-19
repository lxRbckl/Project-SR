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

        self.flags = [

            "flag", # remove
            "alert",
            "pause",
            "retry"

        ]
        self.commands = [

            "command", # remove
            "find",
            "wait",
            "click",
            "mouse",
            "scroll",
            "keyboard"

        ]


    def addStep(self, entry):
        """  """

        flags = None
        command = None
        step = {

            "command" : None,
            "alert" : False,
            "pause" : False,
            "retry" : False

        }
        results = [s for s in split(r",\s*", entry.lower().strip()) if s]

        # if (empty) <
        # elif (just command) <
        # else (then command and flag(s)) <
        if (len(results) == 0): raise IndexError
        elif (len(results) == 1): command = results[0]
        else: command, flags = results[0], results[1:]

        # >

        # check command <
        for c in self.commands:

            if (c in command):

                step["command"] = command
                break

        else: return self.errorInvalidCommand(command)

        # >

        # check flag(s) <
        for f in flags:

            # if (valid flag) <
            # else (then invalid flag) <
            if (f in self.flags): step[f] = True
            else: self.errorInvalidFlag(f)

            # >

        # >

        print(step) # remove
        self.steps