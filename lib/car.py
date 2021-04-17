# -*- coding: UTF-8 -*-
import maya.cmds as cmds
import random
sc = cmds.internalVar(userScriptDir=True)
tpFolder = '/tp_race_generator'
listNumbers = list(range(60,120))
randomSelection1 = random.choice(listNumbers)
randomSelection2 = random.choice(listNumbers)
randomSelection3 = random.choice(listNumbers)
class carCreator():

    # #call sliders:
    # carSlider1 = cmds.intSlider('CarSlider_1', q=True,v=True)
    # carSlider2 = cmds.intSlider('CarSlider_2', q=True,v=True)
    # carSlider3 = cmds.intSlider('CarSlider_3', q=True,v=True)
    # carSlider4 = cmds.intSlider('CarSlider_4', q=True,v=True)
    print(randomSelection1)
    @classmethod
    def createCarOne(self):
        carSlider1 = cmds.intSlider('CarSlider_1', q=True,v=True)
        print('slider car 1: ' + str(carSlider1))
        if (carSlider1 > 1):
            car1 = cmds.textField('NameCar1', q=True, text=True)
            cmds.file(sc +tpFolder+'/fbx/mercedes_rig.fbx', i = True, type='fbx')
            cmds.rename('Grp_Car_python', str(car1))
            cmds.pathAnimation('ctrl_Car_python', c='curve1', stu = 0, etu = randomSelection1, f = False, fa='Z' )
            cmds.keyTangent( 'motionPath1_uValue', ott='linear', itt='linear' )
            cmds.setAttr('motionPath1.worldUpType',0)
            cmds.setAttr('motionPath1.upAxis', 1)
    @classmethod
    def createCarTwo(self):
        carSlider2 = cmds.intSlider('CarSlider_2', q=True,v=True)
        print('slider car 2: ' + str(carSlider2))
        if (carSlider2 > 1):
            car2 = cmds.textField('NameCar2', q=True, text=True)
            cmds.file(sc +tpFolder+'/fbx/couper_rig.fbx', i = True, type='fbx')
            cmds.rename('Grp_Car_couper', str(car2))
            cmds.pathAnimation('ctrl_Car_couper', c='offsetNurbsCurve1', stu = 0, etu = randomSelection2, f = False, fa='Z' )
            cmds.keyTangent( 'motionPath2_uValue', ott='linear', itt='linear' )
            cmds.setAttr('motionPath2.worldUpType',0)
            cmds.setAttr('motionPath2.upAxis', 1)
    @classmethod
    def createCarThree(self):
        carSlider3 = cmds.intSlider('CarSlider_3', q=True,v=True)
        print('slider car 3: ' + str(carSlider3))
        if (carSlider3 > 1):
            car3 = cmds.textField('NameCar3', q=True, text=True)
            cmds.file(sc +tpFolder+'/fbx/Muscle_rig.fbx', i = True, type='fbx')
            cmds.rename('Grp_Car_Muscle', str(car3))
            cmds.pathAnimation('ctrl_Car_Muscle', c='offsetNurbsCurve2', stu = 0, etu = randomSelection3, f = False, fa='Z' )
            cmds.keyTangent( 'motionPath3_uValue', ott='linear', itt='linear' )
            cmds.setAttr('motionPath3.worldUpType',0)
            cmds.setAttr('motionPath3.upAxis', 1)
    @classmethod
    def createCarFour(self):
        carSlider4 = cmds.intSlider('CarSlider_4', q=True,v=True)
        print('slider car 4: ' + str(carSlider4))
        if (carSlider4 > 1):
            car4 = cmds.textField('NameCar3', q=True, text=True)
            cmds.file(sc +tpFolder+'/fbx/camaro_rig.fbx', i = True, type='fbx')
            cmds.rename('Grp_Car_Camaro', str(car4))
            cmds.pathAnimation('ctrl_Car_Camaro', c='offsetNurbsCurve3', stu = 0, etu = randomSelection3, f = False, fa='Z' )
            cmds.keyTangent( 'motionPath4_uValue', ott='linear', itt='linear' )
            cmds.setAttr('motionPath4.worldUpType',0)
            cmds.setAttr('motionPath4.upAxis', 1)
    @classmethod
    def createMeta(self):
        cmds.file(sc+tpFolder+'/fbx/meta.fbx', i=True, type='fbx')
        # enterCurva = cmds.xform('curve1.cv[0]', q=True, t=True)
        # cmds.select('ctrl_meta')
        # cmds.move(enterCurva[0],enterCurva[1],enterCurva[2])
        cmds.pathAnimation('ctrl_meta', c='curve1', stu = 0, etu = 0, f = False )
        cmds.keyTangent( 'motionPath1_uValue', ott='linear', itt='linear' )
        cmds.setAttr('motionPath1.worldUpType',0)
        cmds.setAttr('motionPath1.upAxis', 1)
    @classmethod
    def createCars(self):
        self.createCarOne()
        self.createCarTwo()
        self.createCarThree()
        self.createCarFour()
        self.createMeta()

#    car2 = cmds.textField('NameCar2', q=True, text=True)
#         car3 = cmds.textField('NameCar3', q=True, text=True)
#         car4 = cmds.textField('NameCar4', q=True, text=True)
#---------- MEL SOLUTION for position:
# select -r Grp_Car_python ;
# select -r ctrl_Car_python ;
# setAttr "motionPath1.worldUpType" 0;
# setAttr "motionPath1.upAxis" 1;
#
