## Maximal Score After Applying K Operations
**Problem Link:** https://leetcode.com/problems/maximal-score-after-applying-k-operations/description

**Problem Statement:**
- Input: You are given an array of integers `nums` and an integer `k`.
- Constraints: The array `nums` contains integers in the range `[-10^9, 10^9]`, and `k` is an integer in the range `[1, 10^5]`.
- Expected Output: Find the maximum score that can be obtained by applying at most `k` operations to the array `nums`, where an operation is defined as either adding `1` to all elements in the array or multiplying all elements in the array by `-1`.
- Key Requirements: The goal is to maximize the sum of the array elements after applying at most `k` operations.
- Edge Cases: Consider the cases where `k` is greater than or equal to the length of `nums`, and where `nums` contains negative numbers.

**Example Test Cases:**
- Example 1: `nums = [2, -1, -4, -3, 3], k = 3`. The maximum score is `5`.
- Example 2: `nums = [1, 2, 3, 4, 5], k = 1`. The maximum score is `15`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of adding `1` to all elements and multiplying all elements by `-1` for up to `k` operations.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of operations.
  2. For each combination, apply the operations to a copy of the array `nums`.
  3. Calculate the sum of the array elements after applying the operations.
  4. Keep track of the maximum sum obtained.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxScore(std::vector<int>& nums, int k) {
    int n = nums.size();
    int max_sum = INT_MIN;

    for (int i = 0; i <= k; i++) {
        std::vector<int> temp = nums;
        for (int j = 0; j < i; j++) {
            if (j % 2 == 0) {
                for (int& num : temp) num++;
            } else {
                for (int& num : temp) num = -num;
            }
        }
        int sum = 0;
        for (int num : temp) sum += num;
        max_sum = std::max(max_sum, sum);
    }

    return max_sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^k \cdot n)$, where $n$ is the length of `nums`. This is because we generate all possible combinations of operations and apply them to the array.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we create a copy of the array for each combination of operations.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of operations, which leads to exponential time complexity. The space complexity is linear because we only need to store a copy of the array for each combination.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a greedy approach to maximize the sum of the array elements. The idea is to always add `1` to all elements if there are more negative numbers in the array, and multiply all elements by `-1` otherwise.
- Detailed breakdown of the approach:
  1. Count the number of negative numbers in the array.
  2. If there are more negative numbers than non-negative numbers, add `1` to all elements.
  3. Otherwise, multiply all elements by `-1`.
  4. Repeat steps 1-3 until we have applied `k` operations or the array no longer contains negative numbers.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxScore(std::vector<int>& nums, int k) {
    int n = nums.size();
    int max_sum = 0;
    int neg_count = 0;

    for (int num : nums) {
        if (num < 0) neg_count++;
        max_sum += num;
    }

    for (int i = 0; i < k; i++) {
        if (neg_count > 0) {
            for (int& num : nums) num++;
            max_sum += n;
            neg_count = 0;
            for (int num : nums) {
                if (num < 0) neg_count++;
            }
        } else {
            for (int& num : nums) num = -num;
            neg_count = n;
        }
    }

    return max_sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of `nums`. This is because we iterate over the array for each operation.
> - **Space Complexity:** $O(1)$, where $n$ is the length of `nums`. This is because we only need a constant amount of space to store the count of negative numbers and the maximum sum.
> - **Optimality proof:** The greedy approach ensures that we always maximize the sum of the array elements by adding `1` to all elements when there are more negative numbers and multiplying all elements by `-1` otherwise.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, counting negative numbers.
- Problem-solving patterns identified: Using a greedy approach to maximize the sum of array elements.
- Optimization techniques learned: Avoiding unnecessary operations by counting negative numbers.
- Similar problems to practice: Other problems involving maximizing or minimizing a quantity using a greedy approach.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases where `k` is greater than or equal to the length of `nums`.
- Edge cases to watch for: Arrays containing only non-negative numbers or only negative numbers.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of operations.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.