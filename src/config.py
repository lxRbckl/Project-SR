from dash import Dash
from dash_bootstrap_components import themes


columnWidth = 8
currentVersion = "1.0.0"


app = Dash(
   
   name = "Project SW104SR",
   title = "Project SW104SR",
   assets_folder = "./src/assets",
   suppress_callback_exceptions = True,
   external_stylesheets = [

      themes.GRID,
      themes.BOOTSTRAP

   ]
   
)