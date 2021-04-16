import maya.cmds as cmds
sc = cmds.internalVar(userScriptDir=True)
tpFolder = '/tp_race_generator'
#-------UI:
class uiCreator():
    def __init__(self):
        self.dialog = cmds.loadUI(uiFile=sc+tpFolder+'/main.ui')
        self.windows = cmds.showWindow(self.dialog)
        cmds.button('SelectButt', edit=True, c='pathselector()')


def pathselector(self):
    print('algo')
        #cmds.select('curve1')

#i = Interactor()