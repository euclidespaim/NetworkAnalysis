# Import necessary modules
import matplotlib.pyplot as plt
from nxviz import CircosPlot
from NetworkAnalysis import NetworkTwitter as T

# Create the CircosPlot object: c
c = CircosPlot(T)

# Draw c to the screen
c.draw()

# Display the plot
plt.show()
