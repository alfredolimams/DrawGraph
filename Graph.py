from queue import *

class Graph:
	def __init__(self):
		self.graph = {}
		self.vertex = set()
		self.edges = set()

	def dist2D(self, v1, v2):
		return ( (v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 )**0.5

	def add_vertex(self, v):
		if not v in self.graph:
			self.graph[v] = {}
			self.vertex.add(v)

	def add_vertexs(self, vs):
		for v in vs:
			if not v in self.vertex:
				self.graph[v] = {}
				self.vertex.add(v)

	def connect_edges2D(self, dist=1):
		for v1 in self.graph:
			for v2 in self.graph:
				if v1 == v2: continue
				if v1 not in self.graph[v2] or v2 not in self.graph[v1]:
					d = self.dist2D(v1,v2)
					if d <= dist:
						if v1 not in self.graph[v2]: 
							self.graph[v2][v1] = d
							self.edges.add( (v1,v2,d) )
						if v2 not in self.graph[v1]: 
							self.graph[v1][v2] = d
							self.edges.add( (v2,v1,d) )

	def bfs_plot(self, gates, lim):
		
		steps = {}
		levels = list()
		levels.append(gates)
		q = list()
		step = 0

		for v in self.graph:
			steps[v] = float('inf')

		for g in gates:
			steps[g] = 0
			q.append(g)

		while len(q):
			
			itr = list()
			lvl = list()

			for v in q:
				if steps[v] != step:
					break
				itr.append(v)

			q = q[len(itr):]	
			
			for v in itr:
				cnt = 0
				for u in self.graph[v]:
					if steps[u] > steps[v] + 1:
						cnt = cnt + 1
						steps[u] = steps[v] + 1
						q.append(u)
						lvl.append(u)

					if cnt == lim:
						q = [u] + q
						break
			
			levels.append(lvl)
			step = step + 1
		
		levels.pop()
		
		return levels

	def dfs(self, v, lvl):
		pass

	def dfs_init_plot(self, gates, lim):
		
		stacks = {}
		for v in self.graph:
			stacks[v] = []
