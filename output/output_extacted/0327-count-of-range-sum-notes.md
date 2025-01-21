## Count of Range Sum
**Problem Link:** https://leetcode.com/problems/count-of-range-sum/description

**Problem Statement:**
- Input: An integer array `nums` and two integers `lower` and `upper`.
- Constraints: `0 <= nums.length <= 2 * 10^4`, `-10^9 <= nums[i] <= 10^9`, and `lower <= upper`.
- Expected Output: The number of pairs of indices `(i, j)` such that `i < j` and `lower <= sum(nums[i..j]) <= upper`.
- Key Requirements: Efficiently count the number of subarrays with sums within a given range.
- Edge Cases: Empty array, single-element array, and arrays with all elements being zero.

**Example Test Cases:**
- Example 1: `nums = [-2, 5, -1]`, `lower = -2`, `upper = 2`. The subarray sums are `[-2, 3, 2]`, so the count is `3`.
- Example 2: `nums = [0]`, `lower = 0`, `upper = 0`. The subarray sum is `[0]`, so the count is `1`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to calculate the sum of every possible subarray and check if it falls within the given range.
- This approach involves iterating over the array to generate all possible subarrays, calculating their sums, and counting those that satisfy the condition.

```cpp
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            long long sum = 0;
            for (int j = i; j < nums.size(); j++) {
                sum += nums[j];
                if (sum >= lower && sum <= upper) {
                    count++;
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array, because we are generating all possible subarrays.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, as we only use a constant amount of space to store the sum and count.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space usage is due to only using a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a `multiset` (or a similar data structure like a balanced binary search tree) to store the cumulative sums encountered so far.
- We iterate through the array, maintaining a cumulative sum, and for each cumulative sum, we check how many previous cumulative sums would result in a range sum within the given bounds when subtracted from the current cumulative sum.
- This approach efficiently utilizes the properties of cumulative sums and the data structure to reduce the time complexity significantly.

```cpp
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        long long sum = 0;
        int count = 0;
        multiset<long long> sums;
        sums.insert(0); // To handle the case where the sum of the first few elements is within the range
        
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            count += distance(sums.lower_bound(sum - upper), sums.upper_bound(sum - lower));
            sums.insert(sum);
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the size of the input array, because we are inserting into and searching a `multiset`.
> - **Space Complexity:** $O(n)$, as we are storing all cumulative sums in the `multiset`.
> - **Optimality proof:** This approach is optimal because it reduces the problem to a series of range queries on a set of cumulative sums, which can be efficiently handled by a `multiset`. Further optimization is not possible without a more efficient data structure or algorithm for range queries.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Cumulative sums, range queries, and the use of a `multiset` for efficient range queries.
- Problem-solving patterns identified: Breaking down the problem into smaller, manageable parts (cumulative sums and range queries).
- Optimization techniques learned: Utilizing the properties of data structures like `multiset` to reduce time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases (like an empty array or an array with a single element), and not considering the initial cumulative sum of 0.
- Edge cases to watch for: Arrays with all elements being zero, and arrays where the sum of the first few elements is within the given range.
- Performance pitfalls: Using a data structure that does not support efficient range queries, leading to higher time complexity.