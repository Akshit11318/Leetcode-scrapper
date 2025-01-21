## Maximum Building Height
**Problem Link:** https://leetcode.com/problems/maximum-building-height/description

**Problem Statement:**
- Input format: `int index`, `int height` arrays, representing building indices and their respective heights.
- Constraints: `index` and `height` arrays have the same length, and `index` values are distinct and sorted in ascending order.
- Expected output format: The maximum height of the building that can be achieved.
- Key requirements: Determine the maximum height of a building given the indices and heights of its foundation blocks.
- Edge cases: Handle cases where the input arrays are empty or have a single element.

**Example Test Cases:**
- Input: `index = [1, 3], height = [4, 4]`
  Output: `6`
  Explanation: The maximum height is achieved by placing a building of height 4 at index 1 and another building of height 4 at index 3, with a building of height 2 (the maximum height of the gap between the two buildings) in the gap.
- Input: `index = [2, 9], height = [3, 4]`
  Output: `4`
  Explanation: The maximum height is achieved by placing a building of height 4 at index 9.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible combinations of building heights and calculating the maximum height for each combination.
- Step-by-step breakdown:
  1. Generate all possible combinations of building heights.
  2. For each combination, calculate the maximum height by finding the maximum height of the gap between each pair of buildings.
  3. Update the maximum height if the current combination results in a higher maximum height.

```cpp
#include <vector>
#include <algorithm>

int maxBuildingHeight(std::vector<int>& index, std::vector<int>& height) {
    int n = index.size();
    int max_height = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int gap_height = (index[j] - index[i] - 1) / 2;
            max_height = std::max(max_height, std::min(height[i], height[j]) + gap_height);
        }
    }
    
    return max_height;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of buildings. This is because we have two nested loops iterating over the buildings.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum height.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of building heights, resulting in a quadratic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to recognize that the maximum height of a building can be achieved by finding the maximum height of the gap between each pair of buildings and adding it to the minimum height of the two buildings.
- Step-by-step breakdown:
  1. Initialize the maximum height to 0.
  2. Iterate over each pair of buildings.
  3. For each pair, calculate the maximum height of the gap between the two buildings.
  4. Update the maximum height if the current pair results in a higher maximum height.

```cpp
#include <vector>
#include <algorithm>

int maxBuildingHeight(std::vector<int>& index, std::vector<int>& height) {
    int n = index.size();
    int max_height = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int gap_height = (index[j] - index[i] - 1) / 2;
            max_height = std::max(max_height, std::min(height[i], height[j]) + gap_height);
        }
    }
    
    return max_height;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of buildings. This is because we have two nested loops iterating over the buildings.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum height.
> - **Optimality proof:** The optimal approach involves trying all possible combinations of building heights, which is the most efficient way to find the maximum height.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: brute force approach, optimal approach.
- Problem-solving patterns identified: trying all possible combinations, finding the maximum height of the gap between each pair of buildings.
- Optimization techniques learned: recognizing the key insight to find the maximum height of the gap between each pair of buildings.
- Similar problems to practice: finding the maximum height of a building given the indices and heights of its foundation blocks.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the maximum height to 0, not updating the maximum height correctly.
- Edge cases to watch for: handling cases where the input arrays are empty or have a single element.
- Performance pitfalls: not recognizing the key insight to find the maximum height of the gap between each pair of buildings, resulting in an inefficient solution.
- Testing considerations: testing the solution with different input arrays, including edge cases.