import sys
import time
from algorithm.bubble_sort import bubble_sort
from algorithm.binary_search import binary_search
from algorithm.dijkstra import dijkstra
from algorithm.knapsack import knapsack
from visualize.display import print_colored_array, print_colored_text, print_dp_table
from visualize.animation import plot_array, plot_graph


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


def get_user_input(prompt, input_type=str):
    """Get validated user input"""
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
    """Get array input from user"""
    print("\nEnter array elements (comma-separated):")
    while True:
        try:
            arr_input = input("Array: ").strip()
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
            nodes = graph_input.split(';')
            for node_data in nodes:
                if ':' not in node_data:
                    continue
                node, neighbors = node_data.split(':', 1)
                node = node.strip()
                graph[node] = []
                
                if neighbors.strip():
                    neighbor_pairs = neighbors.split(',')
                    for i in range(0, len(neighbor_pairs), 2):
                        if i + 1 < len(neighbor_pairs):
                            neighbor = neighbor_pairs[i].strip()
                            weight = int(neighbor_pairs[i + 1].strip())
                            graph[node].append((neighbor, weight))
            
            return graph
        except (ValueError, IndexError):
            print("Please enter a valid graph format.")


def run_sorting_algorithms():
    """Handle sorting algorithm menu"""
    print("\nSorting Algorithms:")
    print("1. Bubble Sort")
    print("2. Back to main menu")
    
    choice = get_user_input("Choose sorting algorithm (1-2)", int)
    
    if choice == 1:
        arr = get_array_input()
        print(f"\nOriginal array: {arr}")
        
        # Terminal visualization
        def terminal_viz(arr, i, j):
            print_colored_text(f"Comparing {arr[i]} and {arr[j]}", "\033[93m")
            print_colored_array(arr, [i, j], "\033[91m")
            time.sleep(0.5)
        
        print_colored_text("\nBubble Sort Visualization:", "\033[92m")
        bubble_sort(arr.copy(), terminal_viz)
        print_colored_text(f"Final sorted array: {arr}", "\033[92m")
        
        # Ask for matplotlib visualization
        if input("\nShow matplotlib visualization? (y/n): ").lower() == 'y':
            def plot_viz(arr, i, j):
                plot_array(arr, [i, j], f"Bubble Sort - Comparing {arr[i]} and {arr[j]}")
                time.sleep(0.5)
            
            bubble_sort(arr.copy(), plot_viz)


def run_search_algorithms():
    """Handle search algorithm menu"""
    print("\nSearch Algorithms:")
    print("1. Binary Search")
    print("2. Back to main menu")
    
    choice = get_user_input("Choose search algorithm (1-2)", int)
    
    if choice == 1:
        arr = get_array_input()
        arr.sort()  # Binary search requires sorted array
        print(f"\nSorted array: {arr}")
        
        target = get_user_input("Enter target to search", int)
        
        def terminal_viz(arr, left, right, mid):
            print_colored_text(f"Searching range [{left}:{right}], mid={mid}, value={arr[mid]}", "\033[93m")
            highlight = list(range(left, right + 1))
            print_colored_array(arr, highlight, "\033[91m")
            print_colored_array(arr, [mid], "\033[92m")
            time.sleep(0.8)
        
        print_colored_text("\nBinary Search Visualization:", "\033[92m")
        result = binary_search(arr, target, terminal_viz)
        
        if result != -1:
            print_colored_text(f"Found {target} at index {result}!", "\033[92m")
        else:
            print_colored_text(f"{target} not found in array.", "\033[91m")


def run_graph_algorithms():
    """Handle graph algorithm menu"""
    print("\nGraph Algorithms:")
    print("1. Dijkstra's Algorithm")
    print("2. Back to main menu")
    
    choice = get_user_input("Choose graph algorithm (1-2)", int)
    
    if choice == 1:
        graph = get_graph_input()
        print(f"\nGraph: {graph}")
        
        start_node = get_user_input("Enter start node", str)
        
        def terminal_viz(distances, visited, current):
            print_colored_text(f"Current node: {current}", "\033[93m")
            print_colored_text(f"Visited: {visited}", "\033[92m")
            print_colored_text(f"Distances: {distances}", "\033[94m")
            time.sleep(1)
        
        print_colored_text("\nDijkstra's Algorithm Visualization:", "\033[92m")
        distances = dijkstra(graph, start_node, terminal_viz)
        
        print_colored_text(f"\nFinal distances from {start_node}:", "\033[92m")
        for node, dist in distances.items():
            if dist == float('inf'):
                print(f"{node}: ∞ (unreachable)")
            else:
                print(f"{node}: {dist}")
        
        # Ask for matplotlib visualization
        if input("\nShow matplotlib visualization? (y/n): ").lower() == 'y':
            def plot_viz(distances, visited, current):
                plot_graph(distances, visited, current)
                time.sleep(1)
            
            dijkstra(graph, start_node, plot_viz)


def run_dynamic_programming():
    """Handle dynamic programming algorithm menu"""
    print("\nDynamic Programming Algorithms:")
    print("1. 0/1 Knapsack Problem")
    print("2. Back to main menu")
    
    choice = get_user_input("Choose DP algorithm (1-2)", int)
    
    if choice == 1:
        print("\nEnter knapsack problem data:")
        weights = get_array_input()
        values = get_array_input()
        capacity = get_user_input("Enter knapsack capacity", int)
        
        print(f"\nWeights: {weights}")
        print(f"Values: {values}")
        print(f"Capacity: {capacity}")
        
        def terminal_viz(dp, i, w):
            print_colored_text(f"Filling dp[{i}][{w}]", "\033[93m")
            print_dp_table(dp, i, w)
            time.sleep(0.5)
        
        print_colored_text("\n0/1 Knapsack Visualization:", "\033[92m")
        max_value = knapsack(weights, values, capacity, terminal_viz)
        print_colored_text(f"Maximum value: {max_value}", "\033[92m")


def main():
    """Main function to run the Algorithm Visualizer"""
    print_colored_text("Welcome to Algorithm Visualizer!", "\033[95m")
    print_colored_text("Explore algorithms through interactive visualizations.", "\033[94m")
    
    while True:
        try:
            display_menu()
            choice = get_user_input("Enter your choice (1-5)", int)
            
            if choice == 1:
                run_sorting_algorithms()
            elif choice == 2:
                run_search_algorithms()
            elif choice == 3:
                run_graph_algorithms()
            elif choice == 4:
                run_dynamic_programming()
            elif choice == 5:
                print_colored_text("\nThank you for using Algorithm Visualizer!", "\033[95m")
                print_colored_text("Happy learning! 🚀", "\033[94m")
                break
            else:
                print_colored_text("Invalid choice. Please enter 1-5.", "\033[91m")
                
        except KeyboardInterrupt:
            print_colored_text("\n\nExiting...", "\033[91m")
            break
        except Exception as e:
            print_colored_text(f"An error occurred: {e}", "\033[91m")
            print("Please try again.")


if __name__ == "__main__":
    main()
