# Dijkstra & A* Pathfinding Algorithms

This repository contains Python implementations of two popular pathfinding algorithms: **Dijkstra's Algorithm** and **A* (A-star)**.  
Both algorithms are implemented to work on a weighted graph data structure and can be used to find the shortest path between two nodes.

## Features

- **Dijkstra's Algorithm**:
  - Finds the shortest path from a starting node to all other nodes in a weighted graph.
  - Works with graphs containing positive edge weights.
  
- **A* Search Algorithm**:
  - Uses heuristics to guide the search for faster performance in many cases.
  - Finds the shortest path between a start and goal node.
  
- **Graph Class**:
  - Easy-to-use data structure for storing nodes, edges, and weights.
  - Supports adding nodes, adding edges, and retrieving neighbors.

---

## File Structure

```
├── images         # Contain images of example graphs
├── astar.py       # A* search algorithm implementation
├── dijkstra.py    # Dijkstra’s algorithm implementation
└── graph.py       # Graph data structure and helper methods
```
---

## Algorithms Overview

### Dijkstra's Algorithm
Dijkstra’s Algorithm is a graph search method that finds the shortest paths from a single source node to all other nodes in a graph with non-negative edge weights.  
It works by exploring the graph in order of increasing distance from the source, updating the shortest known distances to each node.

**Key characteristics:**
- Guaranteed to find the optimal path.
- Time complexity: `O((V + E) log V)` using a priority queue.

---

### A* Search Algorithm
A* is an informed search algorithm that combines the actual distance from the start node with a heuristic estimate to the goal node.  
It often finds the shortest path faster than Dijkstra’s by focusing exploration toward the goal.

**Key characteristics:**
- Uses a heuristic function `h(n)` to estimate the cost from node `n` to the goal.
- Optimal if the heuristic is admissible (never overestimates).
- Time complexity: `O(E)` in the worst case, but often faster in practice.

---

## Graph Class

The `Graph` class in `graph.py` provides:
- `add_node(node)` — Add a node to the graph.
- `add_edge(node1, node2, weight)` — Add a weighted edge between two nodes.
- `get_neighbors(node)` — Retrieve all neighbors of a node and their edge weights.

Example:
```python
from graph import Graph

g = Graph()
g.add_edge("A", "B", 5)
g.add_edge("A", "C", 10)
print(g.get_neighbors("A"))
# Output: {'B': 5, 'C': 10}
```

```python
from graph import Graph
from dijkstra import dijkstra

# Create a graph
g = Graph()
g.add_edge("A", "B", 5)
g.add_edge("B", "C", 2)
g.add_edge("A", "C", 9)

# Run Dijkstra from node A
distances, previous_nodes = dijkstra(g, "A")
print(distances)       # Shortest distance from A to all nodes
print(previous_nodes)  # Previous node in the shortest path
```

```python
from graph import Graph
from astar import astar

# Example heuristic (straight-line distance)
def heuristic(node, goal):
    return abs(ord(node) - ord(goal))

# Create a graph
g = Graph()
g.add_edge("A", "B", 5)
g.add_edge("B", "C", 2)
g.add_edge("A", "C", 9)

# Run A* from A to C
path, cost = astar(g, "A", "C", heuristic)
print(path)  # ['A', 'B', 'C']
print(cost)  # 7
```

```bash
python example.py
```
