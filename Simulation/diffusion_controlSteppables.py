
from PySteppables import *
import CompuCell
import sys
from random import randint

class diffusion_controlSteppable(SteppableBasePy):

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)

        
    def start(self):
        fgf = self.getConcentrationField('FGF')
        
        for cell in self.cellList:
            cell.type = self.A
            cell.targetVolume = 10.0
            cell.lambdaVolume = 10.0
            
        for cell in self.cellList:
            cell.type = self.B
            break
            
            
        
        #assign field value
#         fgf[50,50,0] = 2000.0
        
        
    def step(self,mcs):        
        #type here the code that will run every _frequency MCS
        for cell in self.cellList:
            print "cell.id=",cell.id
    def finish(self):
        # Finish Function gets called after the last MCS
        pass
        