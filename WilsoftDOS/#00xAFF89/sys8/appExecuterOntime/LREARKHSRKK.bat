@echo off
title Kernel Shell - Command Line Interface 
mode con lines=20 cols=82

echo.
echo WILSOFTDOS 082017
echo.

goto main

:main
set dir=globalDir

set /p shellcommand=%date%.%username%[%dir%]:: 

if %shellcommand%==close exit
if %shellcommand%==opwil goto startingGui
if %shellcommand%==chcolor goto ccolor
if %shellcommand%==initred goto network

:network
echo INGRESE EL PUERTO AL QUE SE DESEA CONECTAR
set /p webport=PORT: 

:ccolor
set /p ncolor=COLOR: 
if %ncolor%==null (
    goto main
) else (
    color %ncolor%
    goto main
)


:startingGui
:: Inicia la interfaz de usuario
cd ..
cd interface

set /p osmodecode=DESEA INICIAR EL SISTEMA EN MODO SEGURO? [Y/N] 

if %osmodecode%==Y (
	python gui.py -y -y -s -y
) else (
	python gui.py -y -y -n -y
)

pause > nul
exit