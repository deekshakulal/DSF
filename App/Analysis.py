from matplotlib import pyplot as plt
  
x = [2, 3, 4, 5]
  
# Y-axis values
y = [107.345, 157.556, 311.31, 511.94]
  
# Function to plot
plt.plot(x,y,marker = 'o')
plt.xlabel("number of documents")
plt.ylabel("Time taken in seconds")
# function to show the plot
plt.show()