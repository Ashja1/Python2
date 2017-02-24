
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class Boids(object):
    def __init__(self, config, count=0, fly_to_middle=0, alert_distance=0, 
				formation_flying_distance=0, formation_flying_strength=0): 
		
		

    def new_flock(self, count, lower_limits, upper_limits):
        width=upper_limits-lower_limits
        return (lower_limits[:,np.newaxis] + 
            np.random.rand(2, count)*width[:,np.newaxis])
        

    def fly_towards_middle(self, strength):
        

    def avoid_nearby_boids(self, alert_distance):
        
    def match_speeds(self, formation_flying_distance, formation_flying_strength):
   	    
       

    def update_boids(self):
        

    def animate(self,frame, scatter):
        

    def simulate(self):
        


