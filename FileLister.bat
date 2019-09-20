rem display a list of files in windows and push the results to a html file.
@echo off
cls
py test.py c:\windows\system32\*.dll output.html
pause