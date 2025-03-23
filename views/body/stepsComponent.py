from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (iconPending, iconRunning, iconCompleted)


class Steps:


    def __init__(self):
        """  """

        pass


    def setResult(self, result):
        """  """

        print('result', result) # remove
        try:

            pass

        except KeyError: return None


    def setStatus(self, status):
        """  """

        try:

            return DashIconify(

                width = 18,
                icon = {

                    "Pending" : iconPending,
                    "Running" : iconRunning,
                    "Completed" : iconCompleted

                }[status]

            )

        except KeyError: return None


    def _buildStepStatus(self, index):
        """  """

        return dbc.Col(

            width = "auto",
            className = "stepsStatusCol",
            children = dmc.Button(

                disabled = True,
                size = "compact-sm",
                className = "stepsStatusButton",
                children = self.setStatus("Pending"),
                id = {"type" : "status-btn", "index" : f"status-{index}"}

            )

        )


    def _buildStepCommand(self, command, parameters):
        """  """

        return dbc.Col(

            width = "auto",
            className = "stepsCommandCol",
            children = dmc.Button(

                disabled = True,
                size = "compact-sm",
                className = "stepsCommandButton",
                children = [

                    # command <
                    # ?parameters <
                    dmc.Text(fw = 700, size = "xs", children = command.title()),
                    *[

                        dmc.Text(

                            size = "xs",
                            children = p,
                            className = "stepsParameterText"

                        )

                    for p in parameters]

                    # >

                ]

            )

        )


    def _buildStepFlags(self, flags):
        """  """

        if (flags):

            return dbc.Col(

                width = "auto",
                className = "stepsFlagsCol",
                children = dmc.Group(

                    gap = 0,

                    children = [

                        dmc.Button(

                            disabled = True,
                            size = "compact-sm",
                            className = "stepsFlagsButton",
                            children = dmc.Text(size = "xs", fw = 500, children = kf.title())

                        )

                    for kf, kv in flags.items()]

                )

            )

        else: return None


    def _buildStepMessage(self, message):
        """  """

        if (message):

            return dbc.Col(

                width = 12,
                className = "stepsMessageCol",
                children = dmc.Textarea(

                    value = message,
                    disabled = True,
                    size = "compact-sm",
                    className = "stepsMessageTextarea"

                )

            )

        else: return None


    def _buildStep(self, index, step):
        """  """

        return dbc.Row(

            id = f"step-{index}",
            className = "stepsRow",
            children = [

                self._buildStepStatus(index = index),
                self._buildStepCommand(

                    command = step["command"],
                    parameters = step["parameters"]

                ),
                self._buildStepFlags(flags = step["flags"]),
                self._buildStepMessage(message = step["message"])

            ]

        )


    def buildSteps(self, steps):
        """  """

        return [self._buildStep(index = c, step = s) for c, s in enumerate(steps)]
