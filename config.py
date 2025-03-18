from os import (getcwd, listdir)
from dash import (Dash, _dash_renderer)
from dash_mantine_components import styles
from dash_bootstrap_components import themes


iconGuide = "tabler:book"
iconWarning = "bxs:error"
iconMedia = "pajamas:media"
iconTrash = "octicon:trashcan-16"
iconSuccess = "ep:success-filled"
iconCopy = "lucide:clipboard-copy"
iconError = "material-symbols:error"
iconPaste = "lucide:clipboard-paste"
iconUpload = "material-symbols:upload"
iconNotification = "lucide:notification"
iconWindow = "iconamoon:screen-full-fill"

port = 8050
debug = True
emptyValue = ""
currentVersion = "1.0.0"
projectName = "Project SR"
projectDirectory = getcwd()
loaderStyle = {"type" : "dots"}

guideFilepath = "./assets/guide.md"

referencesFilepath = "/assets/references"
getReferences = lambda : listdir(referencesCompleteFilepath)
referencesCompleteFilepath = projectDirectory + referencesFilepath



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