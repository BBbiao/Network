@echo off
echo ...
echo ...
echo ...

python D:\#workspace\GiHub\Netlaunch\Version_1.1\Netlaunch_v1.1.py
::echo %ERRORLEVEL% 
if %ERRORLEVEL%==5 (
   echo µÇÂ½³É¹¦
) else (
   echo Ê§°Ü
)

pause