from os import getcwd
from dash import (Dash, _dash_renderer)
from dash_mantine_components import styles
from dash_bootstrap_components import themes
from os.path import (dirname, join, abspath, basename)


port = 8050
debug = True
emptyValue = ""
projectVersion = "V1.0.0"
projectName = "Project SR"
loaderStyle = {"type" : "dots"}


iconGuide = "tabler:book"
iconWarning = "bxs:error"
iconMedia = "pajamas:media"
iconSettings = "uil:setting"
iconPending = "line-md:circle"
iconAlbum = "solar:album-outline"
iconTrash = "octicon:trashcan-16"
iconOptions = "iconamoon:options"
iconSuccess = "ep:success-filled"
iconCopy = "lucide:clipboard-copy"
iconRunning = "svg-spinners:clock"
iconError = "material-symbols:error"
iconPaste = "lucide:clipboard-paste"
iconUpload = "material-symbols:upload"
iconNotification = "lucide:notification"
iconWindow = "iconamoon:screen-full-fill"
iconCompleted = "fluent-mdl2:completed-solid"


parentDir = dirname(dirname(abspath(__file__)))
currentDir = basename(dirname(abspath(__file__)))

assetDir = join(parentDir, currentDir, "assets")
referencesParentDir = join(parentDir, "references")
referencesChildPartialDir = join("assets", "references")
tesseract = join(parentDir, "Tesseract", "tesseract.exe")
guideFile = join(parentDir, currentDir, "assets", "guide.md")
referencesChildCompleteDir = join(parentDir, currentDir, referencesChildPartialDir)

print('parentDir', parentDir)
print('currentDir', currentDir, '\n')

print('assetDir', assetDir)
print('referencesChildPartialDir', referencesChildPartialDir)
print('referencesParentDir', referencesParentDir)
print('guideFile', guideFile)
print('referencesChildCompleteDir', referencesChildCompleteDir)


# Remove once Dash 3.x.x comes out #
# React conflict, because Dash 2.x.x uses React 16 #
_dash_renderer._set_react_version('18.2.0')


app = Dash(

   name = projectName,
   title = projectName,
   assets_folder = assetDir,
   suppress_callback_exceptions = True,
   external_stylesheets = [

      themes.GRID,
      themes.BOOTSTRAP,
      styles.NOTIFICATIONS

   ]

)