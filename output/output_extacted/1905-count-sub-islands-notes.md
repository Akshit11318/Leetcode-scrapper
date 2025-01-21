## Count Sub Islands

**Problem Link:** https://leetcode.com/problems/count-sub-islands/description

**Problem Statement:**
- Given a 2D grid `grid` containing `0`s (water) and `1`s (land), and a 2D array `subGrid` containing `0`s and `1`s, count the number of sub-islands in `grid` that match `subGrid`.
- A sub-island is defined as a connected component of `1`s in `grid` that matches the shape and size of `subGrid`.
- The matching condition is that the sub-island in `grid` must have the same shape and size as `subGrid`, and the corresponding elements must match.
- The function should return the count of sub-islands that match `subGrid`.

**Example Test Cases:**
- `grid = [[1,1,1,0,0],[1,1,1,0,0],[0,0,0,1,1],[0,0,0,1,1]]`, `subGrid = [[1,1,0],[0,1,0]]`
- `grid = [[1,0,1,0],[0,1,1,1],[0,0,1,0],[1,0,1,0]]`, `subGrid = [[0,0,1],[1,0,1]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over the `grid` and check every possible sub-island that matches the size of `subGrid`.
- For each possible sub-island, we compare it with `subGrid` to check if they match.
- If they match, we increment the count of sub-islands.
- This approach is straightforward but inefficient due to the high number of comparisons.

```cpp
int countSubIslands(vector<vector<int>>& grid, vector<vector<int>>& subGrid) {
    int m = grid.size(), n = grid[0].size();
    int p = subGrid.size(), q = subGrid[0].size();
    int count = 0;

    for (int i = 0; i <= m - p; i++) {
        for (int j = 0; j <= n - q; j++) {
            bool match = true;
            for (int x = 0; x < p; x++) {
                for (int y = 0; y < q; y++) {
                    if (grid[i + x][j + y] != subGrid[x][y]) {
                        match = false;
                        break;
                    }
                }
                if (!match) break;
            }
            if (match) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot p \cdot q)$, where $m$ and $n$ are the dimensions of `grid`, and $p$ and $q$ are the dimensions of `subGrid`. This is because we are iterating over `grid` and comparing each possible sub-island with `subGrid`.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The high time complexity occurs because we are performing a brute force comparison of every possible sub-island in `grid` with `subGrid`.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is to still iterate over `grid` and compare each possible sub-island with `subGrid`, but we can optimize the comparison process.
- We can use a hash-based approach or a string-based approach to compare the sub-islands, but the most straightforward optimization is to directly compare the elements as we do in the brute force approach.
- However, we can optimize the iteration process by using a more efficient algorithm to find the sub-islands, such as using a depth-first search (DFS) to find the connected components in `grid`.
- But since we need to compare each sub-island with `subGrid`, the time complexity remains the same as the brute force approach.

```cpp
int countSubIslands(vector<vector<int>>& grid, vector<vector<int>>& subGrid) {
    int m = grid.size(), n = grid[0].size();
    int p = subGrid.size(), q = subGrid[0].size();
    int count = 0;

    for (int i = 0; i <= m - p; i++) {
        for (int j = 0; j <= n - q; j++) {
            bool match = true;
            for (int x = 0; x < p; x++) {
                for (int y = 0; y < q; y++) {
                    if (grid[i + x][j + y] != subGrid[x][y]) {
                        match = false;
                        break;
                    }
                }
                if (!match) break;
            }
            if (match) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot p \cdot q)$, where $m$ and $n$ are the dimensions of `grid`, and $p$ and $q$ are the dimensions of `subGrid`.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Optimality proof:** The time complexity is optimal because we must compare each possible sub-island in `grid` with `subGrid` to count the sub-islands.

---

### Final Notes

**Learning Points:**
- The problem requires a brute force comparison of each possible sub-island in `grid` with `subGrid`.
- The optimal approach is to directly compare the elements as we do in the brute force approach.
- The time complexity is $O(m \cdot n \cdot p \cdot q)$ due to the comparison of each possible sub-island with `subGrid`.

**Mistakes to Avoid:**
- Not checking the boundaries of `grid` when comparing with `subGrid`.
- Not handling the case where `subGrid` is larger than `grid`.
- Not using a efficient algorithm to find the sub-islands in `grid`.