# -*- coding: utf-8 -*-
"""
Created on Thu May 13 12:32:23 2021

@author: andre
"""
# Import relevant packages

# Import csv to parse/work with CSV data. 
import csv

# Import the drunkframework1 file to import the Drunks class which containing fucntions that 
# determining drunks behaviour as they make their way home. 
import drunkframework1  

# Import matplotlib.pyplot as plt to allow data to be plotted. Importing as plt reduces risk of 
# error throughout the code.
import matplotlib.pyplot as plt

# Import  time to allow access to modules and functions that in some way represent time in the code.
import time



# Begin timing how long the code will take to run
start = time.time()



# Create empty lists and variables needed throughout the model
# Set up an empty list called 'town' that will hold the town data
town = []

# Set up an empty list called pub to hold the pubs location information.
# In addition, set up two empty lists called pubx and puby to store the pubs x and y coordinates. These can
# be used to plot the pub location on a map.
pub = []
pubx = []
puby = []

# Set up an empty list called 'houses' to hold the location information for the 25 houses in the town.
# In addition, set up two empty lists (housesx and housesy) to store x and y coordinates of the homes. This
# can be used to plot the house locations. 
houses = []
housesx = []
housesy = [] 

# Create an empty list called density which will store the route taken by drunks to reach their homes. Everytime a 
# drunk passes a given point on the map, density of that point will increase by 1 which will be stored in this list.
density = []

# Create an empty list called drunks that will store the variables created in the drunk_agents file.
drunks = []

# Create a new variable called 'num_of_drunks' to identify how many drunk persons there are, thus, how many
# drunk persons have to make their way home
num_of_drunks = 25



# Read in the town data- a 300x300 raster displaying 25 houses that drunks have to make their way too from a 
# pub.
# Create a new variable (t) to open the drunk.plan.txt file using the relevant path name.
# This file contains data characterising the town including houses and pub location.
t = open('drunk.plan.txt', newline='')
# Create a new variable (reader) to read the town data into the model. 
reader = csv.reader(t, quoting = csv.QUOTE_NONNUMERIC)
# Create a for-loop to make each row a new list which will store the CSV data.
for row in reader:
    # Initialise a new list (rowlist) where values from the town data will be stored. 
    rowlist = []                
    for value in row:
        # Before each row is processed append the values in each row of the data to the rowlist.
        # Using int before stating 'value' ensures the value will be appended as an integer number.
        rowlist.append(int(value))   
    # Append the rowlist to the town list so that the drunk.plan.txt data will be stored within the town list. 
    town.append(rowlist) 
# Close the drunk.plan.txt file that has been opened so it cannot be read/written anymore. This is not 
# necessary as python tends to close files automatically but it is good practice.
t.close()



# Assess the length of the town list to test it has been appended correctly. This should print 300 for both
# columns and rows as the town data is a 300x300 raster. 
print("Number of rows:", len(town))
print("Number of columns:", len(town[0]))

# Use the plt.imshow module in the matplotlib.pyplot library to display the raster data as an image
plt.imshow(town, cmap="flag")
# Set the x and y axes to the length of the environment.
plt.xlim(0, 300)
plt.ylim(0, 300)
# Add a title to the plot.
plt.title("Town Plan")
plt.show()



# Create a for-loop to look inside the town list and find coordinates of the pub.            
for y, row in enumerate(town):
    for x, value in enumerate(row):
        # As the pub is denoted by the value 1 in the drunk.plan.txt file, search for the value 1 in the town list.
        if value == 1:
            # If the value is equal to 1 append the coordinates of this point to the pub list.
            pub.append((int(x), int(y)))
            # Append the x and y values to the pubx and puby lists. These can be used to plot the pub manually.
            pubx.append(x)
            puby.append(y)
            
# Create a for-loop to look inside the town list and find coordinates of the houses.                
for y, row in enumerate(town):
    for x, value in enumerate(row):
        # As houses are denoted by values 10-250 in the drunk.plan.txt file, search for these values in the town list.
        if value >= 10 and value <= 250:
            # If the value is equal to anything between 10 and 250 append the coordinates of this point to the 
            # houses list. The value on the end states the house number (between 10 and 250) that each coordinate
            # is related to. 
            houses.append((int(x), int(y), int(value)))
            # Append the x and y values to the corresponding house list so houses can be manually drawn.
            housesx.append(x)
            housesy.append(y)
 
            
 
"""
# Plot the town again, this time using the coordinates extracted from the town list for the houses and pub to manually
# draw these. This may take a while. This is done because depending on the colour scheme used when the town is plotted,
# some of the house locations or the pub location may not be visible. This way, they are always visible.             
plt.imshow(town)
# Create a for-loop to plot the pub coordinates.
for i in range(0, len(town)):
    plt.scatter(pubx, puby, color='red', s=10)
# Create a for-loop to plot the house coordinates.
for i in range(0, len(town)):
    plt.scatter(housesx, housesy, color='blue', s=1)
# Show the town plot.
plt.show()

"""



# Find the length of the pub, this should be 441 suggesting the pub is a 20x20 square within the town.         
print("Pub length:", len(pub))

# Create a new variable pub_centre to store the most central coordinate of the pub to use as a starting point for 
# the drunks walking home. To do this, find the length of the pub list and then divide by 2. As there is an odd number 
# of items in the pub list, the easiest way of finding the centre point is dividing by 2.
# This should return a list with the central-most pub coordinates within in.
pub_center = [pub[int(len(pub)/2)]]

# Print the coordinates of the pub center. 
print("Pub centre coordinates:", pub_center)

# Create 2 new variables (pub_x and pub_y to store these central coordinates)
pub_x, pub_y = 138, 148



# Create a new variable (d) to open the drunk.plan.txt file again.
d = open('drunk.plan.txt', newline='')
# Use the reader variable to read the town data into the model, this time using the variable d as the file to be read in. 
reader = csv.reader(d, quoting=csv.QUOTE_NONNUMERIC)
# Create a for-loop to make each row a new list which will store the CSV data.
for row in reader:
   # Initialise a new list (rowlist) where values from the town data will be stored. 
   rowlist2 = []
   for value in row:
       # Set the values in the row to zero. This will be increased by 1 everytime an agent passes over a coordinate.
       value == 0
       # Append these values to the rowlist.
       rowlist2.append(int(value))
   # Append the rowlist to the density list so that the data, with value 0, will be stored in the density list. 
   density.append(rowlist2)
# Close the file.
d.close()



# Creates a for-loop (for i in range), using the num_of_drunks variable to determine the number of coordinates 
# that will be appended to the Drunks list. 
for i in range(num_of_drunks):
    # Create a new variable called 'identifier' to assign each drunk a number relating to a house that they have to
    # reach.
    # As the first value in a list is in the '0' spot on python, the user has to add 1 first before mutliplying by 10.
    identifier = ((i+1)*10)  
    # Ensure all drunks have been assigned an identifier the numbers are correct. This should go up in multiples of 10
    # from 10-250 as their are 25 drunks and should match house numbers ranging from 10-250 as set out in the
    # drunk.plan.txt file.
    #print("Drunk IDs:", identifier)
    # Append the Drunks class from the drunkframework file to the empty drunk list created in this model. 
    # This should pass in the pub, density and identifier variables.
    drunks.append(drunkframework1.Drunks(density, identifier, pub_x, pub_y, drunks, town))

# Create a single variable to ensure that appending the drunk_agents file to the drunks list has worked properly.
d = drunkframework1.Drunks(density, identifier, pub_x, pub_y, drunks, town)

# Test that the files have been appended correctly by printing out the starting location of drunks. This should
# be equal to the pub_centre coordinates.
print("Drunks starting location:", d._x, d._y)

# Test the walk_home function works. This should print out x and y values either 1 greater or 1 less than the initial
# starting values as the Move variable in drunk_agents is equal to 1. If this is changed coordinates will move by whatever
# number is attached to the Move variable.
d.walk_home(town)
print("Drunks location after being moved once:", d._x, d._y)



# Create a variable to store the number of drunks who have made it home.       
#drunk_count = 0
# Create a for-loop to set some behaviour of the drunks. By calling the num_of_drunks variable, this means the loop
# will be run for each of the 25 drunks.    
for i in range(num_of_drunks):
    # While the coordinates of the drunks are not equal to their identifier:
    while (town[drunks[i]._y][drunks[i]._x] != drunks[i].identifier):
        # Make them walk toward their home
        drunks[i].walk_home(town)   
        # Increase the density of the points they cross in the town (increase density of a point by 1 everytime a 
        # drunk passes that point)
        drunks[i].increase_density() 
    ##else: 
        # Increase the number of drunks how made it home variable (drunk_count) by 1.
        #drunk_count +=1
        # When this is equal to the number of drunks (25) it means all drunks have made it back home. 
        #if drunk_count == (num_of_drunks):
            #print("Drunks have made it home!")
    # Once the drunk found their home (i.e. coordinates match their house number), print the coordinates. 
    print (town[drunks[i]._y][drunks[i]._x], drunks[i].identifier)



"""
# The following is an alternative code that allows the drunks to make their way home. This produces the same
# outcome as the previous code, however, here a variable is created to store how many drunks make it home. 
# This code could be more beneficial if the user intends to make the model into an animation as the final
# print statement could be adjusted to print a stopping condition.
# Create a variable to store the number of drunks who have made it home.       
drunk_count = 0
# Create a for-loop to set some behaviour of the drunks. By calling the num_of_drunks variable, this means the loop
# will be run for each of the 25 drunks.    
for i in range(num_of_drunks):
    # While the coordinates of the drunks are not equal to their identifier:
    while (town[drunks[i]._y][drunks[i]._x] != drunks[i].identifier):
        # Make them walk toward their home
        drunks[i].walk_home(town)   
        # Increase the density of the points they cross in the town (increase density of a point by 1 everytime a 
        # drunk passes that point)
        drunks[i].increase_density() 
    else: 
        # Increase the number of drunks how made it home variable (drunk_count) by 1.
        drunk_count +=1
        # When this is equal to the number of drunks (25) it means all drunks have made it back home. 
        if drunk_count == (num_of_drunks):
            print("Drunks have made it home!")
"""



# Plot the density map of where the drunks walked when trying to find their way home
# NOTE: THIS MAY TAKE A WHILE - asking the code to plot the pub and annotate the points is fairly
# means the console has to plot alot of points, thus may take some time - around 5-6 seconds. 
# Set the figure size
plt.figure(figsize=(10,10))
# Set the x and y axes to the length of the town
plt.ylim(0, len(town[0]))
plt.xlim(0, len(town))
# Add a title
plt.title("Density plot of drunk persons movement from the pub to their home")
# Create a for-loop to plot the pub.
for i in range(0, len(town)):
    plt.scatter(pubx, puby, color='yellow', s=10)
# Create a for-loop to plot the house coordinates to ensure the drunks end up here.
#for i in range(0, len(town)):
    #plt.scatter(housesx, housesy, color='blue', s=1)
# Create a for-loop to plot the location of each of the drunks specifying the colour and size of the points.
for i in range(num_of_drunks):
    plt.scatter(drunks[i]._x,drunks[i]._y, c="blue", s=60)
    plt.annotate(drunks[i].identifier, (drunks[i]._x,drunks[i]._y), fontsize=20, color = "white", weight="bold")
# Show the plot
plt.imshow(density, cmap='hot')
#plt.colorbar(shrink = 0.85, label='Density')
plt.show()



# Plot to check if the model works by plotting the drunks location once the model has run to ensure they
# are at their houses. 
# NOTE: THIS MAY TAKE A WHILE - asking the code to plot the pub and houses is means the console has to plot a lot 
# of points- houses x and y each have 3025 coordinates and pubx and puby each have 441.
# Thus, this may take some time - up to 10 seconds - and can be commented out to improve efficiency of the model. 
# Set the x and y-axes.
plt.xlim(0,len(town))
plt.ylim(0,len(town[0]))
# Plot the town.
plt.imshow(town, cmap="flag")
# Create a for-loop to plot the pubs and the houses.
for i in range(0, len(town)):
    plt.scatter(pubx, puby, color='yellow', s=10)
    plt.scatter(housesx, housesy, color='white', s=1)
# Plot the drunks location once the model has run.
for i in range(num_of_drunks):
    plt.scatter(drunks[i]._x,drunks[i]._y, c="blue", s=20)
    # Annotate the drunks by their identifier to establish each drunk has a different identifier and are located
    # at different.
    plt.annotate(drunks[i].identifier, (drunks[i]._x, drunks[i]._y), fontsize=10, color="black", weight="bold")
# Add a title to the plot.
plt.title("Drunks in their homes")
plt.show()



# Export the final density map to a .txt file - the same format as the original town file that was added to
# the model.
with open('density.txt', 'w', newline='') as output:
    # Create a new variable called 'csvwriter' to store the density data in the format required.
    csvwriter = csv.writer(output, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in density:
        # Add density to the rows of the csvwriter variable.
        csvwriter.writerow(row)
        
        
        
# End the timer that was initiated at the start of the model (after the imports) to establish how long the model 
# takes to run.
end = time.time()

# Print the time it takes (in seconds) for the model to run.
print("Time to run the model = " + str(end - start))