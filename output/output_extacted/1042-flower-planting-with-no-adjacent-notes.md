## Flower Planting with No Adjacent
**Problem Link:** https://leetcode.com/problems/flower-planting-with-no-adjacent/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input, representing the number of gardens, and a 2D array `paths` where `paths[i] = [x, y]` means there is a path between the `x-th` garden and the `y-th` garden.
- Expected output format: An array of length `n` where the `i-th` element represents the color of the flower in the `i-th` garden.
- Key requirements and edge cases to consider: The task is to plant flowers in the gardens such that no two adjacent gardens have the same color. There are four colors available (1, 2, 3, and 4).
- Example test cases with explanations: For example, given `n = 3` and `paths = [[1,2],[2,3],[3,1]]`, a valid coloring could be `[1,2,3]` or any other permutation that satisfies the no-adjacent rule.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible color combinations for each garden and check if the combination satisfies the condition that no two adjacent gardens have the same color.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of colors for the gardens.
  2. For each permutation, check if any two adjacent gardens (as defined by the `paths` array) have the same color.
  3. If a permutation satisfies the condition, return it as a valid solution.
- Why this approach comes to mind first: It's a straightforward approach to ensure all possibilities are considered.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<int> gardenNoAdj(int n, vector<vector<int>>& paths) {
    vector<vector<int>> graph(n + 1);
    for (auto& path : paths) {
        graph[path[0]].push_back(path[1]);
        graph[path[1]].push_back(path[0]);
    }
    
    vector<int> colors(n + 1, 0); // Initialize colors for each garden
    
    function<bool(int)> backtrack = [&](int garden) {
        if (garden > n) return true; // Base case: All gardens colored
        
        for (int color = 1; color <= 4; ++color) {
            bool valid = true;
            for (int neighbor : graph[garden]) {
                if (colors[neighbor] == color) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                colors[garden] = color;
                if (backtrack(garden + 1)) return true;
                colors[garden] = 0; // Reset for next color attempt
            }
        }
        return false; // No valid color found for this garden
    };
    
    backtrack(1);
    colors.erase(colors.begin()); // Remove dummy value for garden 0
    return colors;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n)$, where $n$ is the number of gardens. This is because in the worst case, we might have to try all four colors for each garden.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of gardens and $m$ is the number of paths. This is for storing the graph and the colors array.
> - **Why these complexities occur:** The brute force approach involves trying all possible color combinations, leading to exponential time complexity. The space complexity is linear due to the storage needed for the graph and the colors.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a backtracking algorithm to efficiently try color combinations, ensuring that we only explore valid configurations.
- Detailed breakdown of the approach:
  1. Create a graph representation of the gardens and their connections.
  2. Initialize an array to store the color of each garden.
  3. Implement a backtracking function that tries each of the four colors for a garden, ensuring that the chosen color does not conflict with the colors of the garden's neighbors.
  4. If a valid color is found for a garden, recursively attempt to color the remaining gardens.
- Proof of optimality: This approach is optimal because it systematically explores all possible colorings while pruning branches that lead to invalid configurations, thus avoiding unnecessary computations.

```cpp
// The code provided in the Brute Force section is actually an implementation of the Optimal Approach using backtracking.
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n)$ in the worst case, but significantly reduced in practice due to backtracking and pruning of invalid configurations.
> - **Space Complexity:** $O(n + m)$ for storing the graph and colors.
> - **Optimality proof:** The backtracking approach ensures that all valid configurations are considered while minimizing the number of configurations to explore, making it the most efficient approach for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, graph representation, and pruning of search spaces.
- Problem-solving patterns identified: The use of backtracking to solve constraint satisfaction problems.
- Optimization techniques learned: Pruning of search spaces to reduce computational complexity.
- Similar problems to practice: Other constraint satisfaction problems, such as scheduling or resource allocation problems.

**Mistakes to Avoid:**
- Common implementation errors: Failing to properly initialize data structures or not handling edge cases correctly.
- Edge cases to watch for: Gardens with no neighbors, gardens with multiple neighbors, and the case where it's impossible to color the gardens without violating the constraints.
- Performance pitfalls: Not using backtracking or pruning, leading to exponential time complexity.
- Testing considerations: Thoroughly test the function with various inputs, including edge cases and large inputs to ensure efficiency and correctness.