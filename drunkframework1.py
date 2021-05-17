# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:26:42 2021

@author: andre
"""

# Import relevant libraries 

# Import the random library to allow access to random modules and function which will be used to generate 
# pseudo-random numbers
import random



# Create the drunk class - this contains all of the relevant variables and functions to allow the drunks to 
# move around the town and find their way home. This uses the __init__ method to define drunk atributes.
class Drunks:
    def __init__(self, density, identifier, pub_x, pub_y, drunks, town):
        
        """Creates a drunk
        
        Arguments:
            pub_x (number): x-coordinate of drunks starting location
            pub_y (number): y-coordinate of drunks starting location
            identifier(number): value given to identify drunks and which home they have to find
            density (2D list): map of the drunks movements
            town (2D list): the environment drunks move around
        """
        
        # Define the coordinates for centre of the pubs which is where all the drunks will start
        # when making their journey's home. The values of the pub_x and pub_y variables are defined in the 
        # model.
        self._x = pub_x           
        self._y = pub_y     
        
        # Assign each drunk an identifier which determines which house they have to reach. The identifier
        # variable is defined in the model. 
        self.identifier = identifier   
        
        # Set up variable, density, to record and store where the drunks have walked when making their way 
        # home to ultimately allow this to be plotted on a density map.
        self.density = density  
        
        # Set up a variable to use when calling on the drunks to perform certain behaviours
        self.drunks = drunks
        
        # The next two variables should be uncommented if the user wishes to perfect the code to stop agents 
        # re-tracing their steps. 
        # Self.visited creates a dictionary to store self._x and self._y variables relating to where the drunks
        # have been. 
        #self.locationvisited = {(self._x, self._y)}
        # Self.town sets up the environment which drunks will navigate their way around. This should be called in the
        # init function if the user wishes to stop drunks retracing their steps. 
        self.town = town
        
        
        
# Create a walk_home() function within the Agent class. 
# The code will randomly alter the self._x and self._y coordinates using control flow (if-else) statements.
# This will allow agents to randomly move around the town either up, down, left or right, depending on what 
# conditions are met, until drunks find their homes.     
# To deal with boundary issues and stop drunks going missing from the town, a torus method is used.
# To do this, the code uses a modulus operator (%). This is set to the length of the town to ensure drunks
# cannot wander out of the environment as they make their way home.   
    def walk_home(self, town):
        
        """Moves drunks randomly
        
        Returns:
            tuple: the next x and y coordinates drunks will move to
        """
        
        # Define the number of steps the drunks will take each loop. This can be altered to make drunks
        # move faster through the town.
        Move = 1
        
        # Generate a pseudo-random number between 0 and 1 using the random module from the random library.
        # If the random number is less than 0.5:
        if random.random() < 0.5:
            # Drunks x-coordinate increases by 1, moving the drunks right 1 step.
            self._x = (self._x + Move) % len(town)    
        # If the random number is greater than 0.5:
        else:
            # Drunks x-coordinate decreases by 1, moving the drunks left 1 step.
            self._x = (self._x - Move) % len(town)
            
        # Generate a pseudo-random number between 0 and 1 using the random module from the random library.
        # If the random number is less than 0.5:
        if random.random() < 0.5:
             # Drunks y-coordinate increases by 1, moving the drunks up 1 step.
            self._y = (self._y + Move) % len(town[0])
        # If the random number is greater than 0.5:
        else:
            # Drunks x-coordinate decreases by 1, moving the drunks down 1 step.
            self._y = (self._y - Move) % len(town[0])
        

  
# Create an increase_density function to add 1 to each point the drunks pass on their way home.  
    def increase_density(self):
        
        """ Adds 1 to the density list when a drunk passes a point in the town
        """
        
        self.density[self._x][self._y] += 1  
        
        
"""          
# The following code presents an alternative walk_home() function that should prevent drunks from retracing 
# their steps.The general idea for this code was taken from Max Eschenbach from the link:
# https://discourse.mcneel.com/t/python-walker-no-retracing-steps/72956. 
# Nonetheless, the code here was adapted to stores the coordinates in a dictionary rather than a list and 
# creates a keep_trying variable that makes drunks continue trying to find a new coordinate to move to if they have 
# already been in a particular point.
# This code is commented out as, although the model does not find any errors with it, the console is not able to 
# finish running the function, potentially due to it's complexity. I could not find a solution for this, therefore it 
# is not included in the final code. 
    def walk_home(self, town):
        while (self._x, self._y) in self.locationvisited:
            Move = 1
            keep_trying = True
            while keep_trying:
             if town[self._x][self._y] != 0 or town[self._x][self._y] != self.identifier:
                if random.random() < 0.5:
                    move_x = (self._x + Move) % 300   
                else:
                    move_x = (self._x - Move) % 300   
                if random.random() < 0.5:
                    move_y = (self._y + Move) % 300   
                else:
                    move_y = (self._y - Move) % 300
                # When, in the town, self._x and self._y are equal to 0 or the drunks identifier:
                if town[self._x][self._y] == 0 or town[self._x][self._y] == self.identifier:
                        # Keep_trying is false so self._x and self.y coordinates become move_x and move_y as
                        # defined above, which allows them to move.
                        keep_trying = False
                        self._x = move_x
                        self._y = move_y
        # These coordinates are then added to the self.locationvisited dictionary so that the drunks cannot move
        # back into this spot.                
        self.locationvisited.add((self._x, self._y))   
 """       