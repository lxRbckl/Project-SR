from config import app, notificationPosition

from models.body.stepsModel import Steps as stepsModel

from callbacks.body.runCallback import Run as runCallback
from callbacks.body.bodyCallback import Body as bodyCallback
from callbacks.headerCallback import Header as headerCallback
from callbacks.footerCallback import Footer as footerCallback
from callbacks.body.stepsCallback import Steps as stepsCallback
from callbacks.body.buildCallback import Build as buildCallback
from callbacks.body.resultCallback import Result as resultCallback

from views.layout import Layout as layoutView
from views.body.runSection import Run as runSection
from views.body.bodyPartial import Body as bodyPartial
from views.headerPartial import Header as headerPartial
from views.footerPartial import Footer as footerPartial
from views.guideComponent import Guide as guideComponent
from views.body.buildSection import Build as buildSection
from views.body.resultSection import Result as resultSection
from views.body.stepsComponent import  Steps as stepsComponent
from views.notificationComponent import Notification as notificationComponent


# register models <
stepsModel = stepsModel()

# >

# register views <
notifier = notificationComponent()
layout = layoutView(

   notifier = notificationComponent(),
   guide = guideComponent(),
   header = headerPartial(),
   body = bodyPartial(

      items = [

         buildSection(notifier = notifier),
         runSection(notifier = notifier),
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

buildCallback(stepsModel = stepsModel, stepsComponent = stepsComponent)
runCallback(stepsModel = stepsModel, stepsComponent = stepsComponent)
resultCallback(stepsModel = stepsModel)

# >


app.layout = layout.build
app.run_server(debug = True)
