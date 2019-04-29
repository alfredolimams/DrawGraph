import matplotlib.pyplot as plt
import numpy as np

class Plot:
	def __init__(self, x_min, x_max, y_min, y_max):
		plt.ion()
		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1)
		minor_ticks_x = np.arange(x_min-1, x_max+2, 1)
		minor_ticks_y = np.arange(y_min-1, y_max+2, 1)
		ax.set_xticks(minor_ticks_x, minor=True)
		ax.set_yticks(minor_ticks_y, minor=True)
		ax.grid(which='minor', alpha=0.2)
		
	def show(self):
		plt.show(block=False)

	def sleep(self):
		plt.pause(0.001)

	def plot_vertex(self, v, color='r', sleep=False, sz=.05):
		vertex = plt.Circle(v,sz,color=color)
		plt.gcf().gca().add_artist(vertex)
		if sleep : self.sleep()