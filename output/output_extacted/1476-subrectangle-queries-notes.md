## Subrectangle Queries

**Problem Link:** [https://leetcode.com/problems/subrectangle-queries/description](https://leetcode.com/problems/subrectangle-queries/description)

**Problem Statement:**
- Input format and constraints: The problem involves a 2D grid of integers, represented as a vector of vectors (`rectangle`). The task is to implement a class (`SubrectangleQueries`) that supports two operations: 
    1. `void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)`: Updates all values in the subrectangle defined by the top-left corner `(row1, col1)` and the bottom-right corner `(row2, col2)` to `newValue`.
    2. `int getValue(int row, int col)`: Returns the value at the cell `(row, col)`.
- Expected output format: The class should support the above operations efficiently, and the output of the `getValue` operation should be an integer representing the value at the specified cell.
- Key requirements and edge cases to consider: 
    - The grid can have varying dimensions.
    - Updates and queries can occur at any cell within the grid.
    - The grid's dimensions and the number of operations are within reasonable limits (e.g., up to 100x100 cells and up to 100 operations).
- Example test cases with explanations: 
    - Creating a `SubrectangleQueries` object with a 3x3 grid: `SubrectangleQueries rectangle = new SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])`.
    - Updating a subrectangle: `rectangle.updateSubrectangle(0, 0, 2, 2, 5)`.
    - Querying a cell's value: `rectangle.getValue(0, 0)` should return the updated value if the cell falls within the updated subrectangle.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Store the 2D grid as a vector of vectors and perform operations directly on this grid.
- Step-by-step breakdown of the solution:
    1. Initialize the grid with the given values.
    2. For the `updateSubrectangle` operation, iterate over the specified subrectangle and update each cell's value to the new value.
    3. For the `getValue` operation, simply return the value at the specified cell coordinates.
- Why this approach comes to mind first: It directly addresses the problem statement by manipulating the grid as described.

```cpp
class SubrectangleQueries {
public:
    vector<vector<int>> grid;
    
    SubrectangleQueries(vector<vector<int>>& rectangle) {
        grid = rectangle;
    }
    
    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        for (int i = row1; i <= row2; ++i) {
            for (int j = col1; j <= col2; ++j) {
                grid[i][j] = newValue;
            }
        }
    }
    
    int getValue(int row, int col) {
        return grid[row][col];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ for the `updateSubrectangle` operation, where $m$ and $n$ are the dimensions of the subrectangle, and $O(1)$ for the `getValue` operation.
> - **Space Complexity:** $O(M \cdot N)$, where $M$ and $N$ are the dimensions of the entire grid.
> - **Why these complexities occur:** The brute force approach directly manipulates the grid, leading to linear time complexity for updates and constant time complexity for queries.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves maintaining the original grid and only updating the subrectangles as needed. This approach is already implemented in the brute force solution.
- Detailed breakdown of the approach: Since the problem requires updating subrectangles and querying individual cells, the optimal approach is to directly manipulate the grid as in the brute force solution. However, we can slightly optimize the `updateSubrectangle` operation by using iterators or pointer arithmetic for the inner loop, although the time complexity remains the same.
- Proof of optimality: The operations are inherently dependent on the size of the subrectangle for updates and the position of the cell for queries, making the current implementation optimal for these specific operations.

```cpp
class SubrectangleQueries {
public:
    vector<vector<int>> grid;
    
    SubrectangleQueries(vector<vector<int>>& rectangle) {
        grid = rectangle;
    }
    
    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        for (int i = row1; i <= row2; ++i) {
            // Using iterators or pointer arithmetic does not change the complexity
            for (int j = col1; j <= col2; ++j) {
                grid[i][j] = newValue;
            }
        }
    }
    
    int getValue(int row, int col) {
        return grid[row][col];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ for the `updateSubrectangle` operation, where $m$ and $n$ are the dimensions of the subrectangle, and $O(1)$ for the `getValue` operation.
> - **Space Complexity:** $O(M \cdot N)$, where $M$ and $N$ are the dimensions of the entire grid.
> - **Optimality proof:** The operations are performed in the most straightforward manner possible, given the problem constraints and the nature of the operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct manipulation of a 2D grid, iteration over subrectangles.
- Problem-solving patterns identified: Breaking down complex operations into simpler, iterative steps.
- Optimization techniques learned: While the brute force approach is already optimal for this problem, recognizing when direct manipulation is sufficient is an important skill.
- Similar problems to practice: Other grid or matrix manipulation problems, such as finding paths or performing more complex queries.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly indexing the grid, failing to update or query the correct subrectangle or cell.
- Edge cases to watch for: Grid boundaries, empty grids, and queries or updates that fall outside the grid's dimensions.
- Performance pitfalls: Unnecessary iterations or recursive calls that could lead to exponential time complexity.
- Testing considerations: Ensure that the solution handles various grid sizes, update and query operations, and edge cases correctly.