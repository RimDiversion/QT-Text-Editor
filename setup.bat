pyinstaller --onefile -w main.py  && CALL :format && CALL :move
EXIT /B %ERRORLEVEL%

:format
del main.spec
rmdir /S /Q build
mkdir .\QT-Text-Editor\files
mkdir .\QT-Text-Editor\recovery
EXIT /B 0

:move
move .\dist\main.exe .\QT-Text-Editor\QT-Text-Editor.exe
rmdir dist
EXIT /B 0