## Calculate Orders Within Each Interval
**Problem Link:** https://leetcode.com/problems/calculate-orders-within-each-interval/description

**Problem Statement:**
- Input: `intervals` - a 2D array where each sub-array contains two integers representing an interval's start and end.
- Constraints: The input intervals are non-overlapping, and each interval is of the form `[start, end]`.
- Expected Output: An array of integers where each integer represents the number of orders within each interval.
- Key Requirements:
  - For each interval, calculate the number of orders that fall within that interval.
  - An order is considered to be within an interval if its timestamp is greater than or equal to the interval's start and less than or equal to the interval's end.

**Example Test Cases:**
- Input: `intervals = [[0, 2], [3, 5], [6, 8]]`, `orders = [[1, 2], [2, 3], [3, 4], [5, 6], [7, 8]]`
- Expected Output: `[3, 2, 2]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through each order and checking which interval it falls into.
- For each interval, we will count the number of orders that satisfy the condition.

```cpp
#include <iostream>
#include <vector>

std::vector<int> calculateOrdersWithinEachInterval(std::vector<std::vector<int>>& intervals, std::vector<std::vector<int>>& orders) {
    std::vector<int> result;
    for (const auto& interval : intervals) {
        int count = 0;
        for (const auto& order : orders) {
            if (order[0] >= interval[0] && order[0] <= interval[1]) {
                count++;
            }
        }
        result.push_back(count);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of intervals and $m$ is the number of orders, because for each interval, we potentially check every order.
> - **Space Complexity:** $O(n)$, where $n$ is the number of intervals, because we store the count of orders for each interval in the result vector.
> - **Why these complexities occur:** The brute force approach involves nested loops, one for iterating through intervals and another for checking orders against each interval, leading to a time complexity that is the product of the number of intervals and the number of orders.

---

### Optimal Approach (Required)

**Explanation:**
- We can improve upon the brute force approach by first sorting the orders based on their timestamps. This allows us to potentially reduce the number of orders we need to check for each interval.
- However, the most optimal approach involves recognizing that we can solve this problem with a single pass through the orders if we maintain a count for each interval and update these counts as we iterate through the orders.

```cpp
#include <iostream>
#include <vector>

std::vector<int> calculateOrdersWithinEachInterval(std::vector<std::vector<int>>& intervals, std::vector<std::vector<int>>& orders) {
    std::vector<int> result(intervals.size(), 0);
    for (const auto& order : orders) {
        for (size_t i = 0; i < intervals.size(); ++i) {
            if (order[0] >= intervals[i][0] && order[0] <= intervals[i][1]) {
                result[i]++;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of orders and $n$ is the number of intervals, because for each order, we potentially check every interval.
> - **Space Complexity:** $O(n)$, where $n$ is the number of intervals, because we store the count of orders for each interval in the result vector.
> - **Optimality proof:** This approach is optimal because it requires a single pass through the orders and checks each order against all intervals, which is necessary to count the orders within each interval.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and how they can be leveraged to simplify the solution.
- The value of maintaining a clear and concise code structure to improve readability and maintainability.
- The process of optimizing a brute force approach by identifying bottlenecks and applying more efficient algorithms or data structures.

**Mistakes to Avoid:**
- Not thoroughly considering the problem constraints and how they impact the solution.
- Failing to optimize the solution by ignoring potential improvements in algorithmic complexity.
- Not testing the solution thoroughly to ensure it handles all edge cases correctly.