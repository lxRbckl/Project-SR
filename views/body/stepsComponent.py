from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Steps:


    def __init__(self):
        """  """

        pass


    def _buildStepFlags(self, flags):
        """  """

        return None


    def _buildStepStatus(self, status):
        """  """

        return None


    def _buildStepCommand(self, command):
        """  """

        return None


    def _buildStep(self, step):
        """  """

        return dbc.Col(

            width = 12,
            className = "colExtended stepsCol",
            children = [

                self._buildStepStatus(status = step["status"]),
                self._buildStepCommand(command = step["command"]),
                self._buildStepFlags(flags = step["flags"])

            ]

        )


    def buildSteps(self, steps):
        """  """

        return [self._buildStep(s) for s in steps]
