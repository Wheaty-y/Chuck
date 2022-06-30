from tools import  *
from objects import *
from routines import *


#This file is for strategy

class Chuck(GoslingAgent): 
    def run(agent): #Just mad drifting here
        agent.controller.throttle = .5
        agent.controller.steer = 1
        agent.controller.handbrake = True
        
