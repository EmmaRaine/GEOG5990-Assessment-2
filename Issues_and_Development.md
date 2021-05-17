# Model Issues and Improvements

The model has no known issues integral to its running ability, although there are a few minor issues that slightly reduce the models efficiency.
One of the most noticeable issues is the length of time the model takes to run. This issue is mainly noticeable at the last stage of computation, firstly when plotting the density map and secondly when manually plotting the homes and pubs to ensure drunks have made it home. This is likely attributed to the vast number of coordinates that the console is being required to process and ultimately slowing it down. However, this can be largely overcome, usually reducing computation time by around 10-15 seconds, by commenting out the section of code in lines 288-310. This code essentially tests the model to ensure that the drunks have made it home but is not necessary for the final product. 

Another issue with the code was the inability to stop agents re-tracing their steps. In the agentframework1.py file, an alternative walk_home() function was created to do this and, although Spyder and the iPython console could not find any errors with the code it would not run in a reasonable amount of time, despite debugging the code and checking for errors. Getting this to work would have provided a more realistic and advanced model, thus this may be something future work could look to develop.

# Future Model Developments

While this model effectively encapsulates the behaviour of drunks as they make their way home, there are still other options for enhancing the model further and making it more realistic.

Firstly, a relatively simple upgrade to the model would be for future work to plot this as an animation. This would provide the user with insights into the routes each drunk takes as they make their way home. 

Additionally, future work could look to make the model more realistic. As this wasn't an animation it is hard to know exactly where drunks passed through on the map. However, it can be assumed that, given there was no code in place to stop this, drunks were able to roam around the town, walking through houses and the pubs. Future model development could involve creating boundaries around the houses so that drunks cannot walk through them or get to them unless it is their home. This would better represent real-life behaviours.

Finally, future work could enhance the walk_home() function to give the drunks different behaviours depending on how near/far they are from their home. By calculating the distance between the pub and the home, future work could allow drunks to move less randomly as they get closer to their home i.e. when surroundings become more familiar. Once again, this would better represent real-life behaviours.
