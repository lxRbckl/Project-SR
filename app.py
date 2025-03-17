from controller import Controller
from config import (app, port, debug)

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
from views.guideModal import Guide as guideModal
from views.body.buildSection import Build as buildSection
from views.body.resultSection import Result as resultSection
from views.body.stepsComponent import  Steps as stepsComponent
from views.referencesModal import References as referencesModal
from views.notificationComponent import Notification as notificationComponent


# register shared objects <
stepsModel = stepsModel()
controller = Controller()
stepsComponent = stepsComponent()
notifier = notificationComponent()

#

# register views <
layout = layoutView(

   notifier = notifier,
   guide = guideModal(),
   references = referencesModal(),

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
headerCallback()
bodyCallback()
stepsCallback()
buildCallback(

   notifier = notifier,
   stepsModel = stepsModel,
   controller = controller,
   stepsComponent = stepsComponent

)
runCallback(

   notifier = notifier,
   stepsModel = stepsModel,
   controller = controller,
   stepsComponent = stepsComponent

)
resultCallback(

   notifier = notifier,
   stepsModel = stepsModel

)
footerCallback()

# >


app.layout = layout.build
app.run_server(debug = debug, port = port)