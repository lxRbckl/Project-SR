from config import iconPending

from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Steps:


    def __init__(self):
        """  """

        pass


    def _buildStepsResult(self, index):
        """  """

        return dbc.Col(

            width = "auto",
            className = "stepsResultCol",
            children = dmc.Button(

                color = None,
                children = None,
                disabled = True,
                size = "compact-sm",
                className = "stepsResultButton",
                id = {"type" : "result-btn", "index" : f"result-{index}"}

            )

        )


    def _buildStepStatus(self, index, status):
        """  """

        return dbc.Col(

            width = "auto",
            className = "stepsStatusCol",
            children = dmc.Button(

                disabled = True,
                children = status,
                size = "compact-sm",
                className = "stepsStatusButton",
                leftSection = DashIconify(

                    icon = iconPending,
                    id = {"type" : "status-icon", "index" : f"status-icon-{index}"}

                ),
                id = {"type" : "status-btn", "index" : f"status-{index}"}

            )

        )


    def _buildStepCommand(self, index, command):
        """  """

        return dbc.Col(

            width = "auto",
            className = "stepsCommandCol",
            children = dmc.Group(

                gap = 0,
                children = [

                    dmc.Button(

                        children = c,
                        disabled = True,
                        size = "compact-sm",
                        className = "stepsCommandButton"

                    )

                for i, c in enumerate(command.split(" "))]

            )

        )


    def _buildStepFlags(self, index, flags):
        """  """

        return dbc.Col(

            width = "auto",
            className = "stepsFlagsCol",
            children = dmc.Group(

                gap = 0,
                children = [

                    dmc.Button(

                        disabled = True,
                        size = "compact-sm",
                        children = kf.title(),
                        className = "stepsFlagsButton"

                    )

                for kf, kv in flags.items()]

            )

        )


    def _buildStep(self, index, step):
        """  """

        return dbc.Row(

            justify = "start",
            id = f"step-{index}",
            className = "rowExtended stepsRow",
            children = [

                self._buildStepsResult(index = index),
                self._buildStepStatus(index = index, status = step["status"]),
                self._buildStepCommand(index = index, command = step["command"]),
                self._buildStepFlags(index = index, flags = step["flags"])

            ]

        )


    def buildSteps(self, steps):
        """  """

        return [self._buildStep(index = c, step = s) for c, s in enumerate(steps)]
