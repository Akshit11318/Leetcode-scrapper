## Maximum Number of Robots Within Budget
**Problem Link:** https://leetcode.com/problems/maximum-number-of-robots-within-budget/description

**Problem Statement:**
- Input format and constraints: You are given two integer arrays, `cost` and `runtime`, where `cost[i]` is the cost to purchase the `i-th` robot, and `runtime[i]` is the time it takes for the `i-th` robot to complete its work. You are also given two integers, `budget` and `start`, representing the maximum budget you can spend and the start time, respectively. The goal is to find the maximum number of robots you can purchase and use within the given budget and time constraints.
- Expected output format: The function should return an integer representing the maximum number of robots that can be purchased and used within the given budget and time constraints.
- Key requirements and edge cases to consider: The problem requires considering the trade-off between the cost of purchasing a robot and the time it takes to complete its work. The function should handle edge cases such as when the budget is insufficient to purchase any robots or when the start time is too late to complete any work.
- Example test cases with explanations:
  - Example 1: `cost = [2, 3], runtime = [2, 3], budget = 5, start = 0`. The function should return `1` because the maximum number of robots that can be purchased and used within the budget is `1`.
  - Example 2: `cost = [3, 5, 6, 4], runtime = [2, 2, 3, 2], budget = 6, start = 1`. The function should return `2` because the maximum number of robots that can be purchased and used within the budget is `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over all possible combinations of robots and checking if the total cost is within the budget and if the total time is sufficient to complete the work.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `max_robots` to `0`.
  2. Iterate over all possible combinations of robots using a nested loop.
  3. For each combination, calculate the total cost and the total time required to complete the work.
  4. If the total cost is within the budget and the total time is sufficient to complete the work, update `max_robots` with the current combination size.
- Why this approach comes to mind first: The brute force approach is often the first approach that comes to mind because it involves a straightforward iteration over all possible combinations.

```cpp
#include <vector>
#include <algorithm>

int maxRobots(std::vector<int>& cost, std::vector<int>& runtime, int budget, int start) {
    int max_robots = 0;
    int n = cost.size();
    for (int i = 0; i < (1 << n); i++) {
        int total_cost = 0;
        int total_time = 0;
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                total_cost += cost[j];
                total_time += runtime[j];
            }
        }
        if (total_cost <= budget && total_time >= start) {
            max_robots = std::max(max_robots, __builtin_popcount(i));
        }
    }
    return max_robots;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of robots. The reason is that we iterate over all possible combinations of robots using a nested loop, and for each combination, we calculate the total cost and the total time required to complete the work.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables `max_robots`, `total_cost`, and `total_time`.
> - **Why these complexities occur:** The time complexity occurs because we iterate over all possible combinations of robots, and the space complexity occurs because we only use a constant amount of space to store the variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a sliding window approach to find the maximum number of robots that can be purchased and used within the given budget and time constraints.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to `0`.
  2. Initialize a variable `max_robots` to `0`.
  3. Initialize a variable `total_cost` to `0`.
  4. Iterate over the `cost` array using the `right` pointer.
  5. For each robot, add its cost to `total_cost`.
  6. If `total_cost` exceeds the budget, move the `left` pointer to the right until `total_cost` is within the budget.
  7. Update `max_robots` with the current window size.
- Proof of optimality: The sliding window approach is optimal because it ensures that we consider all possible combinations of robots and find the maximum number of robots that can be purchased and used within the given budget and time constraints.

```cpp
#include <vector>
#include <algorithm>

int maxRobots(std::vector<int>& cost, std::vector<int>& runtime, int budget, int start) {
    int max_robots = 0;
    int n = cost.size();
    for (int i = 0; i < n; i++) {
        int total_cost = 0;
        int total_time = 0;
        for (int j = i; j < n; j++) {
            total_cost += cost[j];
            total_time += runtime[j];
            if (total_cost <= budget && total_time >= start) {
                max_robots = std::max(max_robots, j - i + 1);
            }
        }
    }
    return max_robots;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of robots. The reason is that we iterate over the `cost` array using a nested loop.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables `max_robots`, `total_cost`, and `total_time`.
> - **Optimality proof:** The sliding window approach is optimal because it ensures that we consider all possible combinations of robots and find the maximum number of robots that can be purchased and used within the given budget and time constraints.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of the sliding window approach to find the maximum number of robots that can be purchased and used within the given budget and time constraints.
- Problem-solving patterns identified: The problem identifies the pattern of using a sliding window approach to solve problems that involve finding the maximum number of elements that can be selected within a given constraint.
- Optimization techniques learned: The problem teaches the optimization technique of using a sliding window approach to reduce the time complexity of the solution.
- Similar problems to practice: Similar problems to practice include finding the maximum number of elements that can be selected within a given constraint, such as the maximum number of tasks that can be completed within a given time limit.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to update the `max_robots` variable with the current window size.
- Edge cases to watch for: An edge case to watch for is when the budget is insufficient to purchase any robots or when the start time is too late to complete any work.
- Performance pitfalls: A performance pitfall is to use a brute force approach that has a high time complexity.
- Testing considerations: A testing consideration is to test the solution with different input values to ensure that it works correctly in all cases.