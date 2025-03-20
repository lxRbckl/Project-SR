from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Steps:


    def __init__(self):
        """  """

        pass


    def _buildStepStatus(self, index, status):
        """  """

        print('status', status)
        return dbc.Col(

            width = "auto",
            children = dmc.Button(

                size = "compact-sm"

            )

        )


    def _buildStepCommand(self, index, command):
        """  """

        print('command', command)
        return dbc.Col(

            width = "auto",
            children = None

        )


    def _buildStepFlags(self, index, flags):
        """  """

        return dbc.Col(

            width = "auto",
            children = dmc.Group(

                gap = 4,
                children = [

                    dmc.Button(

                        disabled = True,
                        size = "compact-sm",
                        children = kf.title(),
                        className = "stepsFlagsButton",
                        id = f"stepsFlagsButton-{index}"
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

                self._buildStepStatus(index = index, status = step["status"]),
                self._buildStepCommand(index = index, command = step["command"]),
                self._buildStepFlags(index = index, flags = step["flags"])

            ]

        )


    def buildSteps(self, steps):
        """  """

        return [self._buildStep(index = c, step = s) for c, s in enumerate(steps)]
