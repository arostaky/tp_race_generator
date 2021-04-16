# -*- coding: UTF-8 -*-
import maya.cmds as cmds
import random
sc = cmds.internalVar(userScriptDir=True)
tpFolder = '/tp_race_generator'
#étape 1: create a path, e,g, a curve

 
class carCreator():
    listNumbers = list(range(250))
    randomSelection = random.choice(listNumbers)
    print(randomSelection)
    @classmethod
    def createCar(self):
        mercedes = cmds.file(sc +tpFolder+'/fbx/mercedes_rig.fbx', i = True, type='fbx')
        
    @classmethod
    def animateCar(self):
        cmds.pathAnimation('ctrl_Car_python', c='curve1', stu = 0, etu = 120, f = False, fa='Z' )
        cmds.keyTangent( 'motionPath1_uValue', ott='linear', itt='linear' )
        cmds.setAttr('motionPath1.worldUpType',0)
        cmds.setAttr('motionPath1.upAxis', 1)

#---------- MEL SOLUTION for position:
# select -r Grp_Car_python ;
# select -r ctrl_Car_python ;
# setAttr "motionPath1.worldUpType" 0;
# setAttr "motionPath1.upAxis" 1;
#
