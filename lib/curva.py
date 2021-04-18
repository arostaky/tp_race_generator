# -*- coding: UTF-8 -*-
import maya.cmds as cmds

#étape 1: create a path, e,g, a curve
class pathCreator():
    global curva
    @classmethod
    def pathSelector(self):
            print('algo')
            curva = cmds.select('curve1')
    @classmethod
    def createPath(self):

        #cosas raras (parte 1):
        carSlider1 = cmds.intSlider('CarSlider_1', q=True,v=True)
        carSlider2 = cmds.intSlider('CarSlider_2', q=True,v=True)
        carSlider3 = cmds.intSlider('CarSlider_3', q=True,v=True)
        carSlider4 = cmds.intSlider('CarSlider_4', q=True,v=True)
        listCars = [carSlider1, carSlider2, carSlider3, carSlider4]
        global sizeRue 
        realListCars = []
        #obtain the list of active cars:
        for i in range(len(listCars)):
            if(listCars[i]>1):
                # print('estos son los carros:'+ str(listCars[i]))
                realListCars.append(listCars[i])
      
        #use the value:
        # print('estos son los verdaderos carros:'+ str(realListCars))
        amountCars = len(realListCars)
        closedCurve = cmds.closeCurve( 'curve1', ch=True, ps=False, rpo = True )
        #offset:
        # if(amountCars == 2):
        #     off1 = cmds.offsetCurve('curve1', d=2.0)
        # if(amountCars == 3):
        #     off1 = cmds.offsetCurve('curve1',d=-2.0)
        #     off2 = cmds.offsetCurve('curve1',d=2.0)
        # if(amountCars == 4):
        #     off1 = cmds.offsetCurve('curve1',d=-2.0)
        #     off2 = cmds.offsetCurve('curve1',d=2.0)
        #     off3 = cmds.offsetCurve('curve1',d=4.0)
        # if(amountCars == 5):
        off1 = cmds.offsetCurve('curve1',d=-2.0)
        off2 = cmds.offsetCurve('curve1',d=2.0)
        off3 = cmds.offsetCurve('curve1',d=4.0)
        off4 = cmds.offsetCurve('curve1',d=6.0)

        plano = cmds.polyPlane(sx=1,sy=1, n='rue',w=1,h=4*(amountCars/1.6)) #h variable width according to the amount of cars
        
        enterCurva = cmds.xform('curve1.cv[0]', q=True, t=True)
        cmds.move(enterCurva[0],enterCurva[1],enterCurva[2])
        cmds.select('rue')
        cmds.rotate(0,0,'90deg')
        cmds.select( clear=True )
        cmds.polyExtrudeFacet( 'rue.f[0]',inc='curve1', d=100,kft=1, constructionHistory=1, twist=0, thickness = 0, smoothingAngle=30, taper=1)
        cmds.polyNormal('rue.f[0:*]', nm=0)
    @classmethod
    def deleteAll(self):
        cmds.select(all=True)
        cmds.delete()