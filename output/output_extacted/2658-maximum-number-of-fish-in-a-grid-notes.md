## Maximum Number of Fish in a Grid
**Problem Link:** https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description

**Problem Statement:**
- Input format: A `grid` of integers representing the number of fish in each cell, and a `k` value representing the maximum number of fish that can be caught in a single day.
- Expected output format: The maximum number of fish that can be caught.
- Key requirements and edge cases to consider: The grid can be empty, `k` can be larger than the number of cells, and the number of fish in each cell can vary.
- Example test cases with explanations: 
    - An empty grid with `k = 0` should return `0`.
    - A grid with a single cell containing `1` fish and `k = 1` should return `1`.
    - A grid with multiple cells containing different numbers of fish and `k = 2` should return the maximum possible catch.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of catching fish from the grid and keep track of the maximum catch.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of cells to catch fish from.
    2. For each combination, calculate the total number of fish caught.
    3. Keep track of the maximum catch.
- Why this approach comes to mind first: It's a straightforward way to ensure we don't miss any possible solutions.

```cpp
class Solution {
public:
    int maxFish(vector<vector<int>>& grid, int k) {
        int maxCatch = 0;
        int rows = grid.size();
        int cols = grid[0].size();
        
        // Generate all possible combinations of cells to catch fish from
        for (int mask = 0; mask < (1 << (rows * cols)); mask++) {
            int catchCount = 0;
            int fishCaught = 0;
            
            // Calculate the total number of fish caught for the current combination
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    if ((mask & (1 << (i * cols + j))) != 0) {
                        catchCount++;
                        fishCaught += grid[i][j];
                    }
                }
            }
            
            // Keep track of the maximum catch
            if (catchCount <= k && fishCaught > maxCatch) {
                maxCatch = fishCaught;
            }
        }
        
        return maxCatch;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m \cdot n} \cdot m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we generate all possible combinations of cells and for each combination, we iterate over the grid.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. This is because we only use a constant amount of space to store the maximum catch and other variables.
> - **Why these complexities occur:** The brute force approach is inherently inefficient because it tries all possible combinations, leading to exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a greedy approach by always choosing the cell with the maximum number of fish.
- Detailed breakdown of the approach:
    1. Initialize a priority queue to store cells with their fish counts.
    2. Add all cells to the priority queue.
    3. While the number of cells caught is less than `k`, remove the cell with the maximum fish count from the priority queue and add its fish count to the total catch.
- Proof of optimality: This approach is optimal because it always chooses the cell with the maximum number of fish, ensuring the maximum possible catch.

```cpp
class Solution {
public:
    int maxFish(vector<vector<int>>& grid, int k) {
        int maxCatch = 0;
        int rows = grid.size();
        int cols = grid[0].size();
        
        // Initialize a priority queue to store cells with their fish counts
        priority_queue<int> pq;
        
        // Add all cells to the priority queue
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                pq.push(grid[i][j]);
            }
        }
        
        // While the number of cells caught is less than k, remove the cell with the maximum fish count from the priority queue and add its fish count to the total catch
        for (int i = 0; i < k; i++) {
            if (!pq.empty()) {
                maxCatch += pq.top();
                pq.pop();
            } else {
                break;
            }
        }
        
        return maxCatch;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \log(m \cdot n))$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we add all cells to the priority queue and then remove the maximum cell $k$ times.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we store all cells in the priority queue.
> - **Optimality proof:** This approach is optimal because it always chooses the cell with the maximum number of fish, ensuring the maximum possible catch.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, priority queue.
- Problem-solving patterns identified: Always choosing the maximum or minimum value to optimize the solution.
- Optimization techniques learned: Using a priority queue to efficiently select the maximum or minimum value.
- Similar problems to practice: Other problems that involve selecting the maximum or minimum value to optimize the solution.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty grid or `k` being larger than the number of cells.
- Edge cases to watch for: An empty grid, `k` being larger than the number of cells, and the number of fish in each cell being zero.
- Performance pitfalls: Using an inefficient data structure, such as a linear search, to find the maximum or minimum value.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure it works correctly.