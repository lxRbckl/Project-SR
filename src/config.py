from dash import Dash
from dash_bootstrap_components import themes


columnWidth = 8
currentVersion = "1.0.0"
projectName = "Project SW104-SR"


app = Dash(
   
   name = projectName,
   title = projectName,
   assets_folder = "./src/assets",
   suppress_callback_exceptions = True,
   external_stylesheets = [

      themes.GRID,
      themes.BOOTSTRAP

   ]
   
)