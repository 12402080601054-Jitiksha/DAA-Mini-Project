
# Pathfinding Algorithm Visualizer Using Python Tkinter

## 1. Project Overview

The Pathfinding Algorithm Visualizer is a Graphical User Interface (GUI) based mini project developed using Python and Tkinter. It demonstrates how different graph algorithms explore a grid to find a path between a starting point and a destination while avoiding obstacles.

The application provides an interactive grid where users can place walls, select a pathfinding algorithm, visualize the search process, and analyze its performance.

This project is developed as part of the Design and Analysis of Algorithms (DAA) subject to demonstrate graph traversal, shortest-path algorithms, data structures, and time and space complexity analysis.

## 2. Problem Statement

Finding an efficient path between two locations is an important problem in areas such as navigation systems, robotics, gaming, and network routing.

Different pathfinding algorithms explore a graph in different ways and may produce different paths or explore different numbers of nodes.

The objective of this project is to develop an interactive visualizer that demonstrates the working of multiple pathfinding algorithms and allows users to compare their behavior and performance.

## 3. Objectives

- To understand graph representation using a grid.
- To implement Breadth-First Search, Depth-First Search, and Dijkstra's algorithm.
- To visualize the exploration of nodes and the final path.
- To understand queues, stacks, priority queues, and graph traversal.
- To compare algorithms based on visited nodes, path length, and execution time.
- To study the time and space complexity of pathfinding algorithms.
- To provide a simple and interactive GUI for algorithm demonstration.

## 4. Features

- Interactive grid-based interface.
- Selection of starting and destination cells.
- Addition and removal of obstacles.
- Implementation of BFS, DFS, and Dijkstra's algorithm.
- Animated visualization of explored cells.
- Highlighting of the final path.
- Random maze generation.
- Adjustable animation speed.
- Display of visited-node count.
- Display of final path length.
- Measurement of algorithm execution time.
- Clear Search, Clear Walls, and Reset All options.
- Detection of unreachable destinations.

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Tkinter | GUI development |
| Collections deque | Queue implementation for BFS |
| Heapq | Priority queue for Dijkstra's algorithm |
| Random | Random obstacle generation |
| Time | Measurement of algorithm execution time |

All the libraries used in this project belong to Python's standard library. No third-party packages are required.

## 6. System Requirements

### Hardware Requirements
- Computer or laptop.
- Minimum 2 GB RAM recommended.
- Keyboard and mouse.
- Basic processor capable of running Python.

### Software Requirements
- Windows, Linux, or macOS.
- Python 3.
- Tkinter support.
- Visual Studio Code, IDLE, or any Python-compatible editor.
- Terminal or command prompt.

## 7. Algorithms Implemented

### 7.1 Breadth-First Search (BFS)

Breadth-First Search explores neighboring nodes level by level. It uses a queue to maintain the order in which nodes are visited.

Working:
1. Add the starting node to the queue.
2. Mark it as visited.
3. Remove the front node from the queue.
4. Check its valid neighboring nodes.
5. Add unvisited and non-blocked neighbors to the queue.
6. Store parent information to reconstruct the path.
7. Continue until the destination is reached or the queue becomes empty.

Time Complexity: O(V + E)

Space Complexity: O(V)

BFS guarantees a shortest path when all edges have equal cost.

### 7.2 Depth-First Search (DFS)

Depth-First Search explores one branch as deeply as possible before returning to explore other branches. It uses a stack.

Working:
1. Add the starting node to the stack.
2. Remove the top node.
3. Mark and process the node.
4. Add valid, unvisited neighbors to the stack.
5. Continue until the destination is found or no nodes remain.

Time Complexity: O(V + E)

Space Complexity: O(V)

DFS does not guarantee the shortest path.

### 7.3 Dijkstra's Algorithm

Dijkstra's algorithm finds a minimum-cost path from a starting node to a destination when edge weights are non-negative. It uses a priority queue to process the node with the smallest known distance.

Working:
1. Assign distance zero to the starting node.
2. Insert the starting node into the priority queue.
3. Select the node with the smallest distance.
4. Examine its valid neighbors.
5. Update distances when a shorter route is found.
6. Store parent information.
7. Continue until the destination is reached or the priority queue becomes empty.

Time Complexity: O((V + E) log V), using a binary heap and adjacency-list representation.

Space Complexity: O(V), excluding the graph representation.

In this project, all valid moves have equal cost. Dijkstra's algorithm is included to demonstrate priority queues and shortest-path computation.

## 8. Mathematical Representation

The grid is represented as an undirected, unweighted graph.

- V: Set of vertices representing grid cells.
- E: Set of edges representing valid connections between neighboring cells.
- Start: Initial vertex.
- Destination: Target vertex.
- Walls: Blocked vertices that cannot be traversed.
- Path: Sequence of connected vertices from the start to the destination.

Movement is allowed in four directions:

- Up
- Down
- Left
- Right

Diagonal movement is not supported.

For a grid with R rows and C columns:

V <= R x C

Each cell has at most four neighbors, so E = O(V).

Therefore, BFS and DFS have O(V) traversal time on this grid representation. Dijkstra with a binary heap has O(V log V) time on this grid.

## 9. Project Structure

```text
Pathfinding-Visualizer/
|
|-- codes
    |--pathfinding_visualizer.py
|-- screenshots
|-- README.md
```

### File Description

- `pathfinding_visualizer.py`: Contains the GUI, grid representation, pathfinding algorithms, animation, event handling, and performance statistics.
- `README.md`: Contains project documentation, instructions, algorithms, and complexity analysis.

## 10. Installation and Setup

### Step 1: Install Python

Download Python 3 from:

https://www.python.org/downloads/

During installation on Windows, enable the option to add Python to PATH.

### Step 2: Verify Python Installation

Open Command Prompt or PowerShell and execute:

```bash
python --version
```

### Step 3: Verify Tkinter

Run:

```bash
python -m tkinter
```

If Tkinter is installed correctly, a small demonstration window should appear.

### Step 4: Open the Project Folder

Place `pathfinding_visualizer.py` and `README.md` inside the same folder.

### Step 5: Run the Application

Open a terminal in the project folder and execute:

```bash
python pathfinding_visualizer.py
```

The Pathfinding Algorithm Visualizer window will open.

No additional package installation is required when Python includes Tkinter.

## 11. How to Use the Application

1. Launch the application.
2. Observe the grid containing the starting point and destination.
3. Left-click or drag on cells to add obstacles.
4. Right-click or drag to remove obstacles.
5. Select BFS, DFS, or Dijkstra from the algorithm dropdown.
6. Click the Visualize button.
7. Observe the explored cells and the final path.
8. Review the visited-node count, path length, and execution time.
9. Use Random Maze to generate a new arrangement of obstacles.
10. Use Clear Search to remove the previous search visualization.
11. Use Clear Walls to remove all obstacles.
12. Use Reset All to restore the original grid.

### Grid Color Legend

- Green: Starting cell.
- Red: Destination cell.
- Dark gray: Obstacle or wall.
- Light blue: Visited cell.
- Yellow: Final path.
- Light gray: Unvisited cell.

## 12. Performance Analysis

The application displays three main performance measurements.

### Visited Nodes

The total number of nodes processed during the search. A higher count generally means more of the graph was explored.

### Path Length

The number of moves from the starting cell to the destination. The starting cell is not counted as a move.

### Execution Time

The time taken by the algorithm to compute the search result, measured in milliseconds. The visualization animation is excluded.

### Expected Algorithm Behavior

| Property | BFS | DFS | Dijkstra |
|---|---|---|---|
| Main data structure | Queue | Stack | Priority queue |
| Finds a path when one exists | Yes | Yes | Yes |
| Guarantees shortest path | Yes, for equal-cost edges | No | Yes, for non-negative edge weights |
| Traversal strategy | Level by level | Depth first | Lowest known distance |
| Worst-case graph time | O(V + E) | O(V + E) | O((V + E) log V) |

Actual execution time and visited-node counts depend on the grid layout and the order in which neighboring cells are processed.

## 13. Testing

The following test cases can be used to verify the application.

| Test Case | Input or Action | Expected Result |
|---|---|---|
| TC01 | Run BFS on an empty grid | A shortest path is displayed |
| TC02 | Run DFS on an empty grid | A path is displayed |
| TC03 | Run Dijkstra on an empty grid | A minimum-cost path is displayed |
| TC04 | Add walls but leave a route open | The algorithm finds a valid route |
| TC05 | Completely block the destination | No path is found |
| TC06 | Generate a random maze | Random obstacles appear |
| TC07 | Clear Search | Visited cells and the final path disappear |
| TC08 | Clear Walls | All obstacles are removed |
| TC09 | Reset All | The grid returns to its initial configuration |
| TC10 | Change the animation delay | The visualization speed changes |

## 14. Limitations

- Only four-directional movement is supported.
- Diagonal movement is not implemented.
- All valid movements have equal cost.
- Weighted terrain is not available.
- A* search is not included in the current implementation.
- Execution-time measurements can vary across computers.
- The application is designed for educational visualization rather than large-scale navigation.

## 15. Future Enhancements

The project can be extended with the following features:

- A* Search using Manhattan distance.
- Weighted terrain with different movement costs.
- Diagonal movement.
- Side-by-side algorithm comparison.
- Graphs showing execution time against grid size.
- CSV export of performance results.
- Automatic maze generation using maze-generation algorithms.
- Adjustable grid dimensions.
- Improved animation controls, including pause and resume.
- Support for loading custom maps.

## 16. Applications

Pathfinding algorithms are used in:

- GPS and route-planning systems.
- Robot navigation.
- Video game character movement.
- Network routing.
- Maze-solving applications.
- Warehouse automation.
- Navigation in grid-based environments.

## 17. Learning Outcomes

After completing this project, students should be able to:

- Represent a grid as a graph.
- Implement BFS, DFS, and Dijkstra's algorithm.
- Use queues, stacks, and priority queues.
- Reconstruct a path using parent information.
- Analyze time and space complexity.
- Compare graph algorithms experimentally.
- Develop a GUI application using Python Tkinter.
- Understand the relationship between theoretical complexity and observed execution time.

## 18. Conclusion

The Pathfinding Algorithm Visualizer demonstrates the working of graph traversal and shortest-path algorithms through an interactive Python Tkinter GUI.

It provides a practical way to understand how BFS, DFS, and Dijkstra's algorithm explore a graph, handle obstacles, and find routes. The application also supports performance analysis through visited-node counts, path length, and execution-time measurements.

This project connects theoretical concepts from Design and Analysis of Algorithms with practical programming, visualization, and experimental analysis.

## 19. Author Information

Project Title: Pathfinding Algorithm Visualizer Using Python Tkinter

Subject: Design and Analysis of Algorithms (202045601)

Language: Python

GUI Framework: Tkinter

Project Type: Academic Mini Project

Author: Jitiksha Patel

Enrollment Number: 12402080601054

College: ADIT
