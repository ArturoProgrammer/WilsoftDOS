mode con lines=10 cols=80
@echo off
title BIOS
color 9f

set opreg=#00xAFF89
set secunreg=#12x8Wk75
set thirdreg=#76xFFF90


:main
if exist #00xAFF89 (
	echo SOFTWARE OPERATIONAL AND READY
	echo.
	ping -n 2 0.0.0.0 > nul
	echo SEGMENT: %opreg% -- TRUE...
) else (
	echo SEGMENT: %opreg% -- FALSE...
	echo ERROR 5: THE SEGMENT NOT EXIST
	goto try
)

if exist #12x8Wk75 (
	ping -n 2 0.0.0.0 > nul
	echo SEGMENT: %secunreg% -- TRUE...
) else (
	echo SEGMENT: %secunreg% -- FALSE...
	echo ERROR 5: THE SEGMENT NOT EXIST
	goto try
)

if exist #76xFFF90 (
	ping -n 2 0.0.0.0 > nul
	echo SEGMENT: %thirdreg% -- TRUE...
	goto start
) else (
	echo SEGMENT: %thirdreg% -- FALSE...
	echo ERROR 5: THE SEGMENT NOT EXIST
	goto try
)

:try
echo.
set /p retry=DO YOU WANT TO TRY AGAIN? [Y/N] 
if %retry% == Y (
	cls
	goto main
) else (
	exit
)

:start
cd #00xAFF89
if exist kernel.bat (
	start kernel.bat
	exit
) else (
	cd sys8
	cd osMessages
	start kernelmsgError.vbs
)