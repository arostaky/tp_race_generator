import maya.cmds as cmds
sc = cmds.internalVar(userScriptDir=True)
tpFolder = '/tp_race_generator'
#-------UI:
class uiCreator():
    def __init__(self):
        #etape 1:
        self.dialog = cmds.loadUI(uiFile=sc+tpFolder+'/main.ui')
        self.windows = cmds.showWindow(self.dialog)
        #etape 2:
        cmds.button('SelectButt', edit=True, c='i.pathSelector()')
        cmds.button('CreateButt', edit=True, c='i.createPath()')
        cmds.button('EraseButt', edit=True, c='i.deleteAll()')
        #etape 3:
        #car variables
        #etape 4:
        cmds.button('RaceButt', edit=True, c='c.createCars()')
