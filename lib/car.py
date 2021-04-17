# -*- coding: UTF-8 -*-
import maya.cmds as cmds
import random
sc = cmds.internalVar(userScriptDir=True)
tpFolder = '/tp_race_generator'

class carCreator():
    listNumbers = list(range(250))
    randomSelection = random.choice(listNumbers)
    #call sliders:
    # carSlider1 = cmds.intSlider('CarSlider_1', q=True,v=True)
    # carSlider2 = cmds.intSlider('CarSlider_1', q=True,v=True)
    # carSlider3 = cmds.intSlider('CarSlider_1', q=True,v=True)
    # carSlider4 = cmds.intSlider('CarSlider_1', q=True,v=True)
    print(randomSelection)
    @classmethod
    def createCarOne(self):
        carSlider1 = cmds.intSlider('CarSlider_1', q=True,v=True)
        print('slider car 1: ' + str(carSlider1))
        if (carSlider1 > 1):
            car1 = cmds.textField('NameCar1', q=True, text=True)
            cmds.file(sc +tpFolder+'/fbx/mercedes_rig.fbx', i = True, type='fbx')
            cmds.rename('Grp_Car_python', str(car1))
    @classmethod
    def createCarTwo(self):
        carSlider2 = cmds.intSlider('CarSlider_2', q=True,v=True)
        print('slider car 2: ' + str(carSlider2))
        if (carSlider2 > 1):
            car2 = cmds.textField('NameCar2', q=True, text=True)
            cmds.file(sc +tpFolder+'/fbx/couper_rig.fbx', i = True, type='fbx')
            cmds.rename('Grp_Car_couper', str(car2))
    @classmethod
    def createCarThree(self):
        carSlider3 = cmds.intSlider('CarSlider_3', q=True,v=True)
        print('slider car 3: ' + str(carSlider3))
        if (carSlider3 > 1):
            car3 = cmds.textField('NameCar3', q=True, text=True)
            cmds.file(sc +tpFolder+'/fbx/Muscle_rig.fbx', i = True, type='fbx')
            cmds.rename('Grp_Car_Muscle', str(car3))
    @classmethod
    def animateCars(self):
        #car 1:
        cmds.pathAnimation('ctrl_Car_python', c='curve1', stu = 0, etu = 120, f = False, fa='Z' )
        cmds.keyTangent( 'motionPath1_uValue', ott='linear', itt='linear' )
        cmds.setAttr('motionPath1.worldUpType',0)
        cmds.setAttr('motionPath1.upAxis', 1)
        #car 2:
        cmds.pathAnimation('ctrl_Car_couper', c='offsetNurbsCurve1', stu = 0, etu = 120, f = False, fa='Z' )
        cmds.keyTangent( 'motionPath1_uValue', ott='linear', itt='linear' )
        cmds.setAttr('motionPath1.worldUpType',0)
        cmds.setAttr('motionPath1.upAxis', 1)
        #car3:
        cmds.pathAnimation('ctrl_Car_Muscle', c='offsetNurbsCurve2', stu = 0, etu = 120, f = False, fa='Z' )
        cmds.keyTangent( 'motionPath1_uValue', ott='linear', itt='linear' )
        cmds.setAttr('motionPath1.worldUpType',0)
        cmds.setAttr('motionPath1.upAxis', 1)
    @classmethod
    def createCars(self):
        self.createCarOne()
        self.createCarTwo()
        self.createCarThree()
        self.animateCars()

#    car2 = cmds.textField('NameCar2', q=True, text=True)
#         car3 = cmds.textField('NameCar3', q=True, text=True)
#         car4 = cmds.textField('NameCar4', q=True, text=True)
#---------- MEL SOLUTION for position:
# select -r Grp_Car_python ;
# select -r ctrl_Car_python ;
# setAttr "motionPath1.worldUpType" 0;
# setAttr "motionPath1.upAxis" 1;
#
