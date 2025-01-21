## Check If Matrix Is X-Matrix

**Problem Link:** https://leetcode.com/problems/check-if-matrix-is-x-matrix/description

**Problem Statement:**
- Input format: A 2D integer array `grid` of size `n x n`.
- Constraints: `1 <= n <= 100` and `1 <= grid[i][j] <= n`.
- Expected output format: Return `true` if the grid is an X-Matrix, otherwise return `false`.
- Key requirements and edge cases to consider: 
    - The grid is an X-Matrix if all non-zero elements are either on the main diagonal, the anti-diagonal, or both.
    - The main diagonal consists of elements at positions `(0,0)`, `(1,1)`, `(2,2)`, etc.
    - The anti-diagonal consists of elements at positions `(0,n-1)`, `(1,n-2)`, `(2,n-3)`, etc.
- Example test cases with explanations:
    - `grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[2,0,0,0]]` returns `true`.
    - `grid = [[5,0,0],[0,0,0],[0,0,5]]` returns `false`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can simply iterate through each element in the grid.
- Step-by-step breakdown of the solution:
    1. Initialize a variable `isXMatrix` to `true`.
    2. Iterate through each element in the grid using two nested loops.
    3. For each non-zero element, check if it is on the main diagonal or the anti-diagonal.
    4. If a non-zero element is found that is not on either diagonal, set `isXMatrix` to `false` and break the loop.
- Why this approach comes to mind first: It is a straightforward approach that checks each element in the grid.

```cpp
bool checkXMatrix(vector<vector<int>>& grid) {
    int n = grid.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] != 0 && i != j && i + j != n - 1) {
                return false;
            }
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the size of the grid. This is because we are iterating through each element in the grid.
> - **Space Complexity:** $O(1)$ because we are not using any extra space that scales with input size.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops used to iterate through the grid. The space complexity is constant because we are only using a fixed amount of space to store the `isXMatrix` variable and loop counters.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but we can simplify the condition for checking non-zero elements.
- Detailed breakdown of the approach:
    1. Iterate through each element in the grid using two nested loops.
    2. For each non-zero element, check if it is on the main diagonal or the anti-diagonal using a simplified condition.
- Proof of optimality: This solution is optimal because it still checks each element in the grid once, but with a more efficient condition.
- Why further optimization is impossible: We cannot avoid checking each element in the grid because we need to verify that all non-zero elements are on the diagonals.

```cpp
bool checkXMatrix(vector<vector<int>>& grid) {
    int n = grid.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] != 0 && (i != j && i + j != n - 1)) {
                return false;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (grid[i][i] == 0 && i + i == n - 1) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the size of the grid.
> - **Space Complexity:** $O(1)$ because we are not using any extra space that scales with input size.
> - **Optimality proof:** This solution is optimal because it checks each element in the grid once, and it does so with a simple and efficient condition.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checking, and optimization of conditions.
- Problem-solving patterns identified: Checking each element in a grid and verifying that certain conditions are met.
- Optimization techniques learned: Simplifying conditions and avoiding unnecessary checks.
- Similar problems to practice: Other problems that involve checking conditions in a grid or array.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for edge cases or using incorrect conditions.
- Edge cases to watch for: Grids with all zeros, grids with non-zero elements on the diagonals, and grids with non-zero elements off the diagonals.
- Performance pitfalls: Using inefficient conditions or algorithms that have high time complexity.
- Testing considerations: Testing the function with different types of grids, including edge cases.