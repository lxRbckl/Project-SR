from src.config import app
from src.views.layoutView import Layout


layout = Layout()

app.layout = layout.Build
server = app.server


app.run_server() # for running locally