from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Steps:


    def __init__(self):
        """  """

        pass


    def _buildStepStatus(self, status):
        """  """

        return dbc.Col(

            width = "auto",
            children = html.Small(status)

        )


    def _buildStepCommand(self, command):
        """  """

        return dbc.Col(

            width = "auto",
            children = html.Small(command)

        )


    def _buildStepFlags(self, flags):
        """  """

        print('flags', flags) # remove
        return None

        # return dbc.Col(
        #
        #     width = "auto",
        #     children = [
        #
        #         dmc.Badge(children = fk,
        #                   style = {"margin" : 0, "background-color" : "red"})
        #
        #     for fk, fv in flags.items() if (fv == True)]
        #
        # )


    def _buildStep(self, index, step):
        """  """

        return dbc.Row(

            justify = "start",
            # width = 12,
            id = f"step-{index}",
            className = "colExtended stepsCol",
            children = [

                self._buildStepStatus(status = step["status"]),
                self._buildStepCommand(command = step["command"]),
                self._buildStepFlags(flags = step["flags"])

            ]

        )


    def buildSteps(self, steps):
        """  """

        return [self._buildStep(index = c, step = s) for c, s in enumerate(steps)]
