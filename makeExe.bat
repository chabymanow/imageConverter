@ECHO Deleting previous version ...
@RD /S /Q "./dist"
@ECHO Creating exe file from Python script ...
pyinstaller --onefile convert.py
@ECHO The convert.exe file is done in the dist folder