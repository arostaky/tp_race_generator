import sys
import maya.cmds as cmds 
import maya.mel as mel
import random
sys.path.append('C:\Users\wassi\OneDrive\Bureau')
cmds.file(f=True, new=True)






#Importation de de UI 
dialog = cmds.loadUI(uiFile='C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Generateur.ui')

cmds.showWindow(dialog)




#affectation slider a des Var



#carNum = mel.eval("intSlider -q -v CarSlider")   ############ mel
#carNum = cmds.intSlider('CarSlider',q=True,v=True) ##########python

#PotNum= cmds.intSlider('PotSlider', query=True, value=True)




# Main  
def Generate(*args):
    
    carNum = cmds.intSlider('CarSlider',q=True,v=True)
    
    pneuNum=cmds.intSlider('PneuSlider',q=True,v=True)
#Menu  
    if carNum ==1 :
        cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Carross1.ma' ,i=True ) 
        
        if pneuNum==1:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu1F1.ma' ,i=True )
            cmds.parent('Carrosserie1','Control')
            
        
        elif pneuNum==2:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu2F1.ma' ,i=True)
            cmds.parent('Carrosserie1','Control')
        
        elif pneuNum==3:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu3F1.ma' ,i=True)
            cmds.parent('Carrosserie1','Control')
            
        elif pneuNum==4:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu4F1.ma' ,i=True)
            cmds.parent('Carrosserie1','Control')
    
    
    
    elif carNum ==2:
        cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Carross2.ma' ,i=True) 
        
        if pneuNum==1:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu1F2.ma' ,i=True)
            cmds.parent('Carrosserie2','Control')
        
        elif pneuNum==2:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu2F2.ma' ,i=True)
            cmds.parent('Carrosserie2','Control')
        
        elif pneuNum==3:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu3F2.ma' ,i=True)
            cmds.parent('Carrosserie2','Control')
        
        elif pneuNum==4:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu4F2.ma' ,i=True)
            cmds.parent('Carrosserie2','Control')


    elif carNum ==3:
        cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Carross3.ma' ,i=True) 
        if pneuNum==1:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu1F3.ma' ,i=True)
            cmds.parent('Carrosserie3','Control')

        elif pneuNum==2:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu2F3.ma' ,i=True)
            cmds.parent('Carrosserie3','Control')

        elif pneuNum==3:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu3F3.ma' ,i=True)
            cmds.parent('Carrosserie3','Control')

        elif pneuNum==4:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu4F3.ma' ,i=True)
            cmds.parent('Carrosserie3','Control')
    
    
    else :
        cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Carross4.ma' ,i=True) 
        if pneuNum==1:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu1F4.ma' ,i=True)
            cmds.parent('Carrosserie4','Control')
        elif pneuNum==2:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu2F4.ma' ,i=True)
            cmds.parent('Carrosserie4','Control')
        elif pneuNum==3:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu3F4.ma' ,i=True)
            cmds.parent('Carrosserie4','Control')
        elif pneuNum==4:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu4F4.ma' ,i=True)
            cmds.parent('Carrosserie4','Control')
    
    
    
 
    print carNum
   
    print pneuNum

    
    cmds.deleteUI(dialog)
    
        
cmds.button('Generate', edit=True,command =Generate)

def Randomize(*args):
    
    carNum = random.randint(1,4)
    
    pneuNum= random.randint(1,4)
#Menu  
    if carNum ==1 :
        cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Carross1.ma' ,i=True ) 
        
        if pneuNum==1:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu1F1.ma' ,i=True )
            cmds.parent('Carrosserie1','Control')
            
        
        elif pneuNum==2:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu2F1.ma' ,i=True)
            cmds.parent('Carrosserie1','Control')
        
        elif pneuNum==3:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu3F1.ma' ,i=True)
            cmds.parent('Carrosserie1','Control')
            
        elif pneuNum==4:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu4F1.ma' ,i=True)
            cmds.parent('Carrosserie1','Control')
    
    
    
    elif carNum ==2:
        cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Carross2.ma' ,i=True) 
        
        if pneuNum==1:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu1F2.ma' ,i=True)
            cmds.parent('Carrosserie2','Control')
        
        elif pneuNum==2:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu2F2.ma' ,i=True)
            cmds.parent('Carrosserie2','Control')
        
        elif pneuNum==3:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu3F2.ma' ,i=True)
            cmds.parent('Carrosserie2','Control')
        
        elif pneuNum==4:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu4F2.ma' ,i=True)
            cmds.parent('Carrosserie2','Control')


    elif carNum ==3:
        cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Carross3.ma' ,i=True) 
        if pneuNum==1:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu1F3.ma' ,i=True)
            cmds.parent('Carrosserie3','Control')

        elif pneuNum==2:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu2F3.ma' ,i=True)
            cmds.parent('Carrosserie3','Control')

        elif pneuNum==3:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu3F3.ma' ,i=True)
            cmds.parent('Carrosserie3','Control')

        elif pneuNum==4:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu4F3.ma' ,i=True)
            cmds.parent('Carrosserie3','Control')
    
    
    else :
        cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Carross4.ma' ,i=True) 
        if pneuNum==1:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu1F4.ma' ,i=True)
            cmds.parent('Carrosserie4','Control')
        elif pneuNum==2:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu2F4.ma' ,i=True)
            cmds.parent('Carrosserie4','Control')
        elif pneuNum==3:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu3F4.ma' ,i=True)
            cmds.parent('Carrosserie4','Control')
        elif pneuNum==4:
            cmds.file( 'C:\Users\wassi\OneDrive\Bureau\Projet\Code\Kart_Gen\Pneu4F4.ma' ,i=True)
            cmds.parent('Carrosserie4','Control')
    
    
    
 
    print carNum
   
    print pneuNum

    
    cmds.deleteUI(dialog)
    


cmds.button('Random', edit=True,command =Randomize)