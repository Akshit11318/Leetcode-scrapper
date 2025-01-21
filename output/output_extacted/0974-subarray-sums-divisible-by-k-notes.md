## Subarray Sums Divisible by K
**Problem Link:** [https://leetcode.com/problems/subarray-sums-divisible-by-k/description](https://leetcode.com/problems/subarray-sums-divisible-by-k/description)

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 3 * 10^4`, `1 <= nums[i] <= 10^4`, `2 <= k <= 10^4`.
- Expected Output: The number of subarrays where the sum of the elements is divisible by `k`.
- Key Requirements:
  - Consider all possible subarrays of `nums`.
  - Count the number of subarrays where the sum of the elements is divisible by `k`.
- Example Test Cases:
  - `nums = [4,5,0,-2,-3,1], k = 5`, Output: `7`
  - `nums = [4,5,0,-2,-3,1], k = 10`, Output: `3`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible subarrays and calculate their sums.
- Step-by-step breakdown:
  1. Initialize a counter for the number of subarrays with sums divisible by `k`.
  2. Iterate through all possible start indices for the subarrays.
  3. For each start index, iterate through all possible end indices.
  4. Calculate the sum of the current subarray.
  5. Check if the sum is divisible by `k`. If it is, increment the counter.
- Why this approach comes to mind first: It is straightforward and ensures that all possible subarrays are considered.

```cpp
int subarraysDivByK(vector<int>& nums, int k) {
    int count = 0;
    for (int start = 0; start < nums.size(); start++) {
        int sum = 0;
        for (int end = start; end < nums.size(); end++) {
            sum += nums[end];
            if (sum % k == 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`. This is because we are iterating through all possible subarrays.
> - **Space Complexity:** $O(1)$, excluding the input array. We are only using a constant amount of space to store the counter and the sum of the current subarray.
> - **Why these complexities occur:** The time complexity is quadratic because we are using nested loops to iterate through all possible subarrays. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a hashmap to store the cumulative sums modulo `k` and their frequencies. This allows us to avoid recalculating the sums for each subarray.
- Detailed breakdown:
  1. Initialize a hashmap `cumulativeSums` to store the cumulative sums modulo `k` and their frequencies.
  2. Initialize a variable `cumulativeSum` to store the cumulative sum of the elements.
  3. Initialize a counter `count` to store the number of subarrays with sums divisible by `k`.
  4. Iterate through the elements of `nums`.
  5. For each element, update the `cumulativeSum` by adding the current element.
  6. Check if the `cumulativeSum` modulo `k` is already in the hashmap. If it is, increment the counter by the frequency of the `cumulativeSum` modulo `k`.
  7. Increment the frequency of the `cumulativeSum` modulo `k` in the hashmap.
- Proof of optimality: This approach has a linear time complexity, which is the best possible time complexity for this problem because we must iterate through all elements at least once.

```cpp
int subarraysDivByK(vector<int>& nums, int k) {
    unordered_map<int, int> cumulativeSums;
    cumulativeSums[0] = 1; // Initialize with 0 sum
    int cumulativeSum = 0;
    int count = 0;
    for (int num : nums) {
        cumulativeSum = (cumulativeSum + num) % k;
        if (cumulativeSum < 0) {
            cumulativeSum += k; // Handle negative values
        }
        if (cumulativeSums.find(cumulativeSum) != cumulativeSums.end()) {
            count += cumulativeSums[cumulativeSum];
        }
        cumulativeSums[cumulativeSum]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is because we are iterating through the elements once.
> - **Space Complexity:** $O(k)$, where $k` is the divisor. This is because we are storing the frequencies of the cumulative sums modulo `k` in the hashmap.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and uses a hashmap to avoid recalculating the sums for each subarray.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap to store frequencies, cumulative sums, and modulo operations.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems, using a hashmap to avoid recalculating sums.
- Optimization techniques learned: Using a hashmap to store frequencies, avoiding recalculating sums.
- Similar problems to practice: Problems involving cumulative sums, modulo operations, and hashmaps.

**Mistakes to Avoid:**
- Common implementation errors: Not handling negative values correctly, not initializing the hashmap with the 0 sum.
- Edge cases to watch for: Empty input array, divisor `k` equal to 1.
- Performance pitfalls: Using a brute force approach with quadratic time complexity.
- Testing considerations: Test with different input sizes, divisors, and edge cases.