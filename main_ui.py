import maya.cmds as cmds
import sys
cmds.file(f=True, new=True)
sc = cmds.internalVar(userScriptDir=True)
tpFolder = '/tp_race_generator'
sys.path.append(sc+tpFolder)

from lib import curva, car, ui
modules = [curva, car, ui]
def reload_it():
  for sub_module in modules:
    reload(sub_module)
reload_it()

#call ui:
i = curva.pathCreator()
c = car.carCreator()
ui.uiCreator()