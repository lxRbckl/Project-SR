from re import split


class Steps:


    def __init__(self, controller):
        """  """

        self.controller = controller

        self.steps = []
        self.totalSteps = 0
        self.currentStep = 0
        self.ignoreAlerts = False
        self.overrideInputs = False

        self.errorOnSteps = "Invalid input."
        self.errorInvalidFlag = lambda f: f"Flag \"{f}\" not recognized."
        self.errorInvalidCommand = lambda c: f"Command \"{c}\" not recognized."
        self.errorInvalidParameters = lambda p, c: f"Parameters \"{p}\" not recognized for \"{c}\"."


    def getFlags(self): return self.steps[self.currentStep]["flags"]
    def getCommand(self): return self.steps[self.currentStep]["command"]
    def getMessage(self): return self.steps[self.currentStep]["message"]
    def getParameters(self): return self.steps[self.currentStep]["parameters"]


    def _clearSteps(self):
        """  """

        self.steps = []
        self.totalSteps = 0
        self.currentStep = 0


    def _addStep(self, entry):
        """  """

        step = {"flags" : {**self.controller.flags}, "result" : None, "status" : "Pending"}
        results = [s for s in split(r",\s*", entry.strip().lower()) if s]
        command, parameters, flags, message = (results + [None] * 4)[:4]

        # check flags <
        # check command <
        if (flags):

            for f in [f.lower() for f in flags.split(" ")]:

                if (f in self.controller.flags): step["flags"][f] = True
                else: return self.errorInvalidFlag(f)

        if (command not in self.controller.commands): return self.errorInvalidCommand(command)

        # >

        step["parameters"] = parameters.split(" ") if parameters else []
        step["message"] = message
        step["command"] = command
        self.steps.append(step)
        self.totalSteps += 1


    def addSteps(self, steps):
        """  """

        self._clearSteps()

        # if (invalid input) <
        # else (then parsable) <
        if (len(steps.strip().split(",")[0]) == 0): return self.errorOnSteps
        else:

            # iterate (cleaned steps) <
            for step in steps.strip().split("\n"):

                if (len(step.strip()) == 0): continue
                if (response := self._addStep(step)): return response

            # >

        # >


    def runStep(self):
        """  """

        command = self.getCommand()
        parameters = self.getParameters()
        try:

            a, b, c, d = (parameters + [None] * 4)[:4]
            return self.controller.commands[command](a, b, c, d)

        except TypeError: return self.errorInvalidParameters(c = command, p = parameters)