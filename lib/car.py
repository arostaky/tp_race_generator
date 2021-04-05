# -*- coding: UTF-8 -*-
import maya.cmds as cmds
sc = cmds.internalVar(userScriptDir=True)
#étape 1: create a path, e,g, a curve
#print(sc+'tp_race_generator/fbx/couper.fbx')
couper = cmds.file(sc +'tp_race_generator/fbx/mercedes_rig.fbx', i = True, type = 'fbx')  
class carCreator():
    @classmethod
    def createCar(self):
        cmds.pathAnimation('ctrl_Car_python', c='curve1', stu = 0, etu = 120, f = False, fa='Z' )

#---------- MEL SOLUTION for position:
# select -r Grp_Car_python ;
# select -r ctrl_Car_python ;
# setAttr "motionPath1.worldUpType" 0;
# setAttr "motionPath1.upAxis" 1;
#
#----------------
