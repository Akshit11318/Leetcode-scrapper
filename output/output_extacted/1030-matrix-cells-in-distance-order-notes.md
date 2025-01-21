## Matrix Cells in Distance Order
**Problem Link:** https://leetcode.com/problems/matrix-cells-in-distance-order/description

**Problem Statement:**
- Input: `R` (number of rows), `C` (number of columns), and `r0` and `c0` (starting cell coordinates).
- Constraints: `1 <= R <= 10^5`, `1 <= C <= 10^5`, `0 <= r0 < R`, `0 <= c0 < C`.
- Expected Output: A list of coordinates `[r, c]` representing cells in the matrix, sorted in ascending order of their distance from the cell `[r0, c0]`.
- Key Requirements: The distance between two cells `[r1, c1]` and `[r2, c2]` is defined as `|r1 - r2| + |c1 - c2|`.
- Example Test Cases:
  - Input: `R = 1, C = 2, r0 = 0, c0 = 0`. Output: `[[0,0],[0,1]]`.
  - Input: `R = 2, C = 2, r0 = 0, c0 = 1`. Output: `[[0,1],[0,0],[1,1],[1,0]]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves calculating the distance of each cell from the given cell `[r0, c0]`.
- Then, sort these cells based on their distances.
- This approach comes to mind first because it directly addresses the problem statement without considering optimizations.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

struct Cell {
    int r, c, distance;
};

vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0) {
    vector<Cell> cells;
    for (int r = 0; r < R; ++r) {
        for (int c = 0; c < C; ++c) {
            Cell cell;
            cell.r = r;
            cell.c = c;
            cell.distance = abs(r - r0) + abs(c - c0);
            cells.push_back(cell);
        }
    }
    
    sort(cells.begin(), cells.end(), [](const Cell& a, const Cell& b) {
        return a.distance < b.distance;
    });
    
    vector<vector<int>> result;
    for (const auto& cell : cells) {
        result.push_back({cell.r, cell.c});
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(R \cdot C \cdot \log(R \cdot C))$ due to sorting all cells.
> - **Space Complexity:** $O(R \cdot C)$ for storing all cells.
> - **Why these complexities occur:** The brute force approach involves iterating over all cells to calculate distances and then sorting them, leading to these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a data structure that allows efficient insertion and retrieval of cells in ascending order of their distances.
- A `vector` of `pair<int, pair<int, int>>` can be used to store distances along with cell coordinates. This allows for sorting based on distance.
- This approach is optimal because it avoids unnecessary sorting by inserting cells in order of their distances.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0) {
    vector<vector<int>> result;
    int maxDistance = R + C - 2; // Maximum possible distance
    
    for (int d = 0; d <= maxDistance; ++d) {
        for (int r = max(0, r0 - d); r <= min(R - 1, r0 + d); ++r) {
            int c = c0 + d - abs(r - r0);
            if (c >= 0 && c < C) {
                result.push_back({r, c});
            }
            c = c0 - d + abs(r - r0);
            if (c >= 0 && c < C && c != c0 + d - abs(r - r0)) {
                result.push_back({r, c});
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(R \cdot C)$, as we are visiting each cell once.
> - **Space Complexity:** $O(R \cdot C)$ for storing the result.
> - **Optimality proof:** This approach is optimal because it directly constructs the result in the required order without any unnecessary operations, achieving linear time complexity relative to the output size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, distance calculation, and efficient iteration.
- Problem-solving patterns identified: using the right data structure for efficient sorting and iteration.
- Optimization techniques learned: avoiding unnecessary sorting and using iteration to directly construct the result.
- Similar problems to practice: other problems involving sorting and iteration, such as those involving grids or matrices.

**Mistakes to Avoid:**
- Common implementation errors: incorrect distance calculations or missing cells.
- Edge cases to watch for: boundary conditions (e.g., cells at the edges of the matrix).
- Performance pitfalls: using inefficient sorting algorithms or data structures.
- Testing considerations: thoroughly testing with different inputs, including edge cases.