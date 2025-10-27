# 🚀 Algorithm Visualizer

A modular, interactive Algorithm Visualizer developed in Python, tailored specifically for the Analysis of Algorithms (AOA) syllabus. This project enables users to explore and understand classic algorithms through vivid step-by-step visualizations.

## 📚 Algorithms Covered

### 🔢 Sorting Algorithms
- **Bubble Sort** - O(n²) complexity, demonstrates basic sorting concepts

### 🔍 Search Algorithms  
- **Binary Search** - O(log n) complexity, efficient search in sorted arrays

### 🕸️ Graph Algorithms
- **Dijkstra's Algorithm** - O(V²) complexity, finds shortest paths in weighted graphs

### 💰 Dynamic Programming
- **0/1 Knapsack Problem** - O(n×W) complexity, optimization problem solving

## 🎯 Features

- **Interactive Menu System** - Easy navigation through different algorithm categories
- **Step-by-Step Visualization** - See each algorithm's decision-making process
- **Terminal Color Coding** - Highlighted elements for better understanding
- **Execution Timing** - Measure and compare algorithm performance
- **Input Validation** - Robust error handling for user inputs
- **Modular Design** - Clean, maintainable code structure
- **Educational Focus** - Perfect for learning and teaching algorithms

## 🏗️ Project Structure

```
algovisualize/
├── main.py                 # Main program file
├── README.md              # This file
├── TEACHER_GUIDE.md       # Comprehensive teaching guide
├── pyproject.toml         # Project configuration
├── algorithm/             # Algorithm implementations
│   ├── bubble_sort.py     # Bubble sort algorithm
│   ├── binary_search.py   # Binary search algorithm
│   ├── dijkstra.py        # Dijkstra's shortest path
│   └── knapsack.py        # 0/1 Knapsack DP solution
└── visualize/             # Visualization utilities
    ├── display.py         # Terminal color/text functions
    └── animation.py       # Matplotlib plotting (optional)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- Optional: matplotlib (for graphical visualizations)

### Installation
1. Clone or download the project
2. Navigate to the project directory
3. Run the program:
   ```bash
   python3 main.py
   ```

### Optional Dependencies
For enhanced graphical visualizations:
```bash
pip install matplotlib
```

## 🎮 How to Use

1. **Run the program**: `python3 main.py`
2. **Choose algorithm category** from the main menu:
   - Sorting Algorithms
   - Search Algorithms
   - Graph Algorithms
   - Dynamic Programming
3. **Enter your data** when prompted
4. **Watch the visualization** step-by-step
5. **Observe timing results** for performance analysis

## 📖 Usage Examples

### Bubble Sort
```
Enter numbers separated by commas (e.g., 5,2,8,1,9):
Numbers: 5,2,8,1,9

Original array: [5, 2, 8, 1, 9]
Comparing 5 and 2
[5] [2] 8 1 9    # Red highlights elements being compared
...
Final sorted array: [1, 2, 5, 8, 9]
⏱️  Time taken: 0.0023 seconds
```

### Binary Search
```
Enter numbers separated by commas (e.g., 5,2,8,1,9):
Numbers: 1,3,5,7,9,11,13

Sorted array: [1, 3, 5, 7, 9, 11, 13]
Enter number to search for: 7

Searching range [0:6], mid=3, value=7
[1] [3] [5] [7] [9] [11] [13]    # Green highlights search range
Found 7 at index 3!
⏱️  Time taken: 0.0001 seconds
```

### Dijkstra's Algorithm
```
Enter graph as adjacency list:
Example: A:B,4;C,2; B:C,1;D,5; C:D,3
Graph: A:B,4;C,2; B:C,1;D,5; C:D,3

Graph: {'A': [('B', 4), ('C', 2)], 'B': [('C', 1), ('D', 5)], 'C': [('D', 3)], 'D': []}
Enter start node: A

Current node: A
Visited: {'A'}
Distances: {'A': 0, 'B': 4, 'C': 2, 'D': inf}
...
Shortest distances from A:
A: 0
B: 4
C: 2
D: 5
⏱️  Time taken: 0.0008 seconds
```

### 0/1 Knapsack
```
Enter knapsack data:
Weights: 2,3,4,5
Values: 3,4,5,6
Capacity: 8

Building solution table:
Filling dp[1][2]
0 0 3 3 3 3 3 3 3
...
Maximum value: 10
⏱️  Time taken: 0.0002 seconds
```

## 🎓 Educational Benefits

### For Students
- **Visual Learning**: See algorithms in action with color-coded steps
- **Interactive Experience**: Hands-on learning with different inputs
- **Performance Understanding**: Real-time timing measurements
- **Step-by-Step Process**: Understand each decision the algorithm makes

### For Teachers
- **Demonstration Tool**: Perfect for classroom presentations
- **Assignment Material**: Students can experiment with various inputs
- **Assessment Aid**: Students can explain what they observe
- **Comparison Tool**: Compare different algorithms side-by-side

## 🔧 Technical Details

### Dependencies
- **Required**: Python 3.6+, time module, heapq module
- **Optional**: matplotlib, numpy (for graphical visualizations)

### Key Features
- **Error Handling**: Comprehensive input validation
- **Modular Design**: Each algorithm in separate files
- **Visualization**: Terminal-based colored output
- **Timing**: Precise execution time measurement
- **Extensibility**: Easy to add new algorithms

### Performance Considerations
- **Step Visualization**: Includes pauses for better understanding
- **Timing Accuracy**: Measures actual algorithm execution time
- **Memory Efficiency**: Uses copies for visualization to preserve original data

## 🛠️ Development

### Adding New Algorithms
1. Create algorithm file in `algorithm/` directory
2. Implement algorithm with visualization callback parameter
3. Add demonstration function in `main.py`
4. Update menu system to include new algorithm

### Customizing Visualizations
- Modify `visualize/display.py` for terminal colors
- Update `visualize/animation.py` for matplotlib plots
- Adjust timing and pause intervals in demonstration functions

## 📊 Algorithm Complexity

| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| Bubble Sort | O(n²) | O(1) | Educational, small datasets |
| Binary Search | O(log n) | O(1) | Searching in sorted arrays |
| Dijkstra's | O(V²) | O(V) | Shortest path in graphs |
| 0/1 Knapsack | O(n×W) | O(n×W) | Optimization problems |

## 🎯 Learning Objectives

After using this visualizer, students should be able to:
- Understand how each algorithm works step-by-step
- Recognize algorithm complexity patterns
- Explain the purpose and use cases of each algorithm
- Compare different algorithmic approaches
- Connect theoretical concepts to practical implementation

## 🤝 Contributing

This project is designed for educational purposes. Contributions are welcome for:
- Additional algorithms
- Enhanced visualizations
- Better user interface
- Documentation improvements

## 📄 License

This project is created for educational purposes and is open for academic use.

## 🙏 Acknowledgments

- Analysis of Algorithms (AOA) curriculum
- Python community for excellent libraries
- Educational institutions promoting algorithm visualization

## 📞 Support

For questions or issues:
- Check the `TEACHER_GUIDE.md` for detailed explanations
- Review the code comments for implementation details
- Test with different inputs to understand algorithm behavior

---

**Happy Learning!** 🎓✨

*"The best way to understand an algorithm is to see it in action."*
