
import sys
import os
import bpy
import importlib
custom_scriptsPath = r"C:\Users\czars\OneDrive\Documents\Custom Scripts\Haika_scripts\blender_python"

if not custom_scriptsPath in sys.path:
    sys.path.append(custom_scriptsPath)

#imports
import properties_and_Drivers as pd

#reloads
importlib.reload(pd)