## Install
`echo @echo off > installer.bat`
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

## Develop
```
python3 -m venv venv
mac: source .venv/bin/activate
windows: .\venv\Scripts\activate
pip3 install -r requirements.txt
```

## Maintenance
> updating python pip
```
Python3.9.0/python -m ensurepip --upgrade
Python3.9.0/python -m pip --version
```

---

## Resources
[`PyAutoGUI`](https://pyautogui.readthedocs.io/en/latest/screenshot.html?highlight=locateall) [`Iconify`](https://iconify.design/) [`dash-mantine-components`](https://www.dash-mantine-components.com/) [`dash-bootstrap-components`](https://dash-bootstrap-components.opensource.faculty.ai/) [`pytesseract`](https://pypi.org/project/pytesseract/) [`tesseract 5.5.0`](https://github.com/UB-Mannheim/tesseract/wiki)

---
