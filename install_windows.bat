@echo off
echo Installing Python 3.13.0 and dependencies...

REM Download and install Python 3.13.0
powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe' -OutFile 'python-3.13.0.exe'"
python-3.13.0.exe /quiet InstallAllUsers=1 PrependPath=1

REM Install Pillow
pip install Pillow

echo Installation complete!
pause