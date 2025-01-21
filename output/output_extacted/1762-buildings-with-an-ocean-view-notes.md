## Buildings with an Ocean View

**Problem Link:** https://leetcode.com/problems/buildings-with-an-ocean-view/description

**Problem Statement:**
- Input: An array of integers `heights` representing the heights of buildings from east to west.
- Constraints: `1 <= heights.length <= 10^5`.
- Expected Output: A list of indices of buildings that have an ocean view from the west.
- Key Requirements: A building has an ocean view if all the buildings to its west are shorter.
- Example Test Cases:
  - `heights = [4,2,3,1]`, Output: `[0,2,3]`.
  - `heights = [4,3,2,1]`, Output: `[0,1,2,3]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through each building and check all the buildings to its west to see if any are taller.
- Step-by-step breakdown:
  1. Iterate through each building in the `heights` array.
  2. For each building, iterate through all the buildings to its west.
  3. If any building to the west is taller or the same height, mark the current building as not having an ocean view.
  4. If no taller buildings are found to the west, add the current building's index to the result list.
- Why this approach comes to mind first: It directly implements the problem's conditions without considering optimizations.

```cpp
vector<int> findBuildings(vector<int>& heights) {
    vector<int> result;
    for (int i = 0; i < heights.size(); ++i) {
        bool hasOceanView = true;
        for (int j = 0; j < i; ++j) {
            if (heights[j] >= heights[i]) {
                hasOceanView = false;
                break;
            }
        }
        if (hasOceanView) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of buildings. This is because for each building, we potentially check all the buildings to its west.
> - **Space Complexity:** $O(n)$, for storing the indices of buildings with an ocean view.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, and the space complexity is due to the storage of the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking all buildings to the west for each building, we can keep track of the maximum height seen so far from the west as we iterate through the buildings.
- Detailed breakdown:
  1. Initialize an empty result list and a variable `maxHeightFromWest` to 0.
  2. Iterate through the `heights` array from west to east.
  3. For each building, if its height is greater than `maxHeightFromWest`, it has an ocean view. Add its index to the result list and update `maxHeightFromWest`.
- Proof of optimality: This approach ensures that each building is checked only once, resulting in a linear time complexity, which is the best possible for this problem since we must examine each building at least once.

```cpp
vector<int> findBuildings(vector<int>& heights) {
    vector<int> result;
    int maxHeightFromWest = 0;
    for (int i = heights.size() - 1; i >= 0; --i) {
        if (heights[i] > maxHeightFromWest) {
            result.push_back(i);
            maxHeightFromWest = heights[i];
        }
    }
    // Reverse the result since we iterated from east to west
    reverse(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of buildings. This is because we make a single pass through the `heights` array.
> - **Space Complexity:** $O(n)$, for storing the indices of buildings with an ocean view.
> - **Optimality proof:** The linear time complexity is optimal because we only examine each building once, and the space complexity is necessary for storing the result.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Using a single pass through the data to keep track of the maximum value seen so far can significantly improve efficiency.
- Problem-solving pattern: Identifying how to avoid redundant checks (like checking all buildings to the west for each building) is crucial for optimization.
- Optimization technique: Iterating from east to west allows us to keep track of the maximum height seen from the west efficiently.

**Mistakes to Avoid:**
- Common implementation error: Forgetting to update the `maxHeightFromWest` variable when a taller building is found.
- Edge case to watch for: Handling the case when there are no buildings or when all buildings have the same height.
- Performance pitfall: Using nested loops without considering optimizations can lead to inefficient solutions.
- Testing consideration: Ensure to test with various inputs, including edge cases like empty arrays or arrays with a single element.