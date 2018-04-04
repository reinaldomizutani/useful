graph = {}

with open('grafo.in', 'r') as f:
	nodes = f.readline()
	lines = f.readlines()

nodes = int(nodes)
for x in range(nodes):
	graph.setdefault(x, [])


for line in lines:
	if line != '':
		key,value, weigth = line.split()
		key = int(key)
		value = int(value)
		weigth = int(weigth)
		temp = [value, weigth]
		graph[key].append(temp)

print(graph)