## Minimum Index of a Valid Split
**Problem Link:** https://leetcode.com/problems/minimum-index-of-a-valid-split/description

**Problem Statement:**
- Input format: `nums`, an array of integers, and `minVal`, an integer representing the minimum sum of a valid split.
- Constraints: $1 \leq \text{length of nums} \leq 10^5$, $0 \leq \text{nums[i]} \leq 10^5$, and $0 \leq \text{minVal} \leq 10^{15}$.
- Expected output format: The minimum index `i` such that `nums[0..i]` and `nums[i+1..n-1]` both have a sum greater than or equal to `minVal`. If no such index exists, return `-1`.
- Key requirements and edge cases to consider:
  - The array `nums` can have duplicate elements.
  - The sum of the elements in `nums` can exceed `minVal`.
  - The minimum index `i` should be the smallest possible index that satisfies the condition.
- Example test cases with explanations:
  - `nums = [1, 2, 3, 4, 5], minVal = 3`, the minimum index is `2` because `1 + 2 = 3` and `3 + 4 + 5 = 12`, both greater than or equal to `minVal`.
  - `nums = [1, 2, 3, 4, 5], minVal = 11`, the minimum index is `3` because `1 + 2 + 3 = 6` and `4 + 5 = 9`, but there is no split that satisfies the condition, so the answer is `-1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible splits of the array `nums` and check if the sum of the left and right parts are both greater than or equal to `minVal`.
- Step-by-step breakdown of the solution:
  1. Initialize the minimum index `i` to `-1`.
  2. Iterate over the array `nums` and for each index `j`, calculate the sum of the left part `leftSum` and the right part `rightSum`.
  3. Check if `leftSum` and `rightSum` are both greater than or equal to `minVal`. If they are, update the minimum index `i` if `j` is smaller than the current `i`.
- Why this approach comes to mind first: It is a straightforward solution that tries all possible splits of the array.

```cpp
int minIndex(vector<int>& nums, int minVal) {
    int n = nums.size();
    long long sum = 0;
    for (int num : nums) sum += num;
    int minIdx = -1;
    for (int i = 0; i < n - 1; i++) {
        long long leftSum = 0;
        for (int j = 0; j <= i; j++) leftSum += nums[j];
        long long rightSum = sum - leftSum;
        if (leftSum >= minVal && rightSum >= minVal) {
            if (minIdx == -1 || i < minIdx) minIdx = i;
        }
    }
    return minIdx;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array `nums`, because we are iterating over the array and for each index, we are calculating the sum of the left and right parts.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the minimum index and the sums.
> - **Why these complexities occur:** The time complexity is quadratic because of the nested loops, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use prefix sums to calculate the sum of the left part in constant time.
- Detailed breakdown of the approach:
  1. Calculate the prefix sums of the array `nums`.
  2. Iterate over the array `nums` and for each index `i`, calculate the sum of the right part using the prefix sums.
  3. Check if the sum of the left part and the sum of the right part are both greater than or equal to `minVal`. If they are, update the minimum index `i` if `i` is smaller than the current minimum index.
- Proof of optimality: This approach is optimal because we are only iterating over the array once and using constant time to calculate the sums.

```cpp
int minIndex(vector<int>& nums, int minVal) {
    int n = nums.size();
    vector<long long> prefixSums(n + 1, 0);
    for (int i = 0; i < n; i++) prefixSums[i + 1] = prefixSums[i] + nums[i];
    int minIdx = -1;
    for (int i = 0; i < n - 1; i++) {
        long long leftSum = prefixSums[i + 1];
        long long rightSum = prefixSums[n] - prefixSums[i + 1];
        if (leftSum >= minVal && rightSum >= minVal) {
            if (minIdx == -1 || i < minIdx) minIdx = i;
        }
    }
    return minIdx;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array `nums`, because we are iterating over the array once to calculate the prefix sums and once to find the minimum index.
> - **Space Complexity:** $O(n)$, because we are using a vector to store the prefix sums.
> - **Optimality proof:** This approach is optimal because we are only iterating over the array once and using constant time to calculate the sums, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: prefix sums, iteration, and conditional statements.
- Problem-solving patterns identified: using prefix sums to calculate sums in constant time.
- Optimization techniques learned: reducing the time complexity by using prefix sums.
- Similar problems to practice: problems that involve calculating sums or finding minimum/maximum indices.

**Mistakes to Avoid:**
- Common implementation errors: not initializing variables, not checking for edge cases, and not using prefix sums to calculate sums.
- Edge cases to watch for: empty arrays, arrays with a single element, and arrays with duplicate elements.
- Performance pitfalls: using nested loops to calculate sums, resulting in a quadratic time complexity.
- Testing considerations: testing the function with different input sizes, input values, and edge cases to ensure it works correctly.