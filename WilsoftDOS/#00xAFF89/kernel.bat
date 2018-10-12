@echo off
title .:SYSTEM KERNEL:.
color fc
mode con lines=15 cols=70


:main
:: Verifica la existencia de los directorios principales
if exist caches (
	echo 'caches' dir exist[TRUE]
	echo Ultimo inicio: %date% %time% > SystemStart%date%.reg
) else (
	echo 'caches' dir exist[FALSE]!! - ERROR 2
	echo.
	echo Creating dir caches...
	echo.
	mkdir caches
)
if exist programs_ (
	echo 'programs_' dir exist[TRUE]
) else (
	echo 'programs_' dir exist[FALSE]!! - ERROR 2
	echo.
	cd sys8
	start blue_error.bat
	exit
)
if exist dependences (
	echo 'dependences' dir exist[TRUE]
) else (
	echo 'dependences' dir exist[FALSE]!! - ERROR 2
	echo.
	cd sys8
	start blue_error.bat
	exit
)
if exist sys8 (
	echo 'sys8' dir exist[TRUE]
	rem goto startProcess
) else (
	echo 'sys8' dir exist[FALSE]!! - ERROR 2
	echo.
	cd sys8
	start blue_error.bat
	exit
)

:: Carpetas que se encuentran dentro de sys8
cd sys8
if exist appExecuterOntime (
	echo 'appExecuterOntime' dir exist[TRUE]
) else (
	echo 'appExecuterOntime' dir exist[FALSE]!! - ERROR 2
	echo.
	start blue_error.bat
	exit
)

if exist interface (
	echo 'interface' dir exist[TRUE]
) else (
	echo 'interface' dir exist[FALSE]!! - ERROR 2
	echo.
	start blue_error.bat
	exit
)

if exist osMessages (
	echo 'osMessages' dir exist[TRUE]
) else (
	echo 'osMessages' dir exist[FALSE]!! - ERROR 2
	echo.
	start blue_error.bat
	exit
)

cd ..
:: Se regresa un directorio atras


:startProcess
:: En caso de que existe la clase con la interfaz de usuario, se iniciara
cd sys8
cd interface
if exist gui.py (
	echo.
	echo.
	echo EJECUTANDO INTERFAZ PRINCIPAL...
	ping -n 2 0.0.0.0 > nul
	python gui.py -y -y -n -y
	pause > nul
	exit
) else (
	goto initShell
)


:initShell
:: En caso de que no exista la interfaz de usuario, se ejecutara la consola
cd ..
cd appExecuterOntime
echo.
echo.
echo EJECUTANDO SHELL...
ping -n 5 0.0.0.0 > nul
start LREARKHSRKK.bat
exit