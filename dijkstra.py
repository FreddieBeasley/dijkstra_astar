from graph import *

def getAdjacentVertices(graph:Graph, vertex:Vertex) -> list:
     returnlist = []

     for edge in graph.get_edges():
          
          if vertex == edge.get_vertices()[0] and edge.get_vertices()[1] not in returnlist:
               returnlist.append(edge.get_vertices()[1])

          elif vertex == edge.get_vertices()[1] and edge.get_vertices()[0] not in returnlist:
               returnlist.append(edge.get_vertices()[0])
     
     return returnlist

class DijkstraItem:
     def __init__(self, lable, order, count):
          self.__lable = lable
          self.__order = order
          self.__count = count

     def get_lable(self):
          return self.__lable
     
     def get_order(self):
          return self.__order
     
     def get_count(self):
          return self.__count
     
     def update_order(self, order):
          self.__order = order
     
     def update_count(self, count):
          self.__count = count

class Queue:
     def __init__(self):
          self.__contents = [] #contains DijkstraItems
          self.__archive = []
     
     def add(self, dijkstraItem):
          self.__contents.append(dijkstraItem)
     
     def pop(self):
          lowest = 100
          returnItem = None

          for dijkstraItem in self.__contents:
               if dijkstraItem.get_count() < lowest:
                    lowest = dijkstraItem.get_count()
                    returnItem = dijkstraItem
          
          self.__archive.append(returnItem)
          self.__contents.remove(returnItem)
          return returnItem
     
     def lookUp_item(self, lable):
          for dijkstraItem in self.__contents:
               if dijkstraItem.get_lable() == lable:
                    return dijkstraItem
          return None
     
     def get_contents(self):
          return self.__contents
     
     def get_archive(self):
          return self.__archive
     
     def __len__(self):
          return len(self.__contents)


def dijkstra(graph:Graph, startVertex:Vertex, endVertex:Vertex) -> list:

     #validation
     if startVertex not in graph.get_vertices():
          return []
     
     if endVertex not in graph.get_vertices():
          return []
     
     #initialising queue
     queue = Queue()

     for vertex in graph.get_vertices():
          if vertex == startVertex:
               queue.add(DijkstraItem(vertex.get_lable(), None, 0))
          else:
               queue.add(DijkstraItem(vertex.get_lable(), None, 100))
     
     order = -1

     while True:
          order += 1
          #Base cases
          if len(queue) == 0: #all nodes checked
               break

          currentDijkstraItem = queue.pop()
          currentDijkstraItem.update_order(order)

          if currentDijkstraItem.get_lable() == endVertex.get_lable(): #current node is target node
               break

          for edge in graph.get_edges():
               #loops through each vertex in the graph

               if edge.get_vertices()[0] == graph.lookUp_vertex(currentDijkstraItem.get_lable()):
                    #selects vertices which are adjacent to current vertex
                    consideringDijkstraItem = queue.lookUp_item(edge.get_vertices()[1].get_lable())

               elif edge.get_vertices()[1] == graph.lookUp_vertex(currentDijkstraItem.get_lable()):
                    consideringDijkstraItem = queue.lookUp_item(edge.get_vertices()[0].get_lable())

               else:
                    continue

               if consideringDijkstraItem == None:
                    continue
               
               currentRouteCost = consideringDijkstraItem.get_count()
               newRouteCost = currentDijkstraItem.get_count() + edge.get_weight()

               if currentRouteCost > newRouteCost:
                    consideringDijkstraItem.update_count(newRouteCost)
               
     print("\n")
     for item in queue.get_archive():
          print(item.get_lable())
          print(item.get_order())
          print(item.get_count())
          print("\n")



          

dijkstra(my_graph, vertexA, vertexE)















