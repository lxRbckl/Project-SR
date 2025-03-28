from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (iconStop, iconPending, iconRunning, iconCompleted)


class Steps:


    def __init__(self):
        """  """

        pass


    def _buildStepResult(self, index):
        """  """

        return dbc.Col(

            width = "auto",
            className = "stepsResultCol",
            children = dmc.Button(

                children = None,
                disabled = True,
                className = "test",
                size = "compact-sm",
                id = {"type" : "result-btn", "index" : f"result-{index}"}


            )

        )


    def setStepStatus(self, status = "Pending"):
        """  """

        return DashIconify(

            width = 16,
            icon = {

                "stopped" : iconStop,
                "Pending" : iconPending,
                "Running" : iconRunning,
                "Completed" : iconCompleted

            }[status]

        )


    def _buildStepStatus(self, index):
        """  """

        return dbc.Col(

            width = "auto",
            className = "stepsStatusCol",
            children = dmc.Button(

                disabled = True,
                size = "compact-sm",
                children = self.setStepStatus(),
                className = "stepsStatusButton",
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
                            children = p.title(),
                            className = "stepsParameterText"

                        )

                    for p in parameters]

                    # >

                ]

            )

        )


    def _buildStepFlags(self, flags):
        """  """

        if (list(flags.values()).count(True) > 0):

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
                            children = dmc.Text(

                                fw = 500,
                                size = "xs",
                                children = kf.title()

                            )

                        )

                    for kf, kv in flags.items() if kv]

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

            className = "stepsRow",
            id = {"type" : "step-row", "index" : f"step-{index}"},
            children = [

                self._buildStepResult(index),
                self._buildStepStatus(index),
                self._buildStepCommand(

                    command = step["command"],
                    parameters = step["parameters"]

                ),
                self._buildStepFlags(step["flags"]),
                self._buildStepMessage(step["message"])

            ]

        )


    def buildSteps(self, steps):
        """  """

        return [self._buildStep(index = c, step = s) for c, s in enumerate(steps)]