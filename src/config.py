import dash
from dash_mantine_components import styles
from dash_bootstrap_components import themes


columnWidth = 8
currentVersion = "1.0.0"
projectName = "Project FSR"
dash._dash_renderer._set_react_version('18.2.0')


app = dash.Dash(
   
   name = projectName,
   title = projectName,
   assets_folder = "./src/assets",
   suppress_callback_exceptions = True,
   external_stylesheets = [
   
      styles.ALL,
      themes.GRID,
      themes.BOOTSTRAP

   ]
   
)