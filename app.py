from config import app

from models.body.stepsModel import Steps as stepsModel

from views.layout import Layout as layoutView
from views.guideModal import Guide as guideModal
from views.body.runSection import Run as runSection
from views.body.bodyPartial import Body as bodyPartial
from views.headerPartial import Header as headerPartial
from views.footerPartial import Footer as footerPartial
from views.body.buildSection import Build as buildSection
from views.body.resultSection import Result as resultSection

from callbacks.body.runCallback import Run as runCallback
from callbacks.body.bodyCallback import Body as bodyCallback
from callbacks.headerCallback import Header as headerCallback
from callbacks.footerCallback import Footer as footerCallback
from callbacks.body.stepsCallback import Steps as stepsCallback
from callbacks.body.buildCallback import Build as buildCallback
from callbacks.body.resultCallback import Result as resultCallback


# register models <
stepsModel = stepsModel()

# >


# register views <
layout = layoutView(

   guide = guideModal(),
   header = headerPartial(),
   body = bodyPartial(

      items = [

         buildSection(),
         runSection(),
         resultSection()

      ]

   ),
   footer = footerPartial()

)

# >


# register callbacks <
bodyCallback()
stepsCallback()
footerCallback()
headerCallback()

runCallback(stepsModel = stepsModel)
buildCallback(stepsModel = stepsModel)
resultCallback(stepsModel = stepsModel)

# >


app.layout = layout.Build
app.run_server(debug = True)
