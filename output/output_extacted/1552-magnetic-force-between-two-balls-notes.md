## Magnetic Force Between Two Balls

**Problem Link:** https://leetcode.com/problems/magnetic-force-between-two-balls/description

**Problem Statement:**
- Input format and constraints: The problem takes in an integer array `position` representing the positions of balls and an integer `m` representing the number of balls to be placed. The goal is to find the maximum possible minimum distance between any two balls.
- Expected output format: The function should return the maximum possible minimum distance.
- Key requirements and edge cases to consider: The input array `position` is sorted, and the number of balls `m` is less than or equal to the number of positions.
- Example test cases with explanations:
  - For `position = [1, 2, 3, 4, 7]` and `m = 3`, the output should be `3` because we can place the balls at positions `1`, `4`, and `7`, resulting in a minimum distance of `3`.
  - For `position = [5, 4, 3, 2, 1, 1000000000]` and `m = 2`, the output should be `999999999` because we can place the balls at positions `1` and `1000000000`, resulting in a minimum distance of `999999999`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible combinations of positions for placing the balls.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of `m` positions from the input array `position`.
  2. For each combination, calculate the minimum distance between any two balls.
  3. Keep track of the maximum minimum distance found across all combinations.
- Why this approach comes to mind first: It is a straightforward approach that ensures we consider all possible scenarios.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxMinDistance(std::vector<int>& position, int m) {
    int n = position.size();
    int maxMinDist = 0;
    
    // Generate all possible combinations of m positions
    std::vector<bool> combination(n, false);
    for (int i = 0; i < m; i++) {
        combination[i] = true;
    }
    
    do {
        int minDist = INT_MAX;
        for (int i = 0; i < n - 1; i++) {
            if (combination[i] && combination[i + 1]) {
                minDist = std::min(minDist, position[i + 1] - position[i]);
            }
        }
        maxMinDist = std::max(maxMinDist, minDist);
    } while (std::prev_permutation(combination.begin(), combination.end()));
    
    return maxMinDist;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\binom{n}{m} \cdot n)$, where $\binom{n}{m}$ represents the number of combinations and $n$ is the number of positions. This is because we generate all possible combinations and calculate the minimum distance for each combination.
> - **Space Complexity:** $O(n)$, where $n$ is the number of positions. This is because we need to store the current combination.
> - **Why these complexities occur:** The time complexity is high due to the generation of all possible combinations, and the space complexity is relatively low since we only need to store the current combination.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a binary search approach to find the maximum possible minimum distance. The idea is to check if it is possible to place `m` balls with a minimum distance of at least `mid`.
- Detailed breakdown of the approach:
  1. Calculate the range of possible minimum distances, which is from `1` to `position[n - 1] - position[0]`.
  2. Perform a binary search within this range to find the maximum possible minimum distance.
  3. For each `mid` value, check if it is possible to place `m` balls with a minimum distance of at least `mid`.
- Proof of optimality: This approach is optimal because it reduces the search space significantly by using binary search.

```cpp
int maxMinDistance(std::vector<int>& position, int m) {
    int n = position.size();
    int left = 1, right = position[n - 1] - position[0];
    
    while (left < right) {
        int mid = left + (right - left + 1) / 2;
        int count = 1, prev = position[0];
        
        for (int i = 1; i < n; i++) {
            if (position[i] - prev >= mid) {
                count++;
                prev = position[i];
            }
        }
        
        if (count >= m) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    
    return left;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log d)$, where $n$ is the number of positions and $d$ is the maximum possible distance between two positions. This is because we perform a binary search and iterate through the positions for each `mid` value.
> - **Space Complexity:** $O(1)$, which means the space complexity is constant. This is because we only use a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it reduces the search space significantly by using binary search, resulting in a significant improvement in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, combinatorial optimization.
- Problem-solving patterns identified: Reducing the search space using binary search.
- Optimization techniques learned: Using binary search to find the maximum possible minimum distance.
- Similar problems to practice: Other problems involving combinatorial optimization and binary search.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the edge cases, such as when `m` is equal to `n`.
- Edge cases to watch for: When `m` is equal to `n`, the maximum possible minimum distance is `0`.
- Performance pitfalls: Using the brute force approach, which has a high time complexity.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure it works correctly.