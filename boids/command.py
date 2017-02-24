from argparse import ArgumentParser
import yaml
from StringIO import StringIO
from boids import Boids

def process():
    parser = ArgumentParser(description = "Refactored Boid")
    parser.add_argument('--config', '-c', type=str, default="config.cfg",  help="Config YAML file")
    
    arguments= parser.parse_args()
    
    
    cfg={}
	#default values 
    default="""Boids:
  count: 50
  vxlim: [0, 10]
  vylim: [-20, 20]
  xlim: [-450, 50]
  ylim: [300, 600]
Dynamics:
  alert_distance: 100
  fly_to_middle_strength: 0.01
  formation_flying_strength: 0.125
  formation_flying_distance: 10000
Animation:
  frames: 50
  interval: 50
  xlim: [-500, 1500]
  ylim: [-500, 1500]"""
    

    #open given cfg file within try block to catch wrong filename etc.
    try:
		with open(arguments.config) as cfg_file:
			cfg=yaml.load(cfg_file)
            
    except:
        #use default settings if no or wrong config file given!
        print "Error reading config file. Default values used to run the program"
        print default
        cfg=yaml.load(StringIO(default))
    
    
    #run boids simulation with given settings
    boids=Boids(cfg, cfg['Boids']['count'], cfg['Dynamics']['fly_to_middle_strength'], 
				cfg['Dynamics']['alert_distance'], 
				cfg['Dynamics']['formation_flying_distance'],
				cfg['Dynamics']['formation_flying_strength'])
    boids.simulate()


if __name__ == "__main__":
    process()

