## Count Integers in Intervals

**Problem Link:** https://leetcode.com/problems/count-integers-in-intervals/description

**Problem Statement:**
- Input format and constraints: The problem takes in a 2D array `intervals` where each sub-array represents an interval `[start, end]` and an integer `right`. The goal is to count the number of integers in the range `[1, right]` that are covered by at least one of the given intervals.
- Expected output format: The function should return the count of integers in the range `[1, right]` that fall within at least one interval.
- Key requirements and edge cases to consider:
  - The intervals are non-empty and non-overlapping.
  - The intervals are sorted by their start values.
  - `1 <= intervals.length <= 10^5`
  - `1 <= intervals[i][0] <= intervals[i][1] <= 10^9`
  - `1 <= right <= 10^9`
- Example test cases with explanations:
  - Given `intervals = [[1,2],[3,7],[8,14]]` and `right = 14`, the function should return `10` because the integers in the range `[1, 14]` that fall within at least one interval are `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`, which are `14` integers, but since `[1, 2]` covers `2` numbers and `[3, 7]` covers `5` numbers, and `[8, 14]` covers `7` numbers, and all numbers are covered, the answer is `14 - (1 - 1) = 14`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to iterate through each integer in the range `[1, right]` and check if it falls within any of the given intervals.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `count` to keep track of the number of integers that fall within at least one interval.
  2. Iterate through each integer `i` in the range `[1, right]`.
  3. For each integer `i`, iterate through each interval and check if `i` falls within that interval.
  4. If `i` falls within any interval, increment `count`.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem, as it directly checks each integer against all intervals.

```cpp
class Solution {
public:
    int countIntegersInIntervals(vector<vector<int>>& intervals, int right) {
        int count = 0;
        for (int i = 1; i <= right; i++) {
            for (auto& interval : intervals) {
                if (i >= interval[0] && i <= interval[1]) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of integers in the range `[1, right]` and $m$ is the number of intervals. This is because for each integer, we potentially check all intervals.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the count and loop variables.
> - **Why these complexities occur:** The time complexity is high because we're checking each integer against all intervals, and the space complexity is low because we're not using any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the intervals are non-overlapping and sorted by their start values, we can calculate the total count of integers covered by all intervals directly without needing to iterate through each integer in the range `[1, right]`.
- Detailed breakdown of the approach:
  1. Initialize a variable `count` to keep track of the total count of integers covered by all intervals.
  2. Iterate through each interval.
  3. For each interval, calculate the number of integers it covers within the range `[1, right]`. This can be done by taking the minimum of the interval's end and `right`, and subtracting the interval's start, then adding 1.
  4. Add the count of integers covered by the current interval to the total count.
- Proof of optimality: This approach is optimal because it only requires iterating through the intervals once, resulting in a significant reduction in time complexity compared to the brute force approach.

```cpp
class Solution {
public:
    int countIntegersInIntervals(vector<vector<int>>& intervals, int right) {
        int count = 0;
        for (auto& interval : intervals) {
            count += min(right, interval[1]) - interval[0] + 1;
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$ where $m$ is the number of intervals. This is because we only iterate through the intervals once.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the count and loop variables.
> - **Optimality proof:** This is the optimal solution because we've reduced the time complexity to linear with respect to the number of intervals, which is the minimum required to process each interval at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and basic arithmetic operations.
- Problem-solving patterns identified: The importance of understanding the constraints of the problem (e.g., non-overlapping and sorted intervals) to find an efficient solution.
- Optimization techniques learned: Reducing the number of iterations and avoiding unnecessary checks.
- Similar problems to practice: Other problems involving intervals, such as finding overlapping intervals or merging intervals.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize variables, incorrect loop conditions, and off-by-one errors.
- Edge cases to watch for: Handling intervals with the same start and end values, and intervals that extend beyond the range `[1, right]`.
- Performance pitfalls: Using inefficient algorithms that result in high time complexities.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases and large inputs to ensure correctness and efficiency.