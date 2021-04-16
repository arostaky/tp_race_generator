# -*- coding: UTF-8 -*-
import random
import maya.cmds as cmds

sc = cmds.internalVar(userScriptDir=True)
#étape 1: create a path, e,g, a curve
#print(sc+'tp_race_generator/fbx/couper.fbx')
 
class carCreator():
    listNumbers = list(range(250))
    randomSelection = random.choice(listNumbers)
    print(randomSelection)
    @classmethod
    def createCar(self):
        couper = cmds.file(sc +'tp_race_generator/ma/mercedes_rig.ma', i = True)
        # cmds.scale(0.1,0.1,0.1, 'Car_Python', ws=True, a=True)
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
#----------------
