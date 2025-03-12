from dash import (html, dcc)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

from config import (notificationPosition)


class Notification:


    def __init__(self):
        """  """

        pass


    @property
    def build(self):
        """  """

        return html.Div(children = [

            dmc.NotificationProvider(

                autoClose = False,
                position = notificationPosition

            ),
            html.Div(

                children = None,
                id = "notificationDiv"

            )

        ])


    @staticmethod
    def notify(
        message,
        uid = "",
        show = "show",
        duration = False,
        icon = "mingcute:notification-fill"
    ):
        """  """

        return dmc.Notification(

            id = uid,
            action = show,
            message = message,
            autoClose = duration,
            icon = DashIconify(icon = icon)

        )