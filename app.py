from frontend.config import app

from frontend.views.body.run import Run as runItem
from frontend.views.body.body import Body as bodyView
from frontend.views.layout import Layout as layoutView
from frontend.views.header import Header as headerView
from frontend.views.footer import Footer as footerView
from frontend.views.body.build import Build as buildItem
from frontend.views.documentation import Documentation as documentationView
from frontend.views.body.instruction import Instruction as instructionComponent

from frontend.callbacks.body.run import Run as runCallback
from frontend.callbacks.body.body import Body as bodyCallback
from frontend.callbacks.header import Header as headerCallback
from frontend.callbacks.footer import Footer as footerCallback
from frontend.callbacks.body.build import Build as buildCallback
from frontend.callbacks.body.instruction import Instruction as instructionCallback


# register views <
layout = layoutView(children = [

   headerView().Build,
   documentationView().Build,

   bodyView(items = [

      buildItem(instruction = instructionComponent),
      runItem()

   ]).Build,

   footerView().Build

])

# >


# register callbacks <
headerCallback()

runCallback()
bodyCallback()
buildCallback()
instructionCallback()

footerCallback()

# >


app.layout = layout.Build
app.run_server(debug = True)
