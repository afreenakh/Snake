# THIS SCRIPT SHOULD BE CALLED SETUP.PY
import cx_Freeze

import os
os.environ['TCL_LIBRARY'] = "C:\\Users\Acer\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Acer\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tk8.6"

executables = [
        #                   name of your game script
        cx_Freeze.Executable("snake.py")
]

cx_Freeze.setup(
        name = "snake",
        options = {"build_exe": {"packages":["pygame"],"include_files":["apple.png","snakeHead.png"]}},
        description = "hkhchjh",
        executables = executables
)

#python setup.py build
#python setup.py bdist_msi
