## Maximum Count of Positive Integer and Negative Integer

**Problem Link:** https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 2000`, `-1000 <= nums[i] <= 1000`.
- Expected output format: The maximum count of positive integers and negative integers in the array.
- Key requirements: Find the maximum count of either positive or negative integers in the array.
- Edge cases: Empty array, array with all zeros, array with all positive or all negative integers.

**Example Test Cases:**
- `nums = [1, 2, 3, 4, 5]`: The maximum count is `5` (all positive integers).
- `nums = [-1, -2, -3, -4, -5]`: The maximum count is `5` (all negative integers).
- `nums = [1, 2, -3, -4, 5]`: The maximum count is `3` (positive integers) or `2` (negative integers).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the number of positive and negative integers in the array separately.
- Step-by-step breakdown: Iterate through the array, incrementing the count of positive or negative integers as encountered.
- Why this approach comes to mind first: It is a straightforward and simple solution.

```cpp
int maximumCount(vector<int>& nums) {
    int positiveCount = 0;
    int negativeCount = 0;
    
    for (int num : nums) {
        if (num > 0) {
            positiveCount++;
        } else if (num < 0) {
            negativeCount++;
        }
    }
    
    return max(positiveCount, negativeCount);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, because we iterate through the array once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the counts.
> - **Why these complexities occur:** The time complexity is linear because we visit each element in the array once, and the space complexity is constant because we use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved in a single pass through the array, keeping track of the counts of positive and negative integers.
- Detailed breakdown: The optimal approach is essentially the same as the brute force approach, as it already has the best possible time complexity for this problem.
- Proof of optimality: Any solution must examine each element in the array at least once to determine if it is positive or negative, so the optimal time complexity is $O(n)$.

```cpp
int maximumCount(vector<int>& nums) {
    int positiveCount = 0;
    int negativeCount = 0;
    
    for (int num : nums) {
        if (num > 0) {
            positiveCount++;
        } else if (num < 0) {
            negativeCount++;
        }
    }
    
    return max(positiveCount, negativeCount);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space.
> - **Optimality proof:** The time complexity is optimal because we must examine each element at least once, and the space complexity is optimal because we use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Single pass through the array.
- Problem-solving pattern: Counting elements based on conditions.
- Optimization technique: Reducing space complexity by using a constant amount of space.

**Mistakes to Avoid:**
- Not considering the case where the array is empty.
- Not handling the case where all integers are zero.
- Not using a single pass through the array, leading to unnecessary complexity.