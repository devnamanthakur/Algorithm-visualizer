
import time
from algorithm.bubble_sort import bubble_sort
from algorithm.binary_search import binary_search
from algorithm.dijkstra import dijkstra
from algorithm.knapsack import knapsack
from visualize.display import print_colored_array, print_colored_text, print_dp_table


try:
    from visualize.animation import plot_array, plot_graph, MATPLOTLIB_AVAILABLE
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    def plot_array(*args, **kwargs):
        print("Matplotlib not available. Skipping graphical visualization.")
    def plot_graph(*args, **kwargs):
        print("Matplotlib not available. Skipping graphical visualization.")


def display_menu():
    """Display the main menu options"""
    print_colored_text("\n" + "="*50, "\033[94m")
    print_colored_text("    ALGORITHM VISUALIZER", "\033[95m")
    print_colored_text("="*50, "\033[94m")
    print("\nChoose an algorithm category:")
    print("1. Sorting Algorithms")
    print("2. Search Algorithms") 
    print("3. Graph Algorithms")
    print("4. Dynamic Programming")
    print("5. Exit")
    print_colored_text("="*50, "\033[94m")


# Helper Functions for User Input
def get_user_input(prompt, input_type=str):
    """Get user input with validation"""
    while True:
        try:
            value = input(f"{prompt}: ").strip()
            if not value:
                print("Please enter a valid value.")
                continue
            return input_type(value)
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}.")


def get_array_input():
    """Get array of numbers from user"""
    print("\nEnter numbers separated by commas (e.g., 5,2,8,1,9):")
    while True:
        try:
            arr_input = input("Numbers: ").strip()
            if not arr_input:
                print("Please enter some numbers.")
                continue
            arr = [int(x.strip()) for x in arr_input.split(',')]
            return arr
        except ValueError:
            print("Please enter valid integers separated by commas.")


def get_graph_input():
    """Get graph input from user"""
    print("\nEnter graph as adjacency list (format: node1:neighbor1,weight1;neighbor2,weight2)")
    print("Example: A:B,4;C,2; B:C,1;D,5; C:D,3")
    
    while True:
        try:
            graph_input = input("Graph: ").strip()
            if not graph_input:
                print("Please enter a valid graph.")
                continue
            
            graph = {}
            all_nodes = set()  # Track all nodes (both sources and destinations)
            
            nodes = graph_input.split(';')
            for node_data in nodes:
                if ':' not in node_data:
                    continue
                node, neighbors = node_data.split(':', 1)
                node = node.strip()
                all_nodes.add(node)  # Add source node
                graph[node] = []
                
                if neighbors.strip():
                    neighbor_pairs = neighbors.split(',')
                    for i in range(0, len(neighbor_pairs), 2):
                        if i + 1 < len(neighbor_pairs):
                            neighbor = neighbor_pairs[i].strip()
                            weight = int(neighbor_pairs[i + 1].strip())
                            all_nodes.add(neighbor)  # Add destination node
                            graph[node].append((neighbor, weight))
            
            # Ensure all nodes exist in the graph (even if they have no outgoing edges)
            for node in all_nodes:
                if node not in graph:
                    graph[node] = []
            
            return graph
        except (ValueError, IndexError):
            print("Please enter a valid graph format.")


# Algorithm Demonstrations
def demonstrate_bubble_sort():
    """Demonstrate Bubble Sort algorithm"""
    print("\n=== BUBBLE SORT DEMONSTRATION ===")
    print("Bubble Sort compares adjacent elements and swaps them if they're in wrong order.")
    
    # Get input from user
    arr = get_array_input()
    print(f"\nOriginal array: {arr}")
    
    # Create visualization function
    def show_step(arr, i, j):
        print_colored_text(f"Comparing {arr[i]} and {arr[j]}", "\033[93m")
        print_colored_array(arr, [i, j], "\033[91m")
        time.sleep(0.5)
    
    # Run algorithm with timing
    print_colored_text("\nSorting process:", "\033[92m")
    start_time = time.time()
    bubble_sort(arr.copy(), show_step)
    end_time = time.time()
    
    print_colored_text(f"Final sorted array: {arr}", "\033[92m")
    print_colored_text(f"⏱️  Time taken: {end_time - start_time:.4f} seconds", "\033[96m")


def demonstrate_binary_search():
    """Demonstrate Binary Search algorithm"""
    print("\n=== BINARY SEARCH DEMONSTRATION ===")
    print("Binary Search finds an element in a sorted array by repeatedly dividing the search space.")
    
    # Get input from user
    arr = get_array_input()
    arr.sort()  # Binary search requires sorted array
    print(f"\nSorted array: {arr}")
    
    target = get_user_input("Enter number to search for", int)
    
    # Create visualization function
    def show_step(arr, left, right, mid):
        print_colored_text(f"Searching range [{left}:{right}], mid={mid}, value={arr[mid]}", "\033[93m")
        highlight = list(range(left, right + 1))
        print_colored_array(arr, highlight, "\033[91m")
        print_colored_array(arr, [mid], "\033[92m")
        time.sleep(0.8)
    
    # Run algorithm with timing
    print_colored_text("\nSearch process:", "\033[92m")
    start_time = time.time()
    result = binary_search(arr, target, show_step)
    end_time = time.time()
    
    # Show results
    if result != -1:
        print_colored_text(f"Found {target} at index {result}!", "\033[92m")
    else:
        print_colored_text(f"{target} not found in array.", "\033[91m")
    
    print_colored_text(f"⏱️  Time taken: {end_time - start_time:.4f} seconds", "\033[96m")


def demonstrate_dijkstra():
    """Demonstrate Dijkstra's Shortest Path algorithm"""
    print("\n=== DIJKSTRA'S ALGORITHM DEMONSTRATION ===")
    print("Dijkstra finds the shortest path from a start node to all other nodes.")
    
    # Get graph input
    graph = get_graph_input()
    print(f"\nGraph: {graph}")
    
    start_node = get_user_input("Enter start node", str)
    
    # Create visualization function
    def show_step(distances, visited, current):
        print_colored_text(f"Current node: {current}", "\033[93m")
        print_colored_text(f"Visited: {visited}", "\033[92m")
        print_colored_text(f"Distances: {distances}", "\033[94m")
        time.sleep(1)
    
    # Run algorithm with timing
    print_colored_text("\nFinding shortest paths:", "\033[92m")
    start_time = time.time()
    distances = dijkstra(graph, start_node, show_step)
    end_time = time.time()
    
    # Show results
    print_colored_text(f"\nShortest distances from {start_node}:", "\033[92m")
    for node, dist in distances.items():
        if dist == float('inf'):
            print(f"{node}: ∞ (unreachable)")
        else:
            print(f"{node}: {dist}")
    
    print_colored_text(f"⏱️  Time taken: {end_time - start_time:.4f} seconds", "\033[96m")


def demonstrate_knapsack():
    """Demonstrate 0/1 Knapsack Dynamic Programming algorithm"""
    print("\n=== 0/1 KNAPSACK DEMONSTRATION ===")
    print("Knapsack problem: maximize value while staying within weight capacity.")
    
    # Get input
    print("\nEnter knapsack data:")
    weights = get_array_input()
    values = get_array_input()
    capacity = get_user_input("Enter knapsack capacity", int)
    
    print(f"\nWeights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    
    # Create visualization function
    def show_step(dp, i, w):
        print_colored_text(f"Filling dp[{i}][{w}]", "\033[93m")
        print_dp_table(dp, i, w)
        time.sleep(0.5)
    
    # Run algorithm with timing
    print_colored_text("\nBuilding solution table:", "\033[92m")
    start_time = time.time()
    max_value = knapsack(weights, values, capacity, show_step)
    end_time = time.time()
    
    print_colored_text(f"Maximum value: {max_value}", "\033[92m")
    print_colored_text(f"⏱️  Time taken: {end_time - start_time:.4f} seconds", "\033[96m")




def main():
    """Main function - Simple Algorithm Visualizer"""
    print_colored_text("Welcome to Algorithm Visualizer!", "\033[95m")
    print_colored_text("Learn algorithms through step-by-step visualizations.", "\033[94m")
    
    while True:
        try:
            # Show menu
            display_menu()
            choice = get_user_input("Choose algorithm to learn (1-5)", int)
            
            # Run selected algorithm
            if choice == 1:
                demonstrate_bubble_sort()
            elif choice == 2:
                demonstrate_binary_search()
            elif choice == 3:
                demonstrate_dijkstra()
            elif choice == 4:
                demonstrate_knapsack()
            elif choice == 5:
                print_colored_text("\nThank you for learning with us! 🚀", "\033[95m")
                break
            else:
                print_colored_text("Please choose 1-5.", "\033[91m")
                
        except KeyboardInterrupt:
            print_colored_text("\nGoodbye! 👋", "\033[91m")
            break
        except Exception as e:
            print_colored_text(f"Error: {e}", "\033[91m")
            print("Please try again.")


if __name__ == "__main__":
    main()
