from cx_Freeze import setup, Executable

# Reemplaza "Proyecto Excel.py" con el nombre de tu script Python
script = "Proyecto Excel.py"

# Reemplaza "Favi.ico" con el nombre y la ruta de tu ícono, si tienes uno
icono = "Favi.ico"

# Define el ejecutable
executables = [Executable(script, base=None, icon=icono)]

# Configuración de cx_Freeze
setup(
    name="Proyecto Excel",
    version="1.0",
    description="Modificador de Excel",
    executables=executables
)
