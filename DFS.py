def readGraph(grafo):
	with open('teste.in', 'r') as f:
		nodes = f.readline()
		nodes = int(nodes)
		for x in range(nodes):
			grafo[x] = []

		line = f.readline()
		
		while(line != ''):
			a, b = line.split()
			a = int(a)
			b = int(b)
			grafo[a].append(b)
			line = f.readline()

def DFS(grafo, visitados, node, topVet):
	
	visitados[node] = 1
	
	for item in grafo[node]:
		if visitados[item] == 0:
			DFS(grafo, visitados, item, topVet)
			#print(item)
	topVet.insert(0, node)

def BFS(grafo, visitados, node, topVet):
	print("teste")


	
if __name__ == "__main__":
	grafo = {}
	visitados = []
	topVet = []
	readGraph(grafo)
	for nodes in grafo:
		visitados.append(0)

	for nodes in grafo:
		if visitados[nodes] == 0:
			DFS(grafo, visitados, nodes, topVet)
		else:
			continue

	print(topVet)