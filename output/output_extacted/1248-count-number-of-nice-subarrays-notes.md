## Count Number of Nice Subarrays

**Problem Link:** https://leetcode.com/problems/count-number-of-nice-subarrays/description

**Problem Statement:**
- Input format: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^9`, `0 <= k <= 10^5`.
- Expected output format: The number of nice subarrays.
- Key requirements and edge cases to consider:
  - A nice subarray is defined as a subarray where the number of odd elements is exactly `k`.
  - Handle edge cases where `k` is 0 or equal to the length of `nums`.
- Example test cases with explanations:
  - `nums = [1,1,2,1,1], k = 3`, the output should be `2`.
  - `nums = [2,4,6], k = 1`, the output should be `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all possible subarrays and count the number of odd elements in each subarray.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of `nums`.
  2. For each subarray, count the number of odd elements.
  3. If the count of odd elements is exactly `k`, increment the count of nice subarrays.
- Why this approach comes to mind first: It is straightforward and directly addresses the problem statement.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int oddCount = 0;
            for (int l = i; l <= j; l++) {
                if (nums[l] % 2 != 0) {
                    oddCount++;
                }
            }
            if (oddCount == k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`. This is because we have three nested loops: one for the start of the subarray, one for the end of the subarray, and one to count the odd elements within the subarray.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count of nice subarrays and the count of odd elements in the current subarray.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible subarrays and then counts the odd elements in each, resulting in a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a prefix sum approach to count the number of odd elements up to each index in the array, and then use a hashmap to store the frequency of each prefix sum.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum of odd elements for the entire array.
  2. Use a hashmap to store the frequency of each prefix sum.
  3. Iterate through the array, and for each index, calculate the number of odd elements up to that index.
  4. Use the hashmap to find the number of subarrays that have exactly `k` odd elements ending at the current index.
- Proof of optimality: This approach is optimal because it avoids generating all possible subarrays and instead uses a prefix sum and hashmap to efficiently count the number of nice subarrays.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int count = 0;
    int n = nums.size();
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + (nums[i] % 2 != 0);
    }
    unordered_map<int, int> freq;
    freq[0] = 1;
    for (int i = 1; i <= n; i++) {
        count += freq[prefixSum[i] - k];
        freq[prefixSum[i]]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we make a single pass through the array to calculate the prefix sum and then another pass to count the number of nice subarrays.
> - **Space Complexity:** $O(n)$, as we use a hashmap to store the frequency of each prefix sum.
> - **Optimality proof:** This approach is optimal because it uses a prefix sum and hashmap to efficiently count the number of nice subarrays, avoiding the need to generate all possible subarrays.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum, hashmap, and efficient counting of subarrays.
- Problem-solving patterns identified: Using a prefix sum to efficiently count the number of odd elements in subarrays.
- Optimization techniques learned: Avoiding brute force approaches and using data structures like hashmaps to improve efficiency.
- Similar problems to practice: Other problems involving counting subarrays or using prefix sums.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the prefix sum or using an incorrect data structure.
- Edge cases to watch for: Handling cases where `k` is 0 or equal to the length of `nums`.
- Performance pitfalls: Using a brute force approach or inefficient data structures.
- Testing considerations: Thoroughly testing the solution with different input cases and edge cases.