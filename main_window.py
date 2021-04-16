import maya.cmds as cmds
import sys
sc = cmds.internalVar(userScriptDir=True)
cmds.file(f=True, new=True)
sys.path.append(sc+ '/tp_race_generator')

from lib import test, curve, car
modules = [test, curve, car]
def reload_it():
  for sub_module in modules:
    #print ('Reloading %s' % sub_module)
    reload(sub_module)
reload_it()
# test.testTwo()

#------------------------------------------------------
winName = 'Race Generator'
winWidth = 1024 
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Race Generator')
#reference to the main columnLayout
dc = 255.0
grisObscuro = [37/dc,38/dc,37/dc]
grisClaro = [99/dc,106/dc,115/dc]
rougeFounce = [115/dc,37/dc,20/dc]
bgColorB = [255/dc,33/dc,33/dc]
bgColorB2 = [31/dc,15/dc,3/dc]
winName = 'Main_Window'
winWidth = 1050 
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Race Generator', bgc=(grisObscuro))
mainCL = cmds.columnLayout() 
cmds.rowLayout(numberOfColumns=2, columnWidth2=(500, 500))
cmds.text(label='1 Draw Curve....', w=500)
cmds.text(label='...', w=500)
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=(500, 500))
cmds.text(label='2 Choose Cars....', w=500)
cmds.text(label='...', w=500)
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=(500, 500))
cmds.iconTextStaticLabel( st='iconAndTextVertical', i1=sc + '/tp_race_generator/imgs/car_1.png', l='Car 1', al='right', w=500)
cmds.iconTextStaticLabel( st='iconAndTextVertical', i1=sc + '/tp_race_generator/imgs/car_2.png', l='Car 2', w=500)
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=(500, 500))
cmds.textFieldGrp('newName', label = 'Car Name 1: ', width=500)
cmds.textFieldGrp('newName2', label = 'Car Name 2: ', width=500)
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=(500, 500))
cmds.floatSliderGrp( label='Speed C1', field=True, minValue=1, maxValue=4, fieldMinValue=1, fieldMaxValue=4, value=1 )
cmds.floatSliderGrp( label='Speed C2', field=True, minValue=1, maxValue=4, fieldMinValue=1, fieldMaxValue=4, value=1 )
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=(500, 500))
cmds.floatSliderGrp( label='Size C1', field=True, minValue=1, maxValue=4, fieldMinValue=1, fieldMaxValue=4, value=1 )
cmds.floatSliderGrp( label='Size C2', field=True, minValue=1, maxValue=4, fieldMinValue=1, fieldMaxValue=4, value=1 )
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=(500, 500))
cmds.colorSliderButtonGrp( label='Color C1:', buttonLabel='C1', rgb=(1, 0, 0), symbolButtonDisplay=True, columnWidth=(5, 30), image='navButtonUnconnected.xpm' )
cmds.colorSliderButtonGrp( label='Color C2:', buttonLabel='C2', rgb=(1, 0, 0), symbolButtonDisplay=True, columnWidth=(5, 30), image='navButtonUnconnected.xpm' )
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=(500, 500))
cmds.rowLayout(numberOfColumns=2, columnWidth2=(200, 250))
cmds.text('')
cmds.button(label='Import 1', width=100, align='center', bgc=rougeFounce, c='car.carCreator.createCar()')
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=(200, 250))
cmds.text('')
cmds.button(label='Import 2', width=100, align='center', bgc=rougeFounce)
cmds.setParent('..')
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=(500, 500))
cmds.rowLayout(numberOfColumns=2, columnWidth2=(120, 250))
cmds.text('')
cmds.button(label='Create Path', width=250, align='center',bgc=rougeFounce, c='curve.pathCreator.createPath()')
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=(120, 250))
cmds.text('')
cmds.button(label='Race!', width=250, align='center',bgc=rougeFounce, c='car.carCreator.animateCar()')
cmds.setParent('..')
cmds.showWindow(winName)
cmds.window(winName, e=True, width=winWidth, height=450)