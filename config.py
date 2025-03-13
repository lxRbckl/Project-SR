from dash import (Dash, _dash_renderer)
from dash_mantine_components import styles
from dash_bootstrap_components import themes


emptyValue = ""
currentVersion = "1.0.0"
projectName = "Project SR  command, text, parameter"

iconWarning = "bxs:error"
iconCopy = "lucide:clipboard-copy"
iconVersion = "stash:version-solid"
iconError = "material-symbols:error"
iconPaste = "lucide:clipboard-paste"
iconNotification = "lucide:notification"
iconWindow = "iconamoon:screen-full-fill"

buildOptions = [
   "option"
]
runCommands = [
   "command"
]
runParameters = [
   "parameter"
]


# Remove once Dash 3.x.x comes out #
# React conflict, because Dash 2.x.x uses React 16 #
_dash_renderer._set_react_version('18.2.0')


app = Dash(

   name = projectName,
   title = projectName,
   assets_folder = "./assets",
   suppress_callback_exceptions = True,
   external_stylesheets = [

      themes.GRID,
      themes.BOOTSTRAP,
      styles.NOTIFICATIONS

   ]
   
)