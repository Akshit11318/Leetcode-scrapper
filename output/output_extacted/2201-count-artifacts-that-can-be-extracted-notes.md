## Count Artifacts That Can Be Extracted
**Problem Link:** https://leetcode.com/problems/count-artifacts-that-can-be-extracted/description

**Problem Statement:**
- Input format and constraints: Given a 2D grid `grid` representing an archaeological site, where each cell can contain an artifact, and a list of `artifacts` which are rectangles with their top-left and bottom-right corners represented as `[row1, col1, row2, col2]`.
- Expected output format: The number of artifacts that can be extracted, which means the entire rectangle is covered by the dig area.
- Key requirements and edge cases to consider: Overlapping artifacts, artifacts outside the grid, and empty input lists.
- Example test cases with explanations: 
  - A single artifact fully covered by the dig area should return 1.
  - Multiple artifacts partially covered should return the count of fully covered ones.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each artifact's rectangle against the dig area to see if it's fully covered.
- Step-by-step breakdown of the solution: Iterate through each artifact, and for each one, check every cell within its rectangle to see if it's within the dig area.
- Why this approach comes to mind first: It's straightforward and checks every condition directly.

```cpp
int countArtifacts(int** grid, int gridSize, int* gridColSize, int** artifacts, int artifactsSize, int* artifactsColSize) {
    int count = 0;
    for (int i = 0; i < artifactsSize; i++) {
        bool covered = true;
        for (int row = artifacts[i][0]; row <= artifacts[i][2]; row++) {
            for (int col = artifacts[i][1]; col <= artifacts[i][3]; col++) {
                if (grid[row][col] != 1) {
                    covered = false;
                    break;
                }
            }
            if (!covered) break;
        }
        if (covered) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(artifactsSize \times (row_{max} - row_{min} + 1) \times (col_{max} - col_{min} + 1))$ where $row_{max}$, $row_{min}$, $col_{max}$, and $col_{min}$ are the maximum and minimum row and column indices of all artifacts. This simplifies to $O(n \times m \times p)$ where $n$ is the number of artifacts, $m$ and $p$ are the maximum dimensions of an artifact's rectangle.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the count of covered artifacts and other variables.
> - **Why these complexities occur:** The nested loops over the artifacts and their dimensions cause the time complexity. The space complexity is constant because we don't use any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already quite straightforward and optimal in terms of time complexity for this problem because we must check every cell of every artifact. However, we can slightly optimize by breaking out of the loop as soon as we find a cell not covered by the dig area.
- Detailed breakdown of the approach: Same as brute force but with an early exit condition.
- Proof of optimality: Since we must check every cell of every artifact to determine if it's fully covered, the time complexity cannot be improved beyond what's necessary to check each cell once.

```cpp
int countArtifacts(int** grid, int gridSize, int* gridColSize, int** artifacts, int artifactsSize, int* artifactsColSize) {
    int count = 0;
    for (int i = 0; i < artifactsSize; i++) {
        bool covered = true;
        for (int row = artifacts[i][0]; row <= artifacts[i][2] && covered; row++) {
            for (int col = artifacts[i][1]; col <= artifacts[i][3] && covered; col++) {
                if (grid[row][col] != 1) {
                    covered = false;
                }
            }
        }
        if (covered) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(artifactsSize \times (row_{max} - row_{min} + 1) \times (col_{max} - col_{min} + 1))$ or $O(n \times m \times p)$, same as the brute force approach because we still potentially check every cell of every artifact.
> - **Space Complexity:** $O(1)$, same as the brute force approach.
> - **Optimality proof:** This is optimal because we must check every cell of every artifact to ensure it's fully covered. Any algorithm must at least read the input, which requires $O(n \times m \times p)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over multidimensional data structures, conditional checks within nested loops.
- Problem-solving patterns identified: Checking each element of a structure (in this case, cells of an artifact) against a condition.
- Optimization techniques learned: Early exit from loops when a condition is met.
- Similar problems to practice: Other grid-based problems involving conditional checks.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check boundaries or missing the early exit condition.
- Edge cases to watch for: Empty input lists, artifacts outside the grid.
- Performance pitfalls: Not optimizing the loop conditions.
- Testing considerations: Ensure to test with various artifact sizes, positions, and overlaps.