import random
import Plot
import Graph
from multiprocessing import Process
import time

RANDOM = 1

x_min, x_max = 0, 100
y_min, y_max = 0, 100

qt_points = int( (x_max - x_min) * (y_max - y_min) * 8/10 )

qt_gate = min(max(int( qt_points * (1/100) ), 2), 15)

d_max = 2
lim_update = 10

points = set()

if RANDOM :
	print("Gerando pontos")
	
	while len(points) < qt_points:
		x, y = random.randint(x_min, x_max), random.randint(y_min, y_max)
		points.add((x,y))

	points = list(points)
	print("Fim da geração dos pontos")

else :
	print("Pontos fixos")
	points = [(0,0),(0,1),(0,2)]


print("Plot")
plot = Plot.Plot(x_min, x_max, y_min, y_max)
plot.show()

for pt in points:
	plot.plot_vertex(pt)

print("Grafo")

graph = Graph.Graph()
graph.add_vertexs(points)
graph.connect_edges2D(d_max)

print("Fim grafo")

gates = set()

if RANDOM :
	print("Escolhendo os gates")
	while len(gates) < qt_gate:
		g = random.randint(0,len(points)-1)
		gates.add(points[g])

	gates = list(gates)

else :
	print("Gates fixos")
	gates = [(0,1)]


lvls = graph.bfs_plot(gates, lim_update)
color = ['b', 'g']

input("Update")

for lvl in range(len(lvls)):
	if RANDOM :
		print('Level', lvl+1)
	else :
		print('Level', lvl+1, lvls[lvl])
	
	for l in lvls[lvl]:
		if lvl == 0:
			plot.plot_vertex(l, sz=0.1,color=color[lvl&1])
		else :
			plot.plot_vertex(l, color=color[lvl&1])
	
	plot.sleep()
	time.sleep(3)

input("Fim")