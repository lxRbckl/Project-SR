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


    def _clearSteps(self):
        """  """

        self.steps = []
        self.totalSteps = 0
        self.currentStep = 0


    def _addStep(self, entry):
        """  """

        step = {"flags" : {**self.controller.flags}, "result" : None, "status" : "Pending"}
        results = [s for s in split(r",\s*", entry.strip().lower()) if s]
        try:

            command, parameters, flags, message = {

                1 : lambda : (results[0], None, None, None),
                2 : lambda : (results[0], results[1], None, None),
                3 : lambda : (results[0], results[1], results[2], None),
                4 : lambda : (results[0], results[1], results[2], results[3])

            }[len(results)]()

        except IndexError: raise IndexError

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
        if (len(steps.strip().split(",")[0]) == 0):

            return self.errorOnSteps

        else:

            # iterate (cleaned steps) <
            for step in steps.strip().split("\n"):

                if (len(step.strip()) == 0): continue
                if (response := self._addStep(step)): return response

            # >

        # >


    def runStep(self, step):
        """  """

        try:

            self.controller.commands[step["command"]](step["parameters"])

        except Exception as e:

            print('exception', e) # remove
            return False