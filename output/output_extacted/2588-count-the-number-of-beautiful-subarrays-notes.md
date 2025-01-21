## Count the Number of Beautiful Subarrays
**Problem Link:** https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/description

**Problem Statement:**
- Input format: Given an array `nums` of size `n` and an integer `k`.
- Constraints: `1 <= n <= 10^5`, `1 <= k <= n`.
- Expected output format: The number of beautiful subarrays, where a beautiful subarray is defined as a subarray where the number of `1`s is equal to `k`.
- Key requirements and edge cases to consider: Handling edge cases where `k` is larger than the number of `1`s in the array or when `n` is very large.
- Example test cases with explanations: 
  - For `nums = [1, 1, 1, 0]` and `k = 2`, the output should be `2` because there are two beautiful subarrays: `[1, 1]` and `[1, 1]`.
  - For `nums = [0, 0, 0, 0]` and `k = 1`, the output should be `0` because there are no beautiful subarrays.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through all possible subarrays of `nums` and count the number of `1`s in each subarray.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays.
  2. For each subarray, count the number of `1`s.
  3. If the count of `1`s equals `k`, increment the count of beautiful subarrays.
- Why this approach comes to mind first: It's a straightforward method that checks every possible subarray.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int ones = 0;
            for (int l = i; l <= j; l++) {
                if (nums[l] == 1) ones++;
            }
            if (ones == k) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ because for each of the $n$ elements, we are potentially generating $n$ subarrays and then counting the `1`s in each, which takes $n$ time in the worst case.
> - **Space Complexity:** $O(1)$ because we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The nested loops and the counting operation within the innermost loop lead to the cubic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of counting `1`s in each subarray from scratch, we can use a prefix sum approach to keep track of the cumulative sum of `1`s up to each index.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum of `1`s in the array.
  2. Use two pointers to define the subarray and calculate the number of `1`s within it using the prefix sums.
- Proof of optimality: This approach avoids redundant counting of `1`s in subarrays, reducing the time complexity significantly.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int n = nums.size();
    int count = 0;
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int ones = prefixSum[j + 1] - prefixSum[i];
            if (ones == k) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because we have two nested loops, each running up to $n$ times, but we've eliminated the innermost counting loop.
> - **Space Complexity:** $O(n)$ for the prefix sum array.
> - **Optimality proof:** This is optimal because we must consider all possible subarrays to count beautiful ones, and the prefix sum approach minimizes the work done for each subarray.

---

### Alternative Approach
**Explanation:**
- Different perspective or technique: Using a hashmap to store the cumulative sum of `1`s and its frequency. This approach is particularly useful for problems involving sums or differences of elements within subarrays.
- Unique trade-offs: It offers a more efficient solution for certain types of subarray problems but may be overkill for simpler scenarios.
- Scenarios where this approach might be preferred: When dealing with large arrays and the requirement is to find subarrays with specific sum properties, not just counts of `1`s.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int count = 0;
    unordered_map<int, int> sumCount;
    sumCount[0] = 1; // For sum 0, we have one subarray (empty) initially
    int currentSum = 0;
    for (int num : nums) {
        currentSum += num;
        if (sumCount.find(currentSum - k) != sumCount.end()) {
            count += sumCount[currentSum - k];
        }
        sumCount[currentSum]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we make one pass through the array, and hashmap operations are constant time on average.
> - **Space Complexity:** $O(n)$ for the hashmap in the worst case, where every cumulative sum is unique.
> - **Trade-off analysis:** This approach offers the best time complexity but requires more space and might be more complex to understand and implement correctly for those unfamiliar with hashmap-based solutions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sums, hashmap usage for efficient counting, and the importance of avoiding redundant calculations.
- Problem-solving patterns identified: Breaking down problems into smaller, more manageable parts, and recognizing opportunities for optimization.
- Optimization techniques learned: Using prefix sums to avoid redundant counting and employing hashmaps for efficient lookup and counting.
- Similar problems to practice: Other subarray problems involving sums, counts, or specific properties.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, forgetting to initialize variables, and not handling edge cases properly.
- Edge cases to watch for: Empty arrays, arrays with a single element, and cases where `k` is larger than the number of `1`s.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexities.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure the solution works correctly under all scenarios.