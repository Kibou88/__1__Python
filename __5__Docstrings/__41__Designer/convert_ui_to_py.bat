@echo off
:: Convertisseur fichier ui (Designer) en fichier py

echo %cd%

:: Path vers uic.exe
set path_uic="C:\Python\Lib\site-packages\PySide6\uic.exe"

:: Demander le nom du fichier ui
echo Nom du fichier ui :
set /p ui_file=

:: Construire le chemin du fichier ui
set path_ui=%cd%\%ui_file%
echo %path_ui%

:: Demande le nom du fichier py
echo Nom du fichier py :
set /p py_file=

:: Construire le chemin du fichier py
set path_py=%cd%\%py_file%
echo %path_py%

:: Exécuter la commande uic
%path_uic% %path_ui% -o %path_py% -g python

:: Vérifier si le fichier py a été créé
if exist "%path_py%" (
    echo Succes : Le fichier %py_file% a ete cree.
) else (
    echo Erreur : Le fichier %py_file% n'a pas ete cree.
)

pause
