import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque
import heapq
import random
import time

ROWS = 20
COLS = 30
CELL_SIZE = 25

# Colors used by the grid
COLORS = {
    "empty": "#F4F6F8",
    "wall": "#303846",
    "start": "#2EAD67",
    "end": "#E45454",
    "visited": "#9DD8F0",
    "frontier": "#C6E9F7",
    "path": "#FFD166",
    "grid": "#D7DDE4",
}


class PathfindingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pathfinding Algorithm Visualizer")
        self.root.geometry("1050x700")
        self.root.minsize(850, 600)

        self.start = (2, 2)
        self.end = (ROWS - 3, COLS - 3)
        self.walls = set()
        self.visited = set()
        self.path = []
        self.animation_job = None
        self.running = False
        self.search_result = None
        self.paint_mode = "wall"

        self.algorithm_var = tk.StringVar(value="BFS")
        self.speed_var = tk.IntVar(value=15)
        self.status_var = tk.StringVar(value="Ready. Choose an algorithm and click Visualize.")
        self.stats_var = tk.StringVar(value="Visited: —    Path length: —    Time: —")

        self._build_ui()
        self.draw_grid()

    def _build_ui(self):
        outer = ttk.Frame(self.root, padding=10)
        outer.pack(fill="both", expand=True)

        title = ttk.Label(
            outer, text="Pathfinding Algorithm Visualizer",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(anchor="w", pady=(0, 8))

        controls = ttk.Frame(outer)
        controls.pack(fill="x", pady=(0, 8))

        ttk.Label(controls, text="Algorithm:").pack(side="left", padx=(0, 5))
        algorithm_box = ttk.Combobox(
            controls, textvariable=self.algorithm_var,
            values=("BFS", "DFS", "Dijkstra"), state="readonly", width=12
        )
        algorithm_box.pack(side="left", padx=(0, 12))

        ttk.Button(controls, text="Visualize", command=self.start_search).pack(side="left", padx=3)
        ttk.Button(controls, text="Random Maze", command=self.random_maze).pack(side="left", padx=3)
        ttk.Button(controls, text="Clear Walls", command=self.clear_walls).pack(side="left", padx=3)
        ttk.Button(controls, text="Clear Search", command=self.clear_search).pack(side="left", padx=3)
        ttk.Button(controls, text="Reset All", command=self.reset_all).pack(side="left", padx=3)

        speed_frame = ttk.Frame(outer)
        speed_frame.pack(fill="x", pady=(0, 8))
        ttk.Label(speed_frame, text="Animation delay (ms):").pack(side="left")
        ttk.Scale(
            speed_frame, from_=1, to=100, variable=self.speed_var,
            orient="horizontal", length=180
        ).pack(side="left", padx=8)
        ttk.Label(
            speed_frame,
            text="Left-click: add wall  |  Right-click: erase wall  |  Drag to paint"
        ).pack(side="left", padx=12)

        self.canvas = tk.Canvas(
            outer, bg="white", highlightthickness=1,
            highlightbackground="#B7C0CB"
        )
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<B1-Motion>", self.on_left_drag)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.bind("<B3-Motion>", self.on_right_drag)
        self.canvas.bind("<Configure>", self.on_resize)

        legend = ttk.Frame(outer)
        legend.pack(fill="x", pady=(8, 2))
        for label, color in [
            ("Start", COLORS["start"]), ("Destination", COLORS["end"]),
            ("Wall", COLORS["wall"]), ("Visited", COLORS["visited"]),
            ("Final path", COLORS["path"])
        ]:
            swatch = tk.Label(legend, bg=color, width=2, relief="solid", bd=1)
            swatch.pack(side="left", padx=(0, 4))
            ttk.Label(legend, text=label).pack(side="left", padx=(0, 14))

        ttk.Label(outer, textvariable=self.stats_var, font=("Segoe UI", 10, "bold")).pack(
            anchor="w", pady=(6, 2)
        )
        ttk.Label(outer, textvariable=self.status_var, wraplength=950).pack(anchor="w")

    def cell_size(self):
        width = max(1, self.canvas.winfo_width())
        height = max(1, self.canvas.winfo_height())
        return min(width / COLS, height / ROWS)

    def draw_grid(self):
        self.canvas.delete("all")
        size = self.cell_size()
        for r in range(ROWS):
            for c in range(COLS):
                cell = (r, c)
                if cell == self.start:
                    color = COLORS["start"]
                elif cell == self.end:
                    color = COLORS["end"]
                elif cell in self.walls:
                    color = COLORS["wall"]
                elif cell in self.path:
                    color = COLORS["path"]
                elif cell in self.visited:
                    color = COLORS["visited"]
                else:
                    color = COLORS["empty"]

                x1, y1 = c * size, r * size
                x2, y2 = x1 + size, y1 + size
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color,
                    outline=COLORS["grid"], width=1
                )
                if size >= 22 and cell in (self.start, self.end):
                    text = "S" if cell == self.start else "E"
                    self.canvas.create_text(
                        (x1 + x2) / 2, (y1 + y2) / 2,
                        text=text, fill="white", font=("Segoe UI", 9, "bold")
                    )

    def on_resize(self, _event):
        self.draw_grid()

    def event_to_cell(self, event):
        size = self.cell_size()
        c = int(event.x / size)
        r = int(event.y / size)
        if 0 <= r < ROWS and 0 <= c < COLS:
            return (r, c)
        return None

    def stop_animation(self):
        if self.animation_job is not None:
            self.root.after_cancel(self.animation_job)
            self.animation_job = None
        self.running = False

    def clear_search(self):
        self.stop_animation()
        self.visited.clear()
        self.path.clear()
        self.search_result = None
        self.stats_var.set("Visited: —    Path length: —    Time: —")
        self.status_var.set("Search cleared. Start, destination and walls are unchanged.")
        self.draw_grid()

    def reset_all(self):
        self.stop_animation()
        self.start = (2, 2)
        self.end = (ROWS - 3, COLS - 3)
        self.walls.clear()
        self.visited.clear()
        self.path.clear()
        self.stats_var.set("Visited: —    Path length: —    Time: —")
        self.status_var.set("Grid reset.")
        self.draw_grid()

    def clear_walls(self):
        self.walls.clear()
        self.clear_search()
        self.status_var.set("All walls cleared.")

    def random_maze(self):
        self.stop_animation()
        self.visited.clear()
        self.path.clear()
        self.walls.clear()
        for r in range(ROWS):
            for c in range(COLS):
                cell = (r, c)
                if cell not in (self.start, self.end) and random.random() < 0.27:
                    self.walls.add(cell)
        self.stats_var.set("Visited: —    Path length: —    Time: —")
        self.status_var.set("Random maze created. Click Visualize to search.")
        self.draw_grid()

    def edit_cell(self, event, add_wall):
        if self.running:
            return
        cell = self.event_to_cell(event)
        if cell is None or cell in (self.start, self.end):
            return
        if add_wall:
            self.walls.add(cell)
        else:
            self.walls.discard(cell)
        self.visited.clear()
        self.path.clear()
        self.stats_var.set("Visited: —    Path length: —    Time: —")
        self.draw_grid()

    def on_left_click(self, event):
        self.edit_cell(event, True)

    def on_left_drag(self, event):
        self.edit_cell(event, True)

    def on_right_click(self, event):
        self.edit_cell(event, False)

    def on_right_drag(self, event):
        self.edit_cell(event, False)

    @staticmethod
    def neighbors(cell):
        r, c = cell
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                yield (nr, nc)

    def reconstruct_path(self, parent):
        if self.end != self.start and self.end not in parent:
            return []
        result = []
        current = self.end
        while current != self.start:
            result.append(current)
            current = parent[current]
        result.reverse()
        return result

    def run_bfs(self):
        queue = deque([self.start])
        seen = {self.start}
        parent = {}
        order = []
        while queue:
            current = queue.popleft()
            order.append(current)
            if current == self.end:
                break
            for nxt in self.neighbors(current):
                if nxt not in seen and nxt not in self.walls:
                    seen.add(nxt)
                    parent[nxt] = current
                    queue.append(nxt)
        return order, self.reconstruct_path(parent) if self.end in seen else []

    def run_dfs(self):
        stack = [self.start]
        seen = {self.start}
        parent = {}
        order = []
        while stack:
            current = stack.pop()
            order.append(current)
            if current == self.end:
                break
            # Reverse the order so traversal is visually consistent.
            for nxt in reversed(list(self.neighbors(current))):
                if nxt not in seen and nxt not in self.walls:
                    seen.add(nxt)
                    parent[nxt] = current
                    stack.append(nxt)
        return order, self.reconstruct_path(parent) if self.end in seen else []

    def run_dijkstra(self):
        distances = {self.start: 0}
        parent = {}
        heap = [(0, self.start)]
        settled = set()
        order = []
        while heap:
            distance, current = heapq.heappop(heap)
            if current in settled:
                continue
            settled.add(current)
            order.append(current)
            if current == self.end:
                break
            for nxt in self.neighbors(current):
                if nxt in self.walls or nxt in settled:
                    continue
                new_distance = distance + 1
                if new_distance < distances.get(nxt, float("inf")):
                    distances[nxt] = new_distance
                    parent[nxt] = current
                    heapq.heappush(heap, (new_distance, nxt))
        return order, self.reconstruct_path(parent) if self.end in settled else []

    def start_search(self):
        if self.running:
            return
        self.clear_search()
        algorithm = self.algorithm_var.get()

        started = time.perf_counter()
        if algorithm == "BFS":
            order, path = self.run_bfs()
        elif algorithm == "DFS":
            order, path = self.run_dfs()
        else:
            order, path = self.run_dijkstra()
        elapsed_ms = (time.perf_counter() - started) * 1000

        self.search_result = (order, path, elapsed_ms)
        self.running = True
        self.status_var.set(f"Running {algorithm}...")
        self.animate_result(0, 0)

    def animate_result(self, index, path_index):
        if self.search_result is None:
            self.running = False
            return

        order, path, elapsed_ms = self.search_result
        # Reveal visited cells progressively.
        batch_size = 1 if self.speed_var.get() >= 50 else 4
        end_index = min(index + batch_size, len(order))
        for cell in order[index:end_index]:
            self.visited.add(cell)
        self.draw_grid()

        if end_index < len(order):
            delay = max(1, int(self.speed_var.get()))
            self.animation_job = self.root.after(
                delay, lambda: self.animate_result(end_index, 0)
            )
            return

        # Reveal final path after exploration is complete.
        path_batch = 2
        next_path_index = min(path_index + path_batch, len(path))
        self.path = path[:next_path_index]
        self.draw_grid()

        if next_path_index < len(path):
            delay = max(1, int(self.speed_var.get()))
            self.animation_job = self.root.after(
                delay, lambda: self.animate_result(len(order), next_path_index)
            )
            return

        self.running = False
        self.animation_job = None
        self.stats_var.set(
            f"Visited: {len(order)}    Path length: {len(path)} moves    "
            f"Algorithm runtime: {elapsed_ms:.3f} ms"
        )
        if path:
            self.status_var.set(
                f"{self.algorithm_var.get()} finished. Destination reached."
            )
        else:
            self.status_var.set(
                f"{self.algorithm_var.get()} finished. No path could be found."
            )


def main():
    root = tk.Tk()
    try:
        style = ttk.Style()
        if "clam" in style.theme_names():
            style.theme_use("clam")
    except tk.TclError:
        pass
    PathfindingVisualizer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
