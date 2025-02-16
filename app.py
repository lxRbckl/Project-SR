# from src.config import app
# from views.layout import Layout


from src.config import app
from src.views.layout import Layout


layout = Layout()


app.layout = layout.Build
app.run_server(debug = True)