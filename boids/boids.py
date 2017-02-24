
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class Boids(object):
    def __init__(self, config, count=0, fly_to_middle=0, alert_distance=0, 
				formation_flying_distance=0, formation_flying_strength=0): 
		#get config 
		self.config=config
		
		
		self.boid_count=count
		self.fly_to_middle = fly_to_middle
		self.alert_distance = alert_distance
		self.formation_flying_distance = formation_flying_distance
		self.formation_flying_strength = formation_flying_strength
		self.position_lower_limit=np.array([self.config['Boids']['xlim'][0], self.config['Boids']['ylim'][0]])
		self.position_upper_limit=np.array([self.config['Boids']['xlim'][1], self.config['Boids']['ylim'][1]])
		self.velocity_lower_limit=np.array([self.config['Boids']['vxlim'][0], self.config['Boids']['vylim'][0]])
		self.velocity_upper_limit=np.array([self.config['Boids']['vxlim'][1], self.config['Boids']['vylim'][1]]) 
		
		

    def new_flock(self, count, lower_limits, upper_limits):
        width=upper_limits-lower_limits
        return (lower_limits[:,np.newaxis] + 
            np.random.rand(2, count)*width[:,np.newaxis])
        

    def fly_towards_middle(self, strength):
        # Fly towards the middle
        middle=np.mean(self.positions, 1)
        direction_to_middle = self.positions - middle[:, np.newaxis]
        self.velocities -= direction_to_middle * strength

    def avoid_nearby_boids(self, alert_distance):
        # Fly away from nearby boids
        separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        far_away = square_distances > alert_distance
        separations_if_close = np.copy(separations)
        separations_if_close[0,:,:][far_away] =0
        separations_if_close[1,:,:][far_away] =0
        self.velocities += np.sum(separations_if_close,1) 

    def match_speeds(self, formation_flying_distance, formation_flying_strength):
   	    # Try to match speed with nearby boids
        separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        velocity_differences = self.velocities[:,np.newaxis,:] - self.velocities[:,:,np.newaxis]
        very_far=square_distances > formation_flying_distance
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[0,:,:][very_far] =0
        velocity_differences_if_close[1,:,:][very_far] =0
        return (-1) * np.mean(velocity_differences_if_close, 1) * formation_flying_strength
   	    
       

    def update_boids(self):
        

    def animate(self,frame, scatter):
        

    def simulate(self):
        


