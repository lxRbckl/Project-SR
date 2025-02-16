from src.config import app
from src.views.layout import Layout


layout = Layout()
layout.RegisterViews()
layout.RegisterCallbacks()


app.layout = layout.Build
app.run_server(debug = True)