@echo off
title OCMover

:: El argumento a recibir es el nombre del archivo a mover
set filetomove=%1

echo Moviando el archivo %filetomove%
cd ..
cd ..
move sys8\appExecuterOntime\%filetomove% caches

exit