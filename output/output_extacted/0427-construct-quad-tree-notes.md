## Construct Quad Tree
**Problem Link:** https://leetcode.com/problems/construct-quad-tree/description

**Problem Statement:**
- Input format: A 2D grid of size `n x n`, where `n` is a power of 2.
- Constraints: `1 <= n <= 2^10`, where `n` is the number of rows and columns in the grid.
- Expected output format: The root of the constructed quad tree.
- Key requirements and edge cases to consider:
  - The grid contains only `0` and `1` values.
  - The quad tree should be constructed based on the given grid.
  - If all cells in the grid have the same value, the quad tree should have only one node.
- Example test cases with explanations:
  - A grid with all `0` values should result in a quad tree with a single node having a value of `0`.
  - A grid with all `1` values should result in a quad tree with a single node having a value of `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Divide the grid into four quadrants and recursively construct the quad tree for each quadrant.
- Step-by-step breakdown of the solution:
  1. Check if all cells in the grid have the same value. If yes, return a leaf node with that value.
  2. If not, divide the grid into four quadrants.
  3. Recursively construct the quad tree for each quadrant.
  4. Create a new node with the four child nodes as the quadrants.

```cpp
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node() : val(false), isLeaf(false), topLeft(nullptr), topRight(nullptr), bottomLeft(nullptr), bottomRight(nullptr) {}
    Node(bool _val, bool _isLeaf) : val(_val), isLeaf(_isLeaf), topLeft(nullptr), topRight(nullptr), bottomLeft(nullptr), bottomRight(nullptr) {}
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) : val(_val), isLeaf(_isLeaf), topLeft(_topLeft), topRight(_topRight), bottomLeft(_bottomLeft), bottomRight(_bottomRight) {}
};

class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        return constructTree(grid, 0, 0, grid.size());
    }

    Node* constructTree(vector<vector<int>>& grid, int x, int y, int size) {
        // Check if all cells in the grid have the same value
        int val = grid[x][y];
        bool isSame = true;
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (grid[i][j] != val) {
                    isSame = false;
                    break;
                }
            }
            if (!isSame) break;
        }

        if (isSame) {
            return new Node(val, true);
        } else {
            // Divide the grid into four quadrants
            int newSize = size / 2;
            Node* topLeft = constructTree(grid, x, y, newSize);
            Node* topRight = constructTree(grid, x, y + newSize, newSize);
            Node* bottomLeft = constructTree(grid, x + newSize, y, newSize);
            Node* bottomRight = constructTree(grid, x + newSize, y + newSize, newSize);

            return new Node(1, false, topLeft, topRight, bottomLeft, bottomRight);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows and columns in the grid. This is because we are recursively dividing the grid into four quadrants and checking each cell in the grid.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of rows and columns in the grid. This is because we are creating a new node for each quadrant in the grid.
> - **Why these complexities occur:** These complexities occur because we are recursively dividing the grid into four quadrants and checking each cell in the grid.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Divide the grid into four quadrants and recursively construct the quad tree for each quadrant. Use a helper function to check if all cells in the grid have the same value.
- Detailed breakdown of the approach:
  1. Check if all cells in the grid have the same value using a helper function.
  2. If all cells have the same value, return a leaf node with that value.
  3. If not, divide the grid into four quadrants.
  4. Recursively construct the quad tree for each quadrant.
  5. Create a new node with the four child nodes as the quadrants.

```cpp
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node() : val(false), isLeaf(false), topLeft(nullptr), topRight(nullptr), bottomLeft(nullptr), bottomRight(nullptr) {}
    Node(bool _val, bool _isLeaf) : val(_val), isLeaf(_isLeaf), topLeft(nullptr), topRight(nullptr), bottomLeft(nullptr), bottomRight(nullptr) {}
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) : val(_val), isLeaf(_isLeaf), topLeft(_topLeft), topRight(_topRight), bottomLeft(_bottomLeft), bottomRight(_bottomRight) {}
};

class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        return constructTree(grid, 0, 0, grid.size());
    }

    bool isSame(vector<vector<int>>& grid, int x, int y, int size) {
        int val = grid[x][y];
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (grid[i][j] != val) return false;
            }
        }
        return true;
    }

    Node* constructTree(vector<vector<int>>& grid, int x, int y, int size) {
        if (isSame(grid, x, y, size)) {
            return new Node(grid[x][y], true);
        } else {
            int newSize = size / 2;
            Node* topLeft = constructTree(grid, x, y, newSize);
            Node* topRight = constructTree(grid, x, y + newSize, newSize);
            Node* bottomLeft = constructTree(grid, x + newSize, y, newSize);
            Node* bottomRight = constructTree(grid, x + newSize, y + newSize, newSize);

            return new Node(1, false, topLeft, topRight, bottomLeft, bottomRight);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows and columns in the grid. This is because we are recursively dividing the grid into four quadrants and checking each cell in the grid.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of rows and columns in the grid. This is because we are creating a new node for each quadrant in the grid.
> - **Optimality proof:** This solution is optimal because it has a time complexity of $O(n^2)$, which is the minimum time complexity required to check each cell in the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, Divide and Conquer.
- Problem-solving patterns identified: Checking if all cells in the grid have the same value, recursively dividing the grid into four quadrants.
- Optimization techniques learned: Using a helper function to check if all cells in the grid have the same value.
- Similar problems to practice: Constructing a quad tree from a grid with different values, constructing a quad tree from a grid with a different size.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if all cells in the grid have the same value, not recursively dividing the grid into four quadrants.
- Edge cases to watch for: Grids with all `0` values, grids with all `1` values, grids with different sizes.
- Performance pitfalls: Not using a helper function to check if all cells in the grid have the same value, not recursively dividing the grid into four quadrants.
- Testing considerations: Testing the solution with different grid sizes, testing the solution with grids having all `0` values, testing the solution with grids having all `1` values.