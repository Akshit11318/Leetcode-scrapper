## Sum of Consecutive Subarrays
**Problem Link:** https://leetcode.com/problems/sum-of-consecutive-subarrays/description

**Problem Statement:**
- Input format: Given an integer array `nums` and an integer `k`.
- Constraints: `1 <= k <= nums.length <= 1000`, and `1 <= nums[i] <= 1000`.
- Expected output format: An array of integers where the `i-th` integer is the sum of all subarrays of length `k` starting at index `i`.
- Key requirements and edge cases to consider: All elements in the input array are non-negative integers, and `k` is always less than or equal to the length of `nums`.
- Example test cases with explanations:
  - For `nums = [1, 2, 3, 4]` and `k = 2`, the output should be `[3, 5, 7]` because the sums of subarrays of length 2 starting at each index are `1 + 2 = 3`, `2 + 3 = 5`, and `3 + 4 = 7`.
  - For `nums = [1, 2, 3, 4, 5]` and `k = 3`, the output should be `[6, 9, 12]` because the sums of subarrays of length 3 starting at each index are `1 + 2 + 3 = 6`, `2 + 3 + 4 = 9`, and `3 + 4 + 5 = 12`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to iterate over the array and for each starting index, calculate the sum of the subarray of length `k`.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array to store the sums of subarrays.
  2. Iterate over the input array `nums` with a loop that considers each element as a potential starting point for a subarray of length `k`.
  3. For each starting index, calculate the sum of the subarray of length `k` by iterating over the next `k` elements and adding them to a running total.
  4. Append this sum to the result array.
- Why this approach comes to mind first: It directly follows from the problem statement and involves minimal additional concepts beyond basic iteration and summation.

```cpp
vector<int> sumOfConsecutiveSubarrays(vector<int>& nums, int k) {
    vector<int> result;
    for (int i = 0; i <= nums.size() - k; i++) {
        int sum = 0;
        for (int j = i; j < i + k; j++) {
            sum += nums[j];
        }
        result.push_back(sum);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of `nums`, because for each of the $n - k + 1$ starting indices, we perform $k$ additions.
> - **Space Complexity:** $O(n - k + 1)$, because in the worst case, the size of the result array can be $n - k + 1$.
> - **Why these complexities occur:** The brute force approach involves nested loops, with the outer loop iterating over potential starting indices and the inner loop calculating the sum of a subarray of length `k`. This leads to a time complexity that is linear in the size of the input array multiplied by `k`, and a space complexity that is linear in the size of the output array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of recalculating the sum of each subarray from scratch, we can take advantage of the fact that each subarray overlaps with the previous one by `k-1` elements. This means we only need to add the next element and subtract the first element of the previous subarray to get the sum of the current subarray.
- Detailed breakdown of the approach:
  1. Initialize the sum of the first subarray by summing the first `k` elements of `nums`.
  2. Append this sum to the result array.
  3. Iterate over the rest of `nums`, starting from the `k-th` element. For each element at index `i`, calculate the sum of the subarray ending at `i` by adding the current element and subtracting the element that is `k` positions before it.
  4. Append each new sum to the result array.
- Proof of optimality: This approach reduces the number of additions required from $O(n \cdot k)$ to $O(n)$, as we only perform a constant amount of work for each element in `nums`.

```cpp
vector<int> sumOfConsecutiveSubarrays(vector<int>& nums, int k) {
    vector<int> result;
    int windowSum = 0;
    for (int i = 0; i < nums.size(); i++) {
        windowSum += nums[i];
        if (i >= k) {
            windowSum -= nums[i - k];
        }
        if (i >= k - 1) {
            result.push_back(windowSum);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`, because we make a single pass through the input array.
> - **Space Complexity:** $O(n - k + 1)$, because the size of the result array can be up to $n - k + 1$.
> - **Optimality proof:** This is optimal because we only need to process each element in `nums` once to calculate all sums, and we cannot do better than linear time for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique for efficient calculation of overlapping subarray sums.
- Problem-solving patterns identified: Looking for overlap or reuse in calculations to reduce computational complexity.
- Optimization techniques learned: Avoiding redundant calculations by maintaining a running sum and updating it based on changes to the window of consideration.
- Similar problems to practice: Other problems involving arrays and subarrays, such as maximum subarray, minimum window subarray, etc.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty input array or `k` being larger than the array length.
- Edge cases to watch for: Input validation, ensuring `k` is within the bounds of the array length.
- Performance pitfalls: Using brute force approaches for large inputs, leading to inefficient time complexity.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure correctness and performance.