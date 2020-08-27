#Create bar plots with error bars on the same figure

import numpy as np
import matplotlib.pyplot as plt
N = 5
menMeans = (54.74, 42.35, 67.37, 58.24, 30.25)
menStd = (4, 3, 4, 1, 5)
# the x locations for the groups
ind = np.arange(N)    
# the width of the bars
width = 0.35   
plt.bar(ind, menMeans, width, yerr=menStd, color='red')
plt.ylabel('Scores')
plt.xlabel('Velocity')
plt.title('Scores by Velocity')
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()