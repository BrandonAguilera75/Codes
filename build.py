import os
import PyInstaller.__main__

# Nombre de tu proyecto
script_name = 'Proyecto Excel.py'

PyInstaller.__main__.run([
    script_name,
    '--onefile',  # Crea un único archivo ejecutable
    '--windowed',  # Si tu aplicación es de GUI y no necesita consola
    '--icon=Favi.ico'  # Icono del ejecutable
])

print(f"Build completed for {script_name}")