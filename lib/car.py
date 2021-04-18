# -*- coding: UTF-8 -*-
import maya.cmds as cmds
import random
sc = cmds.internalVar(userScriptDir=True)
tpFolder = '/tp_race_generator'
listNumbers = list(range(60,120))
randomSelection1 = random.choice(listNumbers)
randomSelection2 = random.choice(listNumbers)
randomSelection3 = random.choice(listNumbers)
randomSelection4 = random.choice(listNumbers)
class carCreator():
    print(randomSelection1)
    @classmethod
    def listCarsMethod(self):
        global carSlider1, carSlider2, carSlider3, carSlider4
        carSlider1 = cmds.intSlider('CarSlider_1', q=True,v=True)
        carSlider2 = cmds.intSlider('CarSlider_2', q=True,v=True)
        carSlider3 = cmds.intSlider('CarSlider_3', q=True,v=True)
        carSlider4 = cmds.intSlider('CarSlider_4', q=True,v=True)
        listCars = [carSlider1, carSlider2, carSlider3, carSlider4]
        realListCars = []
        #obtain the list of active cars:
        for i in range(len(listCars)):
            if(listCars[i]>1):
                # print('estos son los carros:'+ str(listCars[i]))
                realListCars.append(listCars[i])
        #use the value:
        return realListCars
    @classmethod
    def createMotionPath(self, val):
        v = str(val)
        cmds.keyTangent( 'motionPath'+v+'_uValue', ott='linear', itt='linear' )
        cmds.setAttr('motionPath'+v+'.worldUpType',0)
        cmds.setAttr('motionPath'+v+'.upAxis', 1)
    @classmethod
    def importCars(self, val, oval):
        filesImport = ['/fbx/mercedes_rig.fbx', '/fbx/couper_rig.fbx', '/fbx/Muscle_rig.fbx', '/fbx/camaro_rig.fbx']
        carNames = ['python','couper','Muscle','Camaro']
        curveNames = ['curve1','offsetNurbsCurve1','offsetNurbsCurve2','offsetNurbsCurve3']
        randomC = [randomSelection1, randomSelection2, randomSelection3, randomSelection4]
        car = cmds.textField('NameCar'+str(val), q=True, text=True)
        cmds.file(sc +tpFolder+filesImport[oval], i = True, type='fbx')
        cmds.rename('Grp_Car_'+carNames[oval], str(car))
        cmds.pathAnimation('ctrl_Car_'+carNames[oval], c=curveNames[oval], stu = 0, etu = randomC[oval], f = False, fa='Z' )
    @classmethod
    def createMeta(self):
        cmds.file(sc+tpFolder+'/fbx/meta.fbx', i=True, type='fbx')
        cmds.pathAnimation('ctrl_meta', c='curve1', stu = 0, etu = 0, f = True, wut = 0, fa = 'Z', ua = 'Y')
        self.createMotionPath(1)
    @classmethod
    def createCars(self):
        print('este es el metodo: '+ str(self.listCarsMethod()))
        carList = self.listCarsMethod()
        print('que tan larga es la lista? '+str(len(carList)))
        print('que valores hay en la lista? '+ str(carList[:]))

        #remove duplicates from list:
        carCleanList = set(carList)
        cList = []
        for x in carCleanList:
            cList.append(x)
        
        #-------------------------------------
        for i in range(len(cList)):
            if(cList[i] == 2 ):
                self.importCars(cList[i]-1,cList[i]-2)
                self.createMotionPath(i+1)
            if(cList[i] == 3):
                self.importCars(cList[i]-1,cList[i]-2)
                self.createMotionPath(i+1)
            if(cList[i] == 4):
                self.importCars(cList[i]-1,cList[i]-2)
                self.createMotionPath(i+1)
            if(cList[i] == 5):
                self.importCars(cList[i]-1,cList[i]-2)
                self.createMotionPath(i+1)
        #----------------------------------------
        self.createMeta()