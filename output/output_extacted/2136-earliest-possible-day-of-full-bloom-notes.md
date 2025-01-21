## Earliest Possible Day of Full Bloom
**Problem Link:** https://leetcode.com/problems/earliest-possible-day-of-full-bloom/description

**Problem Statement:**
- Input format and constraints: Given a `0-indexed` integer array `plantTime` and `growTime`, where `plantTime[i]` is the time it takes to plant the `i-th` flower and `growTime[i]` is the time it takes for the `i-th` flower to grow.
- Expected output format: The minimum number of days needed to make all flowers bloom.
- Key requirements and edge cases to consider: We need to find the optimal order in which to plant the flowers to minimize the total time.
- Example test cases with explanations: For example, if `plantTime = [1, 4, 3]` and `growTime = [2, 5, 1]`, the optimal solution is to plant the flowers in the order of their growth times.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible orders of planting the flowers and calculate the total time for each order.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the flowers.
  2. For each permutation, calculate the total time by summing up the planting time and growth time for each flower.
  3. Keep track of the minimum total time found so far.
- Why this approach comes to mind first: It's a straightforward approach to try all possible solutions and find the optimal one.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int earliestFullBloom(std::vector<int>& plantTime, std::vector<int>& growTime) {
    int n = plantTime.size();
    std::vector<int> indices(n);
    for (int i = 0; i < n; i++) {
        indices[i] = i;
    }
    int minDays = INT_MAX;
    do {
        int days = 0;
        int planted = 0;
        for (int i = 0; i < n; i++) {
            int idx = indices[i];
            planted += plantTime[idx];
            days = std::max(days, planted + growTime[idx]);
        }
        minDays = std::min(minDays, days);
    } while (std::next_permutation(indices.begin(), indices.end()));
    return minDays;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the number of flowers, because we're trying all possible permutations of the flowers.
> - **Space Complexity:** $O(n)$, because we need to store the permutations.
> - **Why these complexities occur:** The brute force approach tries all possible solutions, which leads to an exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Sort the flowers by their growth times in descending order.
- Detailed breakdown of the approach:
  1. Sort the flowers by their growth times in descending order.
  2. Initialize the total time to 0.
  3. For each flower, add its planting time to the total time and update the total time to be the maximum of the current total time and the sum of the planting time and growth time.
- Proof of optimality: By sorting the flowers by their growth times, we ensure that the flowers with the longest growth times are planted first, which minimizes the total time.
- Why further optimization is impossible: This approach has a time complexity of $O(n \log n)$, which is optimal because we need to sort the flowers.

```cpp
int earliestFullBloom(std::vector<int>& plantTime, std::vector<int>& growTime) {
    int n = plantTime.size();
    std::vector<std::pair<int, int>> flowers(n);
    for (int i = 0; i < n; i++) {
        flowers[i] = {growTime[i], plantTime[i]};
    }
    std::sort(flowers.rbegin(), flowers.rend());
    int days = 0;
    int planted = 0;
    for (auto& flower : flowers) {
        planted += flower.second;
        days = std::max(days, planted + flower.first);
    }
    return days;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of flowers, because we're sorting the flowers.
> - **Space Complexity:** $O(n)$, because we need to store the sorted flowers.
> - **Optimality proof:** This approach has the optimal time complexity because we need to sort the flowers to find the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, permutation, and greedy algorithms.
- Problem-solving patterns identified: Finding the optimal order to minimize the total time.
- Optimization techniques learned: Sorting and greedy algorithms.
- Similar problems to practice: Other problems that involve finding the optimal order or schedule.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array.
- Edge cases to watch for: An empty input array, or an array with a single element.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing the function with different input arrays, including edge cases.