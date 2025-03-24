## Installer
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

---

## Resources
```
pyautogui https://pyautogui.readthedocs.io/en/latest/screenshot.html?highlight=locateall
icons https://iconify.design/
dmc https://www.dash-mantine-components.com/
dbc https://dash-bootstrap-components.opensource.faculty.ai/
pytesseract https://pypi.org/project/pytesseract/
tesseract 5.5.0 tesseract-ocr-w64-setup-5.5.0.20241111.exe https://github.com/UB-Mannheim/tesseract/wiki
```

```
# development
python3 -m venv venv
mac: source .venv/bin/activate
windows: .\venv\Scripts\activate
pip3 install -r requirements.txt

# updating Python pip
Python3.9.0/python -m ensurepip --upgrade
Python3.9.0/python -m pip --version
```

---
