from config import iconNotification

from dash import (html, dcc)
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class Notification:


    def __init__(self):
        """  """

        self.position = "top-right"


    @property
    def build(self):
        """  """

        return html.Div(children = [

            dmc.NotificationProvider(autoClose = False, position = self.position),
            html.Div(children = None, id = "notificationDiv")

        ])


    def notify(
        self,
        message,
        width = 20,
        show = "show",
        color = "blue",
        duration = False,
        icon = iconNotification
    ):
        """  """

        return dmc.Notification(

            color = color,
            action = show,
            message = message,
            autoClose = duration,
            className = "notification",
            icon = DashIconify(icon = icon, width = width)

        )
