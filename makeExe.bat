@ECHO Deleting previous version ...
@RD /S /Q "./dist"
@RD /S /Q "./build"
@DEL /F convert.spec
@ECHO Creating exe file from Python script ...
pyinstaller --onefile convert.py
@ECHO The convert.exe file is done in the dist folder