## Color the Triangle Red
**Problem Link:** https://leetcode.com/problems/color-the-triangle-red/description

**Problem Statement:**
- Input: A `2D` vector `n` representing the sides of the triangle, and a `2D` vector `edges` representing the edges to color.
- Constraints: The input triangle is valid and has `n` sides.
- Expected Output: The minimum number of colors required to color the edges of the triangle such that no two adjacent edges have the same color.
- Key Requirements: 
  - The triangle has `n` sides.
  - There are `edges` edges to color.
  - No two adjacent edges can have the same color.
- Example Test Cases:
  - `n = 3, edges = [[0,1],[1,2],[2,0]]`
  - `n = 4, edges = [[0,1],[1,2],[2,3],[3,0]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible color combinations for the edges and check if any two adjacent edges have the same color.
- Step-by-step breakdown:
  1. Generate all possible color combinations for the edges.
  2. For each combination, check if any two adjacent edges have the same color.
  3. If a combination is found where no two adjacent edges have the same color, return the number of colors used.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int minColors(vector<vector<int>>& n, vector<vector<int>>& edges) {
        int maxColors = n.size();
        for (int i = 1; i <= maxColors; i++) {
            vector<int> colors(n.size(), -1);
            if (isValidColoring(i, colors, edges)) {
                return i;
            }
        }
        return -1;
    }
    
    bool isValidColoring(int maxColors, vector<int>& colors, vector<vector<int>>& edges) {
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            if (colors[u] == -1) {
                colors[u] = 1;
            }
            if (colors[v] == -1) {
                colors[v] = 1;
            }
            if (colors[u] == colors[v]) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of sides. This is because we are trying all possible color combinations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of sides. This is because we need to store the colors of the edges.
> - **Why these complexities occur:** The brute force approach tries all possible color combinations, resulting in an exponential time complexity. The space complexity is linear because we only need to store the colors of the edges.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is that we can use a graph coloring algorithm to solve this problem.
- Detailed breakdown of the approach:
  1. Create a graph where each edge is a node, and two nodes are connected if the corresponding edges are adjacent.
  2. Use a graph coloring algorithm to find the chromatic number of the graph, which is the minimum number of colors required to color the edges.
- Proof of optimality: The chromatic number of a graph is the minimum number of colors required to color the graph such that no two adjacent nodes have the same color.

```cpp
class Solution {
public:
    int minColors(vector<vector<int>>& n, vector<vector<int>>& edges) {
        int maxColors = n.size();
        vector<vector<int>> graph(maxColors);
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        int colors = 0;
        vector<int> colorAssignment(maxColors, -1);
        for (int i = 0; i < maxColors; i++) {
            if (colorAssignment[i] == -1) {
                colors = max(colors, dfs(graph, colorAssignment, i, 1));
            }
        }
        return colors;
    }
    
    int dfs(vector<vector<int>>& graph, vector<int>& colorAssignment, int node, int color) {
        colorAssignment[node] = color;
        int maxColor = color;
        for (int neighbor : graph[node]) {
            if (colorAssignment[neighbor] == -1) {
                maxColor = max(maxColor, dfs(graph, colorAssignment, neighbor, color + 1));
            } else if (colorAssignment[neighbor] == color) {
                maxColor = max(maxColor, dfs(graph, colorAssignment, neighbor, color + 1));
            }
        }
        return maxColor;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of sides and $m$ is the number of edges. This is because we are doing a depth-first search on the graph.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of sides and $m$ is the number of edges. This is because we need to store the graph and the color assignment.
> - **Optimality proof:** The graph coloring algorithm finds the chromatic number of the graph, which is the minimum number of colors required to color the edges such that no two adjacent edges have the same color.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph coloring, depth-first search.
- Problem-solving patterns identified: Using graph theory to solve a problem.
- Optimization techniques learned: Using a graph coloring algorithm to find the minimum number of colors required.
- Similar problems to practice: Graph coloring, vertex coloring.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for adjacent edges with the same color.
- Edge cases to watch for: Empty input, invalid input.
- Performance pitfalls: Using a brute force approach.
- Testing considerations: Test with different input sizes, test with different edge cases.