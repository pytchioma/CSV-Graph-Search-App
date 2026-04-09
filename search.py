import customtkinter as ctk
import csv
from collections import deque
import time

# The UI setup
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("500x400")

# Load csv
def load_foods():
    foods = []
    with open("1000_foods.csv", newline='', encoding='utf-8') as file: # File is automatically closed after used, spacing issues
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            foods.append(row[0])
    return foods


# Build graph from list
def build_graph_from_list(foods):
    graph = {}

    for food in foods:
        graph[food] = []

        for other in foods:
            if food != other:
                # connect foods with same first word (method)
                if food.split()[0] == other.split()[0]:
                    graph[food].append(other)

    return graph

# BFS search
def search():
    target = entry.get()

    if not target:
        result_label.configure(text="Please enter a search")
        return

    start_time = time.time()  # start timing

    # try BFS from all nodes
    for start_node in foods:
        result = bfs_search(graph, start_node, target)
        if result:
            end_time = time.time()  #  end timing
            duration = end_time - start_time

            result_label.configure(
                text=f"{result}\nTime: {duration:.6f} seconds"
            )
            return

    end_time = time.time()  # end timing
    duration = end_time - start_time

    result_label.configure(
        text=f"not found\nTime: {duration:.6f} seconds"
    )

# Load Data
foods = load_foods()
graph = build_graph_from_list(foods)

# Search function
def bfs_search(graph, start, target):
    visited = set()
    queue = deque([start])

    target = target.lower().strip()

    while queue:
        current = queue.popleft()

        if target in current.lower(): # Searches for partial matches
            return f"{current} found!"

        if current not in visited: # This section ensures you don't visit the same node
            visited.add(current)

            for neighbour in graph.get(current, []):  # Adds neighbours that are connected to the queue to be explored
                queue.append(neighbour)

    return None



# UI
entry = ctk.CTkEntry(
    app,
    placeholder_text="Search food...",
    width=350,
    corner_radius=20
)
entry.pack(pady=20)

button = ctk.CTkButton(
    app,
    text="Search",
    command=search,
    corner_radius=20
)
button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", wraplength=400)
result_label.pack(pady=20)

# press Enter to search
entry.bind("<Return>", lambda event: search())

# -------- RUN --------
app.mainloop()