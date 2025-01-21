## Maximize the Total Height of Unique Towers
**Problem Link:** https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers `heights` and an integer `bricks` as input. The `heights` array represents the heights of towers, and `bricks` represents the number of bricks available to add to the towers. The goal is to maximize the total height of unique towers.
- Expected output format: The output should be an integer representing the maximum total height of unique towers.
- Key requirements and edge cases to consider: The problem requires finding a subset of towers that can be made unique by adding bricks, such that the total height is maximized.
- Example test cases with explanations: For example, given `heights = [1,2,3,4,5]` and `bricks = 5`, the output should be `15` because we can make the towers unique by adding bricks to the smaller towers.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of adding bricks to the towers to make them unique.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of adding bricks to the towers.
  2. For each combination, calculate the total height of the unique towers.
  3. Keep track of the maximum total height found.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the large number of combinations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maximizeHeight(vector<int>& heights, int bricks) {
    int n = heights.size();
    int max_height = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> unique_heights;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                unique_heights.push_back(heights[i]);
            }
        }
        sort(unique_heights.begin(), unique_heights.end());
        int total_bricks = bricks;
        for (int i = 0; i < unique_heights.size() - 1; i++) {
            int diff = unique_heights[i + 1] - unique_heights[i];
            if (diff > 0) {
                total_bricks -= diff;
            }
        }
        if (total_bricks >= 0) {
            int total_height = 0;
            for (int height : unique_heights) {
                total_height += height;
            }
            max_height = max(max_height, total_height);
        }
    }
    return max_height;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \log n)$, where $n$ is the number of towers. This is because we generate all possible combinations of adding bricks to the towers, and for each combination, we sort the unique heights.
> - **Space Complexity:** $O(n)$, where $n$ is the number of towers. This is because we store the unique heights for each combination.
> - **Why these complexities occur:** The high time complexity occurs because we generate all possible combinations of adding bricks to the towers, and the space complexity occurs because we store the unique heights for each combination.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a greedy approach to add bricks to the towers. We should add bricks to the smallest towers first to maximize the total height.
- Detailed breakdown of the approach:
  1. Sort the towers by their heights in ascending order.
  2. Initialize the total height and the number of bricks used.
  3. Iterate through the sorted towers and add bricks to the smallest towers to make them unique.
  4. Update the total height and the number of bricks used.
- Proof of optimality: The greedy approach is optimal because it ensures that the smallest towers are made unique first, which maximizes the total height.

```cpp
int maximizeHeight(vector<int>& heights, int bricks) {
    sort(heights.begin(), heights.end());
    int n = heights.size();
    int total_height = 0;
    for (int i = 0; i < n; i++) {
        if (i > 0 && heights[i] == heights[i - 1]) {
            if (bricks > 0) {
                heights[i]++;
                bricks--;
            } else {
                break;
            }
        }
        total_height += heights[i];
    }
    return total_height;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of towers. This is because we sort the towers by their heights.
> - **Space Complexity:** $O(1)$, where $n$ is the number of towers. This is because we only use a constant amount of space to store the total height and the number of bricks used.
> - **Optimality proof:** The greedy approach is optimal because it ensures that the smallest towers are made unique first, which maximizes the total height.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, sorting.
- Problem-solving patterns identified: Using a greedy approach to optimize a solution.
- Optimization techniques learned: Sorting and iterating through the sorted array to find the optimal solution.
- Similar problems to practice: Other problems that involve optimizing a solution using a greedy approach.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array.
- Edge cases to watch for: Handling cases where the input array is empty or the number of bricks is zero.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the solution with different input arrays and numbers of bricks to ensure that it works correctly.