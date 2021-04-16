import maya.cmds as cmds
import sys
cmds.file(f=True, new=True)
sc = cmds.internalVar(userScriptDir=True)
tpFolder = '/tp_race_generator'
sys.path.append(sc+tpFolder)

from lib import test, curve, car
modules = [test, curve, car]
def reload_it():
  for sub_module in modules:
    #print ('Reloading %s' % sub_module)
    reload(sub_module)
reload_it()

#call ui:

def pathselector(*args):
    print('algo')
    #cmds.select('curve1')

dialog = cmds.loadUI(uiFile=sc+tpFolder+'/main.ui')
windows = cmds.showWindow(dialog)
cmds.button('SelectButt', edit=True, c=pathselector)
cmds.button('CreateButt', edit=True, c=pathselector)