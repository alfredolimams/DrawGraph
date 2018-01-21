from igraph import *
import numpy as np


class DrawGraph:
	def __init__(self, vertices , edges, weight, directed ):
		self.graph = Graph(directed=directed)
		for v in vertices:
			self.graph.add_vertex(v,**{"label":v})
		for i in range(len(edges)) :
			print( edges[i] , "-" , weight[i] )
			if len(weight) :
				self.graph.add_edge( edges[i][0] , edges[i][1] , **{"label":weight[i],"weight":int(weight[i])})
			else :
				self.graph.add_edge( edges[i][0] , edges[i][1] )

	def show(self):
		visual_style = {}
		visual_style["vertex_size"] = 15
		visual_style["edge_curved"] = self.graph.is_directed()
		visual_style["bbox"] = (2000, 1000)
		visual_style["margin"] = 150
		visual_style["layout"] = self.graph.layout("lgl")
		plot(self.graph, **visual_style)		

	def colorVertices( self, vertices , color ):
		for v in self.graph.vs:
			print(v)

	def colorEdges( self, edges , color ):
		for v in self.graph.es:
			print(v)