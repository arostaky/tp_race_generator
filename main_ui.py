import maya.cmds as cmds
import sys
cmds.file(f=True, new=True)
sc = cmds.internalVar(userScriptDir=True)
tpFolder = '/tp_race_generator'
sys.path.append(sc+tpFolder)

from lib import test, curve, car, ui
modules = [test, curve, car, ui]
def reload_it():
  for sub_module in modules:
    #print ('Reloading %s' % sub_module)
    reload(sub_module)
reload_it()

#call ui:
i = curve.pathCreator()
c = car.carCreator()
ui.uiCreator()