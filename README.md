## Installation
`echo @echo off > install.bat`
```
@echo off

set "DIR=Project-SR"
set "PYTHON=%cd%\Python3.9.0\python.exe"
set "REPO_URL=https://github.com/lxRbckl/Project-SR.git"

if exist "%DIR%" (
    rmdir /s /q "%DIR%"
)

git clone %REPO_URL% %DIR%

%PYTHON% -m pip install -r "%DIR%\requirements.txt"

pause
```

## Run
`echo @echo off > run.bat`
```
set "DIR=Project-SR"
set "PYTHON=%cd%\Python3.9.0\python.exe"

%PYTHON% "%DIR%\app.py"
```

```
Ensure both install.bat and run.bat have either ANSI or UTF-8 encoding to run properly. You can do this via Notepad -> Save As.
```

---

## Development
It is recommended to clone this repository within the root directory of the project—ideally at the same level as Tesseract and Python 3.9.0. If following this structure, create a folder named Project-SR and clone the repository into it. Alternatively, if the repository is placed elsewhere, ensure you obtain the full file path to the Tesseract executable, and temporarily update the `tesseract` variable in `config.py` accordingly.


### Windows
```shell
python3 -m venv venv
.\venv\Scripts\activate
pip3 install -r requirements.txt
```

### MacOS
```shell
python3 -m venv venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Configuration
`PyCharm`
```
Setting up Python Interpreter
Settings -> Project-SR -> Python Interpreter -> Add Local Interpreter -> Select Existing -> ~/Project-SR/venv/Scripts/python.exe

Setting up Run Configuration
Configure Run -> Edit Configuration -> Add New -> Python -> Script => ~\Project-SR\Project-SR\app.py
```

### Maintenance
> These are bootstrap procedures in the event of complete local project loss.
```
# updating python pip
Python3.9.0/python -m ensurepip --upgrade
Python3.9.0/python -m pip --version
```

---

## Resources
[`PyAutoGUI`](https://pyautogui.readthedocs.io/en/latest/screenshot.html?highlight=locateall) [`Iconify`](https://iconify.design/) [`dash-mantine-components`](https://www.dash-mantine-components.com/) [`dash-bootstrap-components`](https://dash-bootstrap-components.opensource.faculty.ai/) [`pytesseract`](https://pypi.org/project/pytesseract/) [`tesseract 5.5.0`](https://github.com/UB-Mannheim/tesseract/wiki) [`Dash`](https://dash.plotly.com/)

---
