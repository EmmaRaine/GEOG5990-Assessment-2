# GEOG5990-Assessment-2
#### This file contains the work developed for the second assignment "Planning for Drunks" in the 'programming for geographical information analysis' module. The work has been produced in a python console, using the Spyder application. 
#### This README file provides an overview of the files included and what each of these files do. It will provide links to other documents in this folder that detail how to run the model, model testing, any issues in the model and opportunties for future model development.

Overall, this work aimed to present a density map of drunk person movement as they randomly move around the town to find their way home. This model should:

* pull in the town data and finds out the pub and home points.
* draws the pub and homes on the screen
* models the drunks leaving their pub and reaching their homes, storing how many drunks pass through each point on the map
* draws the density of drunks passing through each point on a map
* saves the density map to the working directory as a text file (.txt)

### Contents

#### drunkframework1.py

This file contains the Drunk class that defines the functions used in the final model. This include code that:

* defines the starting location for drunk movement as the centre of the pub
* creates a walk_home() function that pseudo-randomly moves the drunks around the town from the starting point as they find their way home - the 'Move' variable associated with this can increased so that drunks move faster throughout the town.
* creates an alternative walk_home() function (not fully functional) that randomly moves drunks toward their home, stopping them from retracing their steps
* creates an increase_density() function that adds 1 to a point in the density least each time a drunk passes that point in the town

#### drunkmodel.py

This file contains the final model code and is responsible for plotting the final density map and saving it as a text file. The code should run, firstly saving the town plan to a town list before plotting the town. Following on, the code should find the coordinates and centre coordinates of the pub alongside the house coordinates and provide code that can manually plot these on the screen. A density list is then created before the code to move the drunks and increase density is run. The density map is then plotted along with the drunks final locations before, finally, the density list is exported as a text file and saved in the working folder. The values in this text file will change each time the model is run as drunks do not take the same route hom each time. Iformation on how to run the model can be found ([here]:(https://github.com/EmmaRaine/GEOG5990-Assessment-2/blob/main/User_Documentation.md)).

#### drunk.plan.txt

This file is a text file that contains the town data. This was read into the model and appended to the town list to enable the town to be plotted. It was also read into the model and appended to the density list, although, here, all values were set as 0. To be used in the model, this file has to be saved in the same directory as the model has been created in. 
The file contains values 1, denoting the pub and values 10-250 (increasing by multiples of 10), representing houses. All other values are 0 and denote the surroudning town environment. 

#### density.txt

This is the density file exported at the end of the model. This contains a variety of values that denote how many times a drunks passed through each point on the map.

#### User_Documentation.md

This file contains information on how to run the model, model testing, how the code was developed and the software required to run the model. 

#### Model_Issues.md

This file details any issues encountered in the model developement process. It also highlights any issues or functionality/efficiency problems in the final model and details why they were not/could not be solved. This can be found ([here]: (https://github.com/EmmaRaine/GEOG5990-Assessment-2/blob/main/Model_Issues.md)).

#### Further_Developments.md

This file provides information surrounding potential future model developments. This can be found ([here]: (https://github.com/EmmaRaine/GEOG5990-Assessment-2/blob/main/Further_Developments.md)).
