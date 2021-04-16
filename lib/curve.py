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
        closedCurve = cmds.closeCurve( 'curve1', ch=True, ps=False, rpo = True )
        plano = cmds.polyPlane(sx=1,sy=1, n='rue',w=1,h=4)
        enterCurva = cmds.xform('curve1.cv[0]', q=True, t=True)
        cmds.move(enterCurva[0],enterCurva[1],enterCurva[2])
        cmds.select('rue')
        cmds.rotate(0,0,'90deg')
        cmds.select( clear=True )
        cmds.polyExtrudeFacet( 'rue.f[0]',inc='curve1', d=100,kft=1, constructionHistory=1, twist=0, thickness = 0, smoothingAngle=30, taper=1)
        cmds.polyNormal('rue.f[0:*]', nm=0)
    @classmethod
    def deleteAll(self):
        cmds.select('curve1','rue')
        cmds.delete()