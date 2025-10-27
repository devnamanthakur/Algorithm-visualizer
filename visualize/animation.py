import matplotlib.pyplot as plt
import numpy as np

def plot_array(arr, highlight_indices=None, title="Array Visualization"):
    highlight_indices = highlight_indices or []
    colors = ['skyblue' if i not in highlight_indices else 'orange' for i in range(len(arr))]
    plt.figure(figsize=(8,4))
    plt.bar(np.arange(len(arr)), arr, color=colors)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()


def plot_graph(distances, visited, current=None):
    plt.figure(figsize=(6,4))
    nodes = list(distances.keys())
    dists = [distances[n] if distances[n] != float('inf') else 0 for n in nodes]
    colors = []
    for n in nodes:
        if n == current:
            colors.append('red')
        elif n in visited:
            colors.append('green')
        else:
            colors.append('grey')
    plt.bar(nodes, dists, color=colors)
    plt.title("Dijkstra's Progress")
    plt.xlabel("Node")
    plt.ylabel("Distance from start")
    plt.show()