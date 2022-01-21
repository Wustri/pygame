#calls the neccesary imports
import pygame, random


#class to control the particles
class Particle:
	#create the neccesary variables
	def __init__(self , Screen ) -> None:
		self.screen = Screen
		self.particles = [] 
        
	#def to update the position of the particles
	def emit(self):
		if self.particles:
			self.delete_particles()
			for particle in self.particles:
				#update the position
				particle[0][1] += particle[2][0]
				particle[0][0] += particle[2][1]
				particle[1] -= 0.2


				Surface = pygame.Surface((2,2), pygame.SRCALPHA)
				Surface.fill((129,169,40,100)) 
				self.screen.blit(Surface, particle[0])


	#def to create ew particles when neccesary
	def add_particles(self,x,y):
		pos_x = x
		pos_y = y
		radius = 2
		#start at a random direction
		direction_x = random.randint(-3,3)
		direction_y = random.randint(-1,1)
		particle_circle = [[pos_x,pos_y],radius,[direction_x,direction_y]]
		#add it to the list to update it
		self.particles.append(particle_circle)

	#delete particles after a set time
	def delete_particles(self):
		particle_copy = [particle for particle in self.particles if particle[1] > 0]
		self.particles = particle_copy