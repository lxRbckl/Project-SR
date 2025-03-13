from config import iconNotification

from dash import (html, dcc)
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Notification:

    def __init__(self):
        """  """

        self.notificationPosition = "bottom-right"


    @property
    def build(self):
        """  """

        return html.Div(children = [

            dmc.NotificationProvider(

                autoClose = False,
                position = self.notificationPosition

            ),
            html.Div(

                children = None,
                id = "notificationDiv"

            )

        ])


    def notify(
        self,
        message,
        show = "show",
        color = "blue",
        iconWidth = 20,
        duration = False,
        icon = iconNotification
    ):
        """  """

        return dmc.Notification(

            action = show,
            color = color,
            message = message,
            autoClose = duration,
            className = "notification",
            icon = DashIconify(

                icon = icon,
                width = iconWidth

            )

        )
