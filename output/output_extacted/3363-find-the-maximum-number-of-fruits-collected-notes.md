## Find the Maximum Number of Fruits Collected

**Problem Link:** https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/description

**Problem Statement:**
- Input format and constraints: Given a `2D` vector `fruits`, where `fruits[i] = [starti, endi]` represents a fruit that is available from `starti` to `endi` (inclusive). The goal is to find the maximum number of fruits that can be collected.
- Expected output format: The maximum number of fruits that can be collected.
- Key requirements and edge cases to consider: The fruits are collected in a specific order, and a fruit can only be collected if the previous fruit has been collected and its end time is less than or equal to the start time of the current fruit.
- Example test cases with explanations:
  - Input: `fruits = [[1,2],[3,2],[9,7],[2,3],[3,7]]`
  - Output: `3`
  - Explanation: The maximum number of fruits that can be collected is `3`, which are the fruits with start and end times `[[1,2],[2,3],[3,7]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible combinations of fruits to find the maximum number that can be collected.
- Step-by-step breakdown of the solution:
  1. Sort the fruits based on their end times.
  2. Initialize a variable `max_fruits` to store the maximum number of fruits that can be collected.
  3. Iterate over all possible combinations of fruits.
  4. For each combination, check if the fruits can be collected in the given order.
  5. Update `max_fruits` if the current combination has more fruits than the previous maximum.
- Why this approach comes to mind first: The brute force approach is often the most straightforward solution, as it involves checking all possible scenarios.

```cpp
#include <vector>
#include <algorithm>

int maxFruits(std::vector<std::vector<int>>& fruits) {
    // Sort the fruits based on their end times
    std::sort(fruits.begin(), fruits.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[1] < b[1];
    });

    int max_fruits = 0;
    int n = fruits.size();

    // Iterate over all possible combinations of fruits
    for (int mask = 0; mask < (1 << n); mask++) {
        int current_fruits = 0;
        int prev_end = -1;

        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                if (fruits[i][0] >= prev_end) {
                    current_fruits++;
                    prev_end = fruits[i][1];
                }
            }
        }

        max_fruits = std::max(max_fruits, current_fruits);
    }

    return max_fruits;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of fruits. This is because we are iterating over all possible combinations of fruits, and for each combination, we are iterating over the fruits to check if they can be collected.
> - **Space Complexity:** $O(n)$, where $n$ is the number of fruits. This is because we are storing the fruits in a vector.
> - **Why these complexities occur:** The time complexity is high because we are using a brute force approach, which involves checking all possible combinations of fruits. The space complexity is relatively low because we are only storing the fruits in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use dynamic programming to store the maximum number of fruits that can be collected up to each fruit.
- Detailed breakdown of the approach:
  1. Sort the fruits based on their end times.
  2. Initialize a vector `dp` to store the maximum number of fruits that can be collected up to each fruit.
  3. Iterate over the fruits, and for each fruit, find the maximum number of fruits that can be collected up to the previous fruit.
  4. Update `dp` with the maximum number of fruits that can be collected up to the current fruit.
- Proof of optimality: The dynamic programming approach ensures that we are considering all possible combinations of fruits, and we are storing the maximum number of fruits that can be collected up to each fruit. This allows us to avoid redundant calculations and reduce the time complexity.

```cpp
int maxFruits(std::vector<std::vector<int>>& fruits) {
    // Sort the fruits based on their end times
    std::sort(fruits.begin(), fruits.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[1] < b[1];
    });

    int n = fruits.size();
    std::vector<int> dp(n, 1);

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (fruits[i][0] >= fruits[j][1]) {
                dp[i] = std::max(dp[i], dp[j] + 1);
            }
        }
    }

    return *std::max_element(dp.begin(), dp.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of fruits. This is because we are iterating over the fruits and for each fruit, we are iterating over the previous fruits to find the maximum number of fruits that can be collected.
> - **Space Complexity:** $O(n)$, where $n$ is the number of fruits. This is because we are storing the maximum number of fruits that can be collected up to each fruit in a vector.
> - **Optimality proof:** The dynamic programming approach ensures that we are considering all possible combinations of fruits, and we are storing the maximum number of fruits that can be collected up to each fruit. This allows us to avoid redundant calculations and reduce the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, sorting, and iteration.
- Problem-solving patterns identified: Using dynamic programming to store the maximum number of fruits that can be collected up to each fruit.
- Optimization techniques learned: Avoiding redundant calculations by storing the maximum number of fruits that can be collected up to each fruit.
- Similar problems to practice: Other dynamic programming problems, such as the `0/1` knapsack problem or the longest increasing subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the fruits based on their end times, or not initializing the `dp` vector correctly.
- Edge cases to watch for: Fruits with the same start and end times, or fruits with negative start and end times.
- Performance pitfalls: Using a brute force approach, which can result in high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.