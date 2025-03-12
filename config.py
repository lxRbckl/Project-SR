import dash
from dash_mantine_components import styles
from dash_bootstrap_components import themes


emptyValue = ""
layoutColWidth = 9
accordionLoadTime = 0
currentVersion = "1.0.0"
projectName = "Project SR"
defaultAccordionItem = "Build"
notificationPosition = "bottom-right"

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
dash._dash_renderer._set_react_version('18.2.0')


app = dash.Dash(

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