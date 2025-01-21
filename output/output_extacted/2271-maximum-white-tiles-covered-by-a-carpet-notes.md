## Maximum White Tiles Covered by a Carpet

**Problem Link:** https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/description

**Problem Statement:**
- Input format and constraints: The problem involves finding the maximum number of white tiles that can be covered by a carpet of a given length, considering the positions and lengths of white and black tiles.
- Expected output format: The function should return the maximum number of white tiles that can be covered.
- Key requirements and edge cases to consider: We need to handle cases where the carpet can start at any position, including before the first white tile or after the last white tile, and where the carpet length exceeds the total length of all tiles.
- Example test cases with explanations: For example, given a carpet length of 10 and white tile positions [(1,5),(10,11),(12,18),(20,25),(30,32)], the maximum number of white tiles covered should be calculated considering all possible positions of the carpet.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking every possible position where the carpet could start and calculating the number of white tiles covered in each case.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible start positions for the carpet.
  2. For each start position, calculate the end position based on the carpet length.
  3. For each white tile, check if it falls within the start and end positions of the carpet.
  4. Count the number of white tiles that fall within the carpet's range.
  5. Keep track of the maximum count found across all possible start positions.

```cpp
int maximumWhiteTiles(vector<vector<int>>& tiles, int carpetLen) {
    int maxWhiteTiles = 0;
    for (int start = 0; start <= 10000; start++) {
        int whiteTiles = 0;
        for (auto& tile : tiles) {
            if (start <= tile[0] && tile[0] + tile[1] - 1 <= start + carpetLen - 1) {
                whiteTiles += tile[1];
            } else if (start <= tile[0] + tile[1] - 1 && start + carpetLen - 1 >= tile[0]) {
                whiteTiles += min(tile[0] + tile[1], start + carpetLen) - max(tile[0], start);
            }
        }
        maxWhiteTiles = max(maxWhiteTiles, whiteTiles);
    }
    return maxWhiteTiles;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of possible start positions (up to 10000 in this case) and $m$ is the number of white tiles.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum count and other variables.
> - **Why these complexities occur:** The time complexity is high due to iterating over all possible start positions and checking each white tile against the carpet's range. The space complexity is low since we don't use any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a prefix sum array to efficiently calculate the number of white tiles covered by the carpet at any position.
- Detailed breakdown of the approach:
  1. Create a prefix sum array `ps` where `ps[i]` represents the total length of white tiles up to position `i`.
  2. Iterate over all possible start positions for the carpet.
  3. For each start position, use the prefix sum array to efficiently calculate the number of white tiles covered by the carpet.
  4. Keep track of the maximum count found across all possible start positions.

```cpp
int maximumWhiteTiles(vector<vector<int>>& tiles, int carpetLen) {
    vector<int> ps(10001, 0);
    for (auto& tile : tiles) {
        for (int i = tile[0]; i <= tile[0] + tile[1] - 1; i++) {
            ps[i]++;
        }
    }
    for (int i = 1; i <= 10000; i++) {
        ps[i] += ps[i - 1];
    }
    int maxWhiteTiles = 0;
    for (int start = 1; start <= 10000; start++) {
        int end = min(start + carpetLen - 1, 10000);
        int whiteTiles = ps[end] - (start - 1 >= 0 ? ps[start - 1] : 0);
        maxWhiteTiles = max(maxWhiteTiles, whiteTiles);
    }
    return maxWhiteTiles;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of positions (up to 10000) and $m$ is the total length of all white tiles.
> - **Space Complexity:** $O(n)$, for storing the prefix sum array.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity significantly by using a prefix sum array to calculate the number of white tiles covered in constant time for each start position.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum arrays for efficient calculation of cumulative sums.
- Problem-solving patterns identified: Using data structures to reduce time complexity.
- Optimization techniques learned: Applying prefix sum arrays to simplify calculations.
- Similar problems to practice: Other problems involving range queries or cumulative sums.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the prefix sum array or miscalculating the end position of the carpet.
- Edge cases to watch for: Handling cases where the carpet starts before the first white tile or ends after the last white tile.
- Performance pitfalls: Using a brute force approach without considering optimizations.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases.