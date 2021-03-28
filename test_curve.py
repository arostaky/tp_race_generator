import maya.cmds as cmds
cmds.file(f=True, new=True)
#étape 1: create a path, e,g, a curve
path = cmds.curve(n='curve1',d=3,p=[(-10, 0, 0),(5, 0, 15),(1, 0, -10),(10, 2, 0)],k=[0, 0, 0, 1, 1, 1])
closedCurve = cmds.closeCurve( 'curve1', ch=True, ps=True, rpo = True )
duplicatedCurve = cmds.duplicateCurve( closedCurve, ch=False )
cmds.scale( 2, 2, 2, duplicatedCurve, pivot=(1, 0, 0), absolute=True )
cmds.loft(closedCurve, duplicatedCurve, ch=True, rn=True, ar=True, n='loftToConvert' )
cmds.nurbsToPoly('loftToConvert')
cmds.hide('loftToConvert')
#repeat and play:
mypath1 = cmds.curve(d = 1, p = [(12,0,12),(12,0,-12),(-12,0,-12),(-12,0,12),(12,0,12)])
duplicatedCurve2 = cmds.duplicateCurve( mypath1, ch=False )
cmds.scale( 1.3, 1.3, 1.3, duplicatedCurve2, pivot=(1, 0, 0), absolute=True )
cmds.loft(mypath1, duplicatedCurve2, ch=True, rn=True, ar=True, n='loftToConvert2' )
cmds.nurbsToPoly('loftToConvert2')
mypath2 = cmds.curve(d = 1, p = [(10,0,10),(10,0,-10),(-10,0,-10),(-10,0,10),(10,0,10)])
duplicatedCurve3 = cmds.duplicateCurve( mypath2, ch=False )
cmds.scale( 1.2, 1.2, 1.2, duplicatedCurve3, pivot=(1, 0, 0), absolute=True )
cmds.loft(mypath2, duplicatedCurve3, ch=True, rn=True, ar=True, n='loftToConvert3' )
cmds.nurbsToPoly('loftToConvert3')
cmds.hide('loftToConvert')
cmds.hide('loftToConvert2')
cmds.hide('loftToConvert3')
#étape 2: create objs et anim avec le curve

#mypath3 = cmds.curve(d = 1, p = [(8,0,8),(8,0,-8),(-8,0,-8),(-8,0,8),(8,0,8)])
myCube1 = cmds.polyCube(w = 1.5)
#cmds.pathAnimation(mySphere1[0], c = mypath1, stu = 0, etu = 120, f = True)
myCube2 = cmds.polyCube(w = 0.5)
#cmds.pathAnimation(mySphere2[0], c = mypath2, stu = 0, etu = 120, f = True)
mySphere3 = cmds.polySphere(r = 1)
cmds.pathAnimation(myCube1[0], c=mypath1, stu = 0, etu = 120, f = True )
cmds.pathAnimation(myCube2[0], c=mypath2, stu = 10, etu = 120, f = True )
cmds.pathAnimation(mySphere3[0], c=path, stu = 20, etu = 120, f = True )
