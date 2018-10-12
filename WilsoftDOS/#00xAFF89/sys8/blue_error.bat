@echo off
title Operative System Error Screen
mode con lines=25 cols=70
color 1f


:message
set errorcode=###000A
echo ERROR
echo.
echo.
echo HA OCURRIDO UN ERROR EN EL SISTEMA, LAS POSIBLES CAUSAS PUEDEN SER:
echo.
echo - UNA MALA INSTALACION DE UN SOFTWARE
echo - UNA MALA CONFIGURACION DEL SO
echo - UN ERROR EN EL HARDWARE
echo - INCOMPATIBILIDAD DE ARCHIVO/S O HARDWARE
echo - FALTA DE ARCHIVOS CLASS-8 O DLA
echo.
echo ERROR CODE: %errorcode%
echo.
echo.
set /p searcherror=BUSCAR PROBLEMA [Ok/Cancel] 
if %searcherror%==Ok ( 
	goto searchproblem 
) else (
	exit
)


:searchproblem
::Check Directories
cls
cd ..
echo.
echo OS ANALITYCS
echo.
echo REVISANDO ARCHIVOS Y DIRECTORIOS IMPORTANTES CLASS-8
echo.
if exist caches (
	echo -caches dir.return[TRUE]
) else (
	echo -caches dir.return[FALSE]
	set errorcode=#FFx61H770
)
::Agregar busqueda de archivos principales.
if exist sys8 (
	echo -sys8 dir.return[TRUE]
	cd sys8
	if exist appExecuterOntime (
		echo --appExecuterOntime dir.return[TRUE]
		cd appExecuterOntime
	)
	if exist main_onTime.py (
		echo ---main_onTime.py file.return[TRUE]
	) else (
		echo ---main_onTime.py file.return[FALSE]
	)
	if exist mainOnTimeTEMPORAL.bat (
		echo ---mainOnTimeTEMPORAL.bat file.return[TRUE]
	) else (
		echo ---mainOnTimeTEMPORAL.bat file.return[FALSE]
	)
	rem Regresa al directorio 'sys8'
	cd ..
	if exist consoleenvironment (
		echo --consoleenvironment dir.return[TRUE]
		cd consoleenvironment
	)
	rem Regresa al directorio 'sys8'
	cd ..
	rem Regresa el directorio '#00xAFF89'
	cd ..
) else (
	echo -sys8 dir.return[FALSE]
	set errorcode=#FFx8GA35K
)
if exist usr.bin (
	echo -usr.bin dir.return[TRUE]
) else (
	echo -usr.bin dir.return[FALSE]
	set errorcode=#FFx92YFFF
)

if not %errorcode%==###000A goto scanfinal-t
if %errorcode%==###000A goto scanfinal-f

:scanfinal-t
echo.
echo BUSQUEDA TERMINADA
echo.
echo.
echo ERROR CODE: %errorcode%
echo.
echo PARA MAS INFORMACION ACERCA DEL PROBLEMA, CONSULTA EL PROGRAMA 'OsHelp'
echo COPIE EL CODIGO DE ERROR Y BUSQUE MAS INFORMACION ACERCA DE EL PARA	
echo SABER LA FUENTE DEL PROBLEMA.
echo.
echo.
set /p restartQ=REINICIAR SISTEMA [Y] 
if %restartQ%==Y goto restart

:scanfinal-f
echo.
echo BUSQUEDA TERMINADA
echo.
echo.
echo ERROR CODE: %errorcode%
echo.
echo NO SE HA DETECTADO NINGUN PROBLEMA INTERNO.
set /p restartQ=REINICIAR SISTEMA [Y] 
if %restartQ%==Y goto restart

:restart
cd ..
start bios.bat
exit