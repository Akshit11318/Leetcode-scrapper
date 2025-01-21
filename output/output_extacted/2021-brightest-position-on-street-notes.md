## Brightest Position on Street

**Problem Link:** https://leetcode.com/problems/brightest-position-on-street/description

**Problem Statement:**
- Input: `n`, `lamps` - The number of lights on the street and their positions.
- Constraints: `1 <= n <= 10^5`, `1 <= lamps.length <= 10^5`, `0 <= lamps[i] <= 10^5`.
- Expected Output: The position on the street where the light is the brightest.
- Key Requirements:
  - Each lamp has a radius of `1`.
  - The brightness of a position is the number of lamps that illuminate it.
- Edge Cases:
  - If there are multiple positions with the same maximum brightness, return any one of them.
- Example Test Cases:
  - `n = 3`, `lamps = [2]`, The brightest position is at `2`.
  - `n = 2`, `lamps = [1, 1]`, The brightest position is at `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check each position on the street and calculate how many lamps illuminate it.
- Step-by-step breakdown:
  1. Iterate over each position on the street.
  2. For each position, check how many lamps are within a distance of `1`.
  3. Keep track of the position with the maximum brightness.

```cpp
int brightestPosition(int n, vector<int>& lamps) {
    int maxBrightness = 0;
    int brightestPos = 0;
    for (int pos = 0; pos <= n; pos++) {
        int brightness = 0;
        for (int lamp : lamps) {
            if (abs(pos - lamp) <= 1) {
                brightness++;
            }
        }
        if (brightness > maxBrightness) {
            maxBrightness = brightness;
            brightestPos = pos;
        }
    }
    return brightestPos;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of positions on the street and $m$ is the number of lamps. This is because for each position, we iterate over all lamps.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum brightness and the brightest position.
> - **Why these complexities occur:** The brute force approach is inefficient because it checks every lamp for every position, leading to a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we only need to consider positions that are within a distance of `1` from any lamp.
- Detailed breakdown:
  1. Create a set of positions that are within a distance of `1` from any lamp.
  2. Iterate over these positions and calculate their brightness.
  3. Keep track of the position with the maximum brightness.

```cpp
int brightestPosition(int n, vector<int>& lamps) {
    unordered_set<int> positions;
    for (int lamp : lamps) {
        for (int pos = max(0, lamp - 1); pos <= min(n, lamp + 1); pos++) {
            positions.insert(pos);
        }
    }
    int maxBrightness = 0;
    int brightestPos = 0;
    for (int pos : positions) {
        int brightness = 0;
        for (int lamp : lamps) {
            if (abs(pos - lamp) <= 1) {
                brightness++;
            }
        }
        if (brightness > maxBrightness) {
            maxBrightness = brightness;
            brightestPos = pos;
        }
    }
    return brightestPos;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot k + m \cdot p)$ where $m$ is the number of lamps, $k$ is the average number of positions within a distance of `1` from a lamp, and $p$ is the number of unique positions. This is because we first generate the positions and then iterate over them.
> - **Space Complexity:** $O(p)$, as we store the unique positions in a set.
> - **Optimality proof:** This approach is optimal because we only consider positions that can potentially have a high brightness, reducing the number of iterations significantly.

---

### Final Notes

**Learning Points:**
- The importance of reducing the search space in optimization problems.
- Using data structures like sets to efficiently store and iterate over unique elements.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Not considering the constraints of the problem, leading to inefficient solutions.
- Not optimizing the iteration over the search space.
- Not using the right data structures for the problem at hand.

---