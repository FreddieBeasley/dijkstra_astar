class Vertex:
     def __init__(self, lable):
          self.__lable = lable
     
     def get_lable(self):
          return self.__lable

class Edge:
     def __init__(self, weight, vertexA:Vertex, vertexB:Vertex):
          self.__weight = weight
          self.__vertexA = vertexA
          self.__vertexB = vertexB

     def get_weight(self):
          return self.__weight
     
     def get_vertices(self):
          return [self.__vertexA, self.__vertexB]
     
class Graph:
     def __init__(self):
          self.__vertices = []
          self.__edges = []

     #Getter
     def get_vertices(self):
          return self.__vertices
     
     def get_edges(self):
          return self.__edges
     
     #Adder
     def add_vertex(self, vertex:Vertex):
          self.__vertices.append(vertex)
     
     def add_edge(self, edge:Edge):
          self.__edges.append(edge)

     def lookUp_vertex(self, lable:str):
          for vertex in self.__vertices:
               if vertex.get_lable() == lable:
                    return vertex
          return None

my_graph = Graph()

vertexA = Vertex("a")
vertexB = Vertex("b")
vertexC = Vertex("c")
vertexD = Vertex("d")
vertexE = Vertex("e")
vertexF = Vertex("f")

my_graph.add_vertex(vertexA)
my_graph.add_vertex(vertexB)
my_graph.add_vertex(vertexC)
my_graph.add_vertex(vertexD)
my_graph.add_vertex(vertexE)
my_graph.add_vertex(vertexF)

my_graph.add_edge(Edge(5,vertexA, vertexB))
my_graph.add_edge(Edge(7,vertexA, vertexC))
my_graph.add_edge(Edge(8,vertexB, vertexC))
my_graph.add_edge(Edge(4,vertexB, vertexD))
my_graph.add_edge(Edge(4,vertexC, vertexD))
my_graph.add_edge(Edge(6,vertexC, vertexE))
my_graph.add_edge(Edge(5,vertexD, vertexE))


"""
print("\n")
print("--Vertices--")
for vertex in my_graph.get_vertices():
     print(vertex.get_lable())

print("\n")
print("--Edges--")
for edge in my_graph.get_edges():
     print("weight", edge.get_weight())
     print("edges", edge.get_vertices()[0].get_lable(), edge.get_vertices()[1].get_lable())
     print("\n")
"""