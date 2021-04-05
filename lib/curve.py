# -*- coding: UTF-8 -*-
import maya.cmds as cmds

#étape 1: create a path, e,g, a curve
class pathCreator():
    @classmethod
    def createPath(self):
        curva = cmds.select('curve1')
        closedCurve = cmds.closeCurve( 'curve1', ch=True, ps=False, rpo = True )
        plano = cmds.polyPlane(sx=1,sy=1, n='rue',w=1,h=7)
        enterCurva = cmds.xform('curve1.cv[0]', q=True, t=True)
        #enterAcurva = cmds.xform('curve1.cv[0]',q=True, rp=True)
        #print('dime la rotation: ')
        #print(enterCurva[0])
        #print(enterAcurva)
        cmds.move(enterCurva[0],enterCurva[1],enterCurva[2])
        cmds.select('rue')
        cmds.rotate(0,0,'90deg')
        cmds.select( clear=True )
        cmds.polyExtrudeFacet( 'rue.f[0]',inc='curve1', d=100,kft=1, constructionHistory=1, twist=0, thickness = 0, smoothingAngle=30, taper=1)
        cmds.polyNormal('rue.f[0:*]', nm=0)
#polyExtrudeFacet -constructionHistory 1 -keepFacesTogether 1 -pvx -83.21590008 -pvy 0 -pvz -58.80080258 -divisions 1 -twist 0 -taper 1 -off 0 -thickness 0 -smoothingAngle 30 -inputCurve curve1  rue.f[0];
#polyNormal -normalMode 0 -userNormalMode 0 -ch 1 rue.f[0:401];
        #cmds.polyExtrudeFacet()
        
        # print('dime la curva: ')
        # print(enterCurva)
        # closedCurve = cmds.closeCurve( 'curve1', ch=True, ps=False, rpo = True )
        # duplicatedCurve = cmds.duplicateCurve(path, ch=False )
        # cmds.scale( 2, 2, 2, duplicatedCurve, pivot=(1, 0, 0), absolute=True )
        # cmds.loft(path, duplicatedCurve, ch=True, rn=True, ar=True, n='loftToConvert' )
        #cmds.nurbsToPoly('loftToConvert')
        #cmds.hide('loftToConvert')