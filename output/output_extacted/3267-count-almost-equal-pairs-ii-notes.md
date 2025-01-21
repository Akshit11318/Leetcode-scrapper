## Count Almost Equal Pairs II

**Problem Link:** https://leetcode.com/problems/count-almost-equal-pairs-ii/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^9`, `1 <= k <= 10^9`.
- Expected output format: The number of pairs of indices `(i, j)` where `0 <= i < j < nums.length` and `abs(nums[i] - nums[j]) <= k`.
- Key requirements and edge cases to consider: Handling large inputs, avoiding unnecessary computations.
- Example test cases with explanations:
  - For `nums = [1, 2, 3, 4]` and `k = 1`, the output should be `3`, because the pairs `(1, 2)`, `(2, 3)`, and `(3, 4)` satisfy the condition.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each pair of elements in the array.
- Step-by-step breakdown of the solution:
  1. Iterate over the array with two nested loops to consider each pair of indices `(i, j)`.
  2. For each pair, calculate the absolute difference `abs(nums[i] - nums[j])`.
  3. If the absolute difference is less than or equal to `k`, increment the count of almost equal pairs.
- Why this approach comes to mind first: It directly follows from the problem statement, checking each pair to see if it meets the given condition.

```cpp
int countAlmostEquallyPairs(vector<int>& nums, int k) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (abs(nums[i] - nums[j]) <= k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`, because we are comparing each pair of elements in the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, because we are using a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it involves comparing each pair of elements in the array, resulting in quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a data structure that allows for efficient counting of elements within a certain range, such as a hash map or a balanced binary search tree. However, given the specific constraints of this problem, a simpler approach can be derived by observing that the condition `abs(nums[i] - nums[j]) <= k` can be transformed into checking if `nums[j]` falls within the range `[nums[i] - k, nums[i] + k]`.
- Detailed breakdown of the approach:
  1. Sort the array `nums`.
  2. For each element `nums[i]`, find the range of elements that satisfy `abs(nums[i] - nums[j]) <= k` by using binary search to find the first element greater than `nums[i] + k` and the last element less than `nums[i] - k`.
  3. Calculate the number of elements in this range, which represents the number of almost equal pairs for `nums[i]`.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(n^2)$ to $O(n \log n)$ due to the sorting and binary search operations.

```cpp
int countAlmostEquallyPairs(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        int left = lower_bound(nums.begin() + i + 1, nums.end(), nums[i] - k) - nums.begin();
        int right = upper_bound(nums.begin() + i + 1, nums.end(), nums[i] + k) - nums.begin();
        count += right - left;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of `nums`, due to the sorting and binary search operations.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, because we are using a constant amount of space to store the count and indices.
> - **Optimality proof:** This approach is optimal because it minimizes the number of comparisons needed to find almost equal pairs by leveraging the sorted order of the array and efficient range queries via binary search.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, binary search, and range queries.
- Problem-solving patterns identified: Transforming conditions into range queries and leveraging data structures for efficient computation.
- Optimization techniques learned: Reducing time complexity by using more efficient algorithms and data structures.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing binary search or range queries.
- Edge cases to watch for: Handling duplicate elements and ensuring correct indexing.
- Performance pitfalls: Failing to optimize the algorithm for large inputs, leading to high time complexity.
- Testing considerations: Thoroughly testing the implementation with various inputs, including edge cases.