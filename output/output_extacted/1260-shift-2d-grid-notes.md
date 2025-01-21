## Shift 2D Grid
**Problem Link:** https://leetcode.com/problems/shift-2d-grid/description

**Problem Statement:**
- Input format: A 2D grid `grid` and an integer `k`.
- Constraints: `1 <= m <= 50`, `1 <= n <= 50`, `1 <= k <= 100`, where `m` and `n` are the dimensions of the grid.
- Expected output format: The modified grid after shifting all elements `k` times.
- Key requirements and edge cases to consider: 
  - Handle cases where `k` is greater than the total number of elements in the grid.
  - Ensure the grid is modified in-place or return a new modified grid as required.
- Example test cases with explanations:
  - Example 1: `grid = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 1`. The output should be `[[9,1,2],[3,4,5],[6,7,8]]`.
  - Example 2: `grid = [[3,8,1,9],[19,7,2,5],[14,3,6,7],[12,15,0,16]]`, `k = 4`. The output should be `[[12,0,15,16],[3,8,1,9],[19,7,2,5],[14,3,6,7]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To shift the elements in the grid `k` times, we can repeatedly perform the shift operation `k` times.
- Step-by-step breakdown of the solution:
  1. Flatten the grid into a one-dimensional array.
  2. Perform the shift operation `k` times by moving the last element to the first position and shifting all other elements one position to the right.
  3. Reshape the array back into the original grid dimensions.
- Why this approach comes to mind first: It directly implements the problem statement without considering optimizations.

```cpp
#include <vector>
using namespace std;

vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
    int m = grid.size();
    int n = grid[0].size();
    int totalElements = m * n;
    k %= totalElements; // Reduce k to its effective shifts
    
    vector<int> flatGrid(totalElements);
    int index = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            flatGrid[index++] = grid[i][j];
        }
    }
    
    // Perform shift
    vector<int> shiftedFlatGrid(totalElements);
    for (int i = 0; i < totalElements; i++) {
        shiftedFlatGrid[(i + k) % totalElements] = flatGrid[i];
    }
    
    // Reshape back to grid
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            grid[i][j] = shiftedFlatGrid[index++];
        }
    }
    
    return grid;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k)$, where $m$ and $n$ are the dimensions of the grid. However, after optimizing `k` to its effective shifts, the time complexity becomes $O(m \cdot n)$ because we only need to perform the shift once after reducing `k`.
> - **Space Complexity:** $O(m \cdot n)$, for storing the flattened grid and the shifted grid.
> - **Why these complexities occur:** The brute force approach involves iterating over all elements in the grid to perform the shift, leading to linear time complexity with respect to the total number of elements. The space complexity is also linear because we create additional arrays to hold the flattened and shifted grids.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of shifting the grid `k` times, we can calculate the effective shift positions in one step by using the modulo operator to reduce `k` to its effective shifts within the total number of elements.
- Detailed breakdown of the approach:
  1. Flatten the grid into a one-dimensional array.
  2. Calculate the effective shift positions by reducing `k` modulo the total number of elements.
  3. Perform a single shift operation based on the effective shift positions.
  4. Reshape the array back into the original grid dimensions.
- Proof of optimality: This approach is optimal because it minimizes the number of operations required to shift the grid. By reducing `k` to its effective shifts and performing a single shift operation, we avoid unnecessary iterations.

```cpp
#include <vector>
using namespace std;

vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
    int m = grid.size();
    int n = grid[0].size();
    int totalElements = m * n;
    k %= totalElements; // Reduce k to its effective shifts
    
    vector<int> flatGrid(totalElements);
    int index = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            flatGrid[index++] = grid[i][j];
        }
    }
    
    vector<int> shiftedFlatGrid(totalElements);
    for (int i = 0; i < totalElements; i++) {
        shiftedFlatGrid[(i + k) % totalElements] = flatGrid[i];
    }
    
    index = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            grid[i][j] = shiftedFlatGrid[index++];
        }
    }
    
    return grid;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because we perform a constant amount of work for each element in the grid.
> - **Space Complexity:** $O(m \cdot n)$, for storing the flattened grid and the shifted grid.
> - **Optimality proof:** The optimal approach achieves a linear time complexity because it only requires a single pass through the grid to perform the shift, making it the most efficient solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Array flattening, modulo arithmetic for reducing shift operations, and efficient array manipulation.
- Problem-solving patterns identified: Reducing a problem to its simplest form (e.g., reducing `k` to its effective shifts) and applying basic arithmetic operations to solve complex problems.
- Optimization techniques learned: Using the modulo operator to minimize unnecessary operations and focusing on the essential steps required to solve a problem.
- Similar problems to practice: Other grid or array manipulation problems that involve shifts, rotations, or other transformations.

**Mistakes to Avoid:**
- Common implementation errors: Failing to reduce `k` to its effective shifts, which can lead to inefficient solutions.
- Edge cases to watch for: Grids with zero or one element, and cases where `k` is greater than the total number of elements.
- Performance pitfalls: Not optimizing the shift operation, leading to unnecessary iterations.
- Testing considerations: Ensure that the solution works correctly for various grid sizes and shift values, including edge cases.