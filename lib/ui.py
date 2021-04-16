import maya.cmds as cmds
sc = cmds.internalVar(userScriptDir=True)
tpFolder = '/tp_race_generator'
#-------UI:
class uiCreator():
    def __init__(self):
        self.dialog = cmds.loadUI(uiFile=sc+tpFolder+'/main.ui')
        self.windows = cmds.showWindow(self.dialog)
        cmds.button('SelectButt', edit=True, c='i.pathSelector()')
        cmds.button('CreateButt', edit=True, c='i.createPath()')
        cmds.button('EraseButt', edit=True, c='i.deleteAll()')
        cmds.button('RaceButt', edit=True, c='c.createCar()')

        #cmds.rename('Grp_Car_python', 'spinning_ball')