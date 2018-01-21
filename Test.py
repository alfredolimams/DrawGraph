import DrawGraph

V, E = map( int , input().split() )

vertices = []
edges = []
for i in range(V):
	vertices.append( input() )

for i in range(E):
	u , v = input().split()
	edges.append( (u,v) )

draw = DrawGraph.DrawGraph( vertices = vertices , edges = edges , weight = [1,2] , directed=True )

draw.colorVertices([], 'sds')
draw.colorEdges([], 'sds')
draw.show()