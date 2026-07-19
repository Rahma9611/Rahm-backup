# PART 1 - IMPORT MATPLOTLIB
# Before drawing any chart you need to import the matplotlib library
# matplotlib,pyplot is the drawing tool -- "plt" is its short nickname.
import matplotlib.pyplot as plt

# PART 2 - YOUR DATA
# days holds the x-axis labels -- the days of your school week
# scroes holds the y-axis vlaues -- your quiz score for each day
# every score pairs up with the day in the same position 
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores = [70, 85, 60, 90, 75]

#PART 3 - PLOT YOUR FIRST LINE GRAPH 
# plt.plot(x, y) draws a line throught all your data points
# plt.show() opens the chart window -- call it at the end of every chart 
plt.plot(days, scores)
plt.show()
