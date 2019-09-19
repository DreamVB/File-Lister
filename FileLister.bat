rem display a list of files in windows and push the results to a html file.
@echo off
cls
py FileLister.py c:\windows\*.exe > c:\out\dir.html
rem display the page in the default web broswer
c:\out\dir.html
pause