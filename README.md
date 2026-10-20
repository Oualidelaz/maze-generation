<div align="center">

# 🧩 Maze Generation & Pathfinding

#### Generate mazes with DFS. Find the shortest path with BFS.

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Generation-DFS-2563EB?style=flat-square" alt="DFS"/>
  <img src="https://img.shields.io/badge/Pathfinding-BFS-10B981?style=flat-square" alt="BFS"/>
  <img src="https://img.shields.io/badge/Visualization-Terminal-6D5EF5?style=flat-square" alt="Terminal visualization"/>
</p>

</div>


## 📌 Overview

A Python-based maze generation and pathfinding system that couples stochastic maze construction with classical graph-search algorithms. Depth-First Search (DFS) synthesizes the maze topology by carving passages between adjacent cells of an initially fully walled grid, while Breadth-First Search (BFS) traverses the resulting graph to compute the shortest path between the designated entry and exit points.

## 🔍 Depth-First Search (DFS)

</div>

<p align="center">
  <img src="assets/advanced_dfs_maze.gif" alt="DFS Maze Generation" width="600"/>
</p>

<p align="center">
  <span style="background: linear-gradient(90deg, red, cyan); 
               -webkit-background-clip: text; 
               color: transparent;">
    The animation illustrates DFS descending greedily along a single path and backtracking upon reaching a dead end.
  </span>
</p>



This project is a Python-based maze generation and visualization system that demonstrates the practical application of graph traversal algorithms, with particular emphasis on Depth-First Search (DFS). The application constructs a randomized maze using recursive backtracking, maintains per-cell state and wall connectivity, and renders the resulting layout in the terminal.

### ✨ Features

- 🧩 Maze generation via DFS traversal
- 📦 Matrix-based, cell-oriented architecture
- 🎨 Modular maze rendering system
- 🧠 Step-by-step visualization of the recursive algorithm
- ⚙️ Configuration-driven customization
- 🚪 Configurable entry and exit points
- 🔄 Loop injection and path tracing
- 📍 Coordinate and direction management
- 🛡️ Robust input parsing and validation

### 🏗️ Project Structure

- `add_loops.py` → imperfect maze generation (loop injection)
- `cell.py` → maze cell data model
- `cell_closed.py` → predefined closed-cell patterns
- `config.txt` → maze configuration parameters
- `dfs.py` → DFS-based maze generation algorithm
- `draw_maze.py` → maze visualization and rendering
- `generate_matrix.py` → matrix/grid construction
- `get_block_position.py` → blocked-region positioning utilities
- `get_direction.py` → movement and direction resolution logic
- `main.py` → application entry point and interactive menu system
- `parsing.py` → configuration parsing and validation
- `trace_u.py` → special path and block tracing logic

## 🤝 Team Contribution - Achraf Elhadjaoui

*Achraf Elhadjaoui* authored the BFS-based path-processing component of the project. His work centers on computing a valid route through the generated maze using Breadth-First Search, and on extracting the path-related data required for visualization and analysis:


- `path`
- `valid path coordinates`
- `wall values`
- `path directions` 


### 🎯 Purpose


This project aims to build a rigorous understanding of:

- 🧠 DFS and BFS algorithms
- 🧩 Maze generation and solving
- 🌐 Graph traversal concepts
- 🎨 Algorithm visualization


## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Oualidelaz/maze-generation.git
cd maze-generation/src
```

---

### 2️⃣ Configure the maze settings

Edit the `config.txt` file:

```text
HEIGHT = 20
WIDTH = 20
ENTRY = 0,0
EXIT = 19,19
PERFECT = TRUE
```

#### Configuration Options

- `HEIGHT` → Number of rows in the maze grid
- `WIDTH` → Number of columns in the maze grid
- `ENTRY` → Entry cell coordinates `(x,y)`
- `EXIT` → Exit cell coordinates `(x,y)`
- `PERFECT` → Toggles loop injection (imperfect maze generation)

---

### 3️⃣ Run the program

```bash
python main.py config.txt
```

---

### 4️⃣ Use the interactive menu

```text
==============================
         MAZE MENU
==============================

[1] Draw Maze
[2] Change Maze Color
[3] Show Maze Path

[0] Exit

==============================
```

- **Draw Maze** → Generates and renders a new maze
- **Change Maze Color** → Re-renders the maze using an alternative color theme
- **Show Maze Path** → Displays the computed solution path *(coming soon)*
- **Exit** → Terminates the application

---

### 📌 Requirements

- Python 3.8+
- A terminal with ANSI color support


<div align="center">

## 📌 Short Description - DFS

</div>

**Depth-First Search (DFS)** is a graph-traversal algorithm for exploring graphs, trees, and grid-based structures.

- Starting from a source node, it follows a single path as deeply as possible. Upon reaching a dead end, it backtracks to the most recent node that still has unexplored neighbors and resumes exploration from there.
- Backtracking is the act of retreating to a previously visited state in order to pursue an alternative branch.
- The process repeats until every node (or cell) has been visited.

It is widely applied in:
- Graph traversal
- Maze generation 🧩
- Tree exploration 🌲
- Backtracking problems 🔁


<div align="center">

## ⚙️ Functions and Responsibilities

</div>

<table>
  <tr>
    <td width="180"><strong>🧠 <code>dfs()</code></strong></td>
    <td>
      <strong>Core traversal algorithm</strong><br>
      Exhaustively explores a single branch to its full depth before backtracking to examine the remaining branches.
    </td>
  </tr>
</table>


<div align="center">

<h2>⚙️ Core <span style="color: #FFD700;">DFS</span> Function</h2>

</div>


<br>

<div style="border-left: 4px solid cyan; padding: 12px; background:rgba(30, 30, 30, 0.45); color: #ddd;">

<strong style="color: white;">📌 Grid Initialization</strong>

<ul>
<li>Construct a 2D grid (matrix) of <code>Cell</code> objects</li>
<li>Each cell is identified by its coordinates: <code>Cell(row, col)</code></li>
</ul>

<strong>Example:</strong>
<ul>
<li><code>WIDTH = 5</code>, <code>HEIGHT = 5</code></li>
<li>Cells span from <code>Cell(0,0)</code> → <code>Cell(4,4)</code></li>
</ul>
</div>
<br>


```python
class Cell:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.visited = False
        self.walls = {
            'top': 1,
            'right': 2,
            'bottom': 4,
            'left':8
        }

def dfs(self, matrix):
    stack = []
    entry_x, entry_y = self.entry
    n_cell = matrix[entry_y][entry_x]
    n_cell.visited = True
    stack.append(n_cell)

    while stack:
        current = stack[-1]
        x, y = current.x, current.y
        valid_neighbors = []
        neighbors = {
            'top': (x, y - 1),
            'down': (x, y + 1),
            'left': (x - 1, y),
            'right': (x + 1, y),
        }
        for nx, ny in neighbors.values():
            if 0 <= nx < self.width and 0 <= ny < self.height: 
                cell = matrix[ny][nx]
                if not cell.visited:
                    valid_neighbors.append(cell)
    
        if valid_neighbors:
            neighbor = random.choice(valid_neighbors)
            direction = get_direction(current, neighbor)
            opposite_direction  = get_direction(neighbor, current)
            current.walls[direction] = 0
            neighbor.walls[opposite_direction] = 0
            neighbor.visited = True
            stack.append(neighbor)
        else:
            stack.pop()
```

<div align="center">

## 🔍 Breadth-First Search (BFS) 

</div>

<p align="center">
  <img src="assets/advanced_bfs_maze.gif" alt="BFS" width="600"/>
</p>

<p align="center">
  <span style="background: linear-gradient(90deg, red, cyan); 
               -webkit-background-clip: text; 
               color: transparent;">
    The animation illustrates BFS expanding level by level from the source, which guarantees the shortest path in an unweighted graph.
  </span>
</p>

<div align="center">

## 📌 Short Description

</div>

**Breadth-First Search (BFS)** is a graph-traversal algorithm for exploring graphs, trees, and grid-based structures.

- Starting from a source node, it visits all immediate neighbors before advancing to the next depth level.
- In contrast to DFS, which commits to depth, BFS expands uniformly outward, much like a wave 🌊.
- It relies on a queue (FIFO) to maintain the frontier of nodes awaiting exploration.
- The process continues until all nodes (or cells) have been visited or the target is reached.

It is widely applied in:
- Graph traversal
- Shortest-path computation 📏
- Level-order traversal of trees 🌲


<div align="center">

## ⚙️ Functions and Responsibilities

</div>

<table>
  <tr>
    <td width="180"><strong>🧠 <code>bfs()</code></strong></td>
    <td>
      <strong>Core traversal algorithm</strong><br>
      Visits all neighbors of the current node before descending to the next level, using a queue-based frontier.
    </td>
  </tr>
</table>

<div align="center">

<h2>⚙️ Core <span style="color: #FFD700;">BFS</span> Function</h2>

</div>

```python
def bfs(matrix, entry, exit, width, height):
  start = matrix[entry[1]][entry[0]]
  end = matrix[exit[1]][exit[0]]
  queue = [start]
  visited = set()
  parent = {start: None}
  while queue:
      current = queue.pop(0)
      if current == end:
          break
      visited.add(current)
      neighbors = {
          "top": (current.x, current.y - 1),
          "bottom": (current.x, current.y + 1),
          "left": (current.x - 1, current.y),
          "right": (current.x + 1, current.y),
      }
      for direction, (x, y) in neighbors.items():
          if 0 <= x < width and 0 <= y < height:
              neighbor = matrix[y][x]
              if (neighbor not in visited
                  and current.walls[direction] == 0):
                  queue.append(neighbor)
                  visited.add(neighbor)
                  parent[neighbor] = current
  path = []
  if end not in parent:
      return path
  current = end
  while current is not None:
      path.append(current)
      current = parent[current]
  path.reverse()
  return path
```

---

## 🖼️ Maze Gallery

### Default Maze

<p align="center">
  <img src="./assets/img-1.png" width="700" alt="Default Maze">
</p>

---

### Colored Maze

<p align="center">
  <img src="./assets/img-2.png" width="700" alt="Colored Maze">
</p>

---

### Imperfect Maze (with loops)

<p align="center">
  <img src="./assets/img-3.png" width="700" alt="Imperfect Maze">
</p>