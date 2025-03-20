from re import split


class Steps:


    def __init__(self):
        """  """

        self.steps = []
        self.totalSteps = 0
        self.currentStep = 0

        self.ignoreAlerts = False
        self.overrideInputs = False

        self.errorInvalidFlag = lambda f: f"Flag \"{f}\" not recognized."
        self.errorInvalidCommand = lambda c: f"Command \"{c}\" not recognized."

        self.flags = {

            "alert" : False,
            "pause" : False,
            "retry" : False

        }
        self.commands = [

            "find",
            "wait",
            "click",
            "mouse",
            "scroll",
            "keyboard"

        ]


    def clearSteps(self):
        """  """

        self.steps = []
        self.totalSteps = 0
        self.currentStep = 0


    def addStep(self, entry):
        """  """

        step = {}
        flags = None
        command = None
        results = [s for s in split(r",\s*", entry.strip().lower()) if s]

        # if (empty) <
        # elif (just command) <
        # else (then command and flag(s)) <
        if (len(results) == 0): raise IndexError
        elif (len(results) == 1): command = results[0]
        else: command, flags = results[0], results[1:]

        # >

        # check command <
        if (command.split(' ')[0] in self.commands):

            # add properties #
            step["flags"] = {}
            step["result"] = None
            step["command"] = command
            step["status"] = "Pending"

        else: return self.errorInvalidCommand(command.split(' ')[0])

        # >

        # check flag(s) <
        for f in flags:

            # if (valid flag) <
            # else (then invalid flag) <
            if (f in self.flags): step["flags"][f] = True
            else: return self.errorInvalidFlag(f)

            # >

        # >

        self.totalSteps += 1
        self.steps.append(step)