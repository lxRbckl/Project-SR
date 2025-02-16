from src.config import app
from src.views.layout import Layout


layout = Layout()
layout.RegisterViews()
layout.RegisterCallbacks()


app.layout = layout.Build
app.run_server(debug = True)



# blinker==1.9.0
# certifi==2025.1.31
# charset-normalizer==3.4.1
# click==8.1.8
# dash==2.18.2
# dash-bootstrap-components==1.7.1
# dash-core-components==2.0.0
# dash-html-components==2.0.0
# dash-table==5.0.0
# dash_mantine_components==0.15.3
# Flask==3.0.3
# idna==3.10
# importlib_metadata==8.6.1
# itsdangerous==2.2.0
# Jinja2==3.1.5
# MarkupSafe==3.0.2
# narwhals==1.26.0
# nest-asyncio==1.6.0
# packaging==24.2
# plotly==6.0.0
# requests==2.32.3
# retrying==1.3.4
# six==1.17.0
# typing_extensions==4.12.2
# urllib3==2.3.0
# Werkzeug==3.0.6
# zipp==3.21.0
