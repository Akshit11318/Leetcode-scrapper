## Increasing Triplet Subsequence

**Problem Link:** https://leetcode.com/problems/increasing-triplet-subsequence/description

**Problem Statement:**
- Input: An integer array `nums`.
- Output: `true` if there exists an increasing triplet subsequence, `false` otherwise.
- Key requirements: A triplet subsequence means three elements `a`, `b`, and `c` in the array such that `a < b < c` and `a`, `b`, and `c` are not necessarily adjacent.
- Example test cases:
  - Input: `nums = [1,2,3]`, Output: `true`
  - Input: `nums = [1,2,1,2,3]`, Output: `true`
  - Input: `nums = [1,1,1]`, Output: `false`

---

### Brute Force Approach

**Explanation:**
- The first approach that comes to mind is to check every possible triplet in the array to see if it forms an increasing sequence.
- This involves using three nested loops to generate all possible triplets and then checking if the elements of each triplet are in ascending order.
- This approach is straightforward but inefficient due to its high time complexity.

```cpp
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] < nums[j] && nums[j] < nums[k]) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the input array. This is because we are using three nested loops, each of which can iterate up to $n$ times.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The brute force approach is inherently inefficient because it checks every possible combination of elements, leading to a cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight here is to maintain two variables, `first` and `second`, which represent the smallest and second smallest numbers we have seen so far that could potentially be part of an increasing triplet.
- We initialize `first` and `second` with `INT_MAX` to ensure that any number in the array will be smaller.
- As we iterate through the array, if we find a number smaller than `first`, we update `first`. If we find a number greater than `first` but smaller than `second`, we update `second`. If we find a number greater than `second`, we have found an increasing triplet, so we return `true`.
- This approach is optimal because it only requires a single pass through the array.

```cpp
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first = INT_MAX, second = INT_MAX;
        for (int num : nums) {
            if (num <= first) {
                first = num;
            } else if (num <= second) {
                second = num;
            } else {
                return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we are making a single pass through the array.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store `first` and `second`.
> - **Optimality proof:** This is the optimal solution because we are only iterating through the array once and using a constant amount of extra space, making it as efficient as possible for this problem.

---

### Final Notes

**Learning Points:**
- The importance of maintaining a small set of variables to track the state of the problem.
- How to optimize a brute force solution by reducing the number of iterations and comparisons needed.
- The concept of using a single pass through the data to achieve optimal time complexity.

**Mistakes to Avoid:**
- Not considering the potential for early returns to simplify the logic and improve performance.
- Overcomplicating the solution by introducing unnecessary variables or data structures.
- Failing to recognize when a problem can be solved with a simple, linear pass through the data.