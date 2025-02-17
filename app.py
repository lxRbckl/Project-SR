from frontend.config import app
from frontend.views.layout import Layout


layout = Layout()
layout.RegisterViews()
layout.RegisterCallbacks()


app.layout = layout.Build
app.run_server(debug = True)
