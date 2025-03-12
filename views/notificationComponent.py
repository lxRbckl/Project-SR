from dash import (html, dcc)
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from config import (notificationPosition, iconNotification)


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
        icon = iconNotification
    ):
        """  """

        return dmc.Notification(

            id = uid,
            action = show,
            message = message,
            autoClose = duration,
            icon = DashIconify(icon = icon)

        )
