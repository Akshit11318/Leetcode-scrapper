## Find the Number of K-Even Arrays

**Problem Link:** https://leetcode.com/problems/find-the-number-of-k-even-arrays/description

**Problem Statement:**
- Input: An integer `k` and an array `nums` of integers.
- Constraints: `1 <= k <= 10^5` and `1 <= nums.length <= 10^5`.
- Expected output: The number of subarrays in `nums` that are `k`-even.
- Key requirements: A subarray is `k`-even if the sum of its elements is a multiple of `k`.
- Edge cases: Empty array, single-element array, array with all elements being multiples of `k`, etc.
- Example test cases:
  - Input: `k = 2`, `nums = [1,2,3,4,5]`
    - Output: `8`
    - Explanation: The `k`-even subarrays are `[2]`, `[4]`, `[1,3]`, `[1,3,5]`, `[2,4]`, `[3,5]`, `[2,3,4]`, and `[4,5]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subarray to see if its sum is a multiple of `k`.
- Step-by-step breakdown:
  1. Generate all possible subarrays of `nums`.
  2. For each subarray, calculate its sum.
  3. Check if the sum is a multiple of `k`. If it is, increment the count of `k`-even subarrays.
- Why this approach comes to mind first: It is straightforward and ensures that no `k`-even subarrays are missed.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int sum = 0;
            for (int x = i; x <= j; x++) {
                sum += nums[x];
            }
            if (sum % k == 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`. This is because for each of the $n$ elements, we potentially generate $n$ subarrays, and for each subarray, we calculate its sum, which takes up to $n$ time.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, as we only use a constant amount of space to store the count and the sum.
> - **Why these complexities occur:** The brute force approach is inefficient because it involves nested loops that generate all possible subarrays and then calculate their sums. This leads to a cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all possible subarrays and checking their sums, we can use a prefix sum array to efficiently calculate the sum of any subarray in constant time.
- Detailed breakdown:
  1. Calculate the prefix sum array `prefixSum` where `prefixSum[i]` is the sum of the first `i` elements of `nums`.
  2. Initialize a hashmap `countMap` to store the count of prefix sums modulo `k`.
  3. Iterate through `prefixSum` and for each `prefixSum[i]`, calculate its value modulo `k` and store it in `countMap`.
  4. For each `i`, calculate the number of subarrays ending at `i` that are `k`-even by checking how many times the value `prefixSum[i] % k` appears in `countMap`.
- Proof of optimality: This approach is optimal because it reduces the time complexity to $O(n)$ by avoiding the generation of all possible subarrays and instead using a prefix sum array and a hashmap to efficiently count `k`-even subarrays.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    unordered_map<int, int> countMap;
    countMap[0] = 1; // For the empty subarray
    int count = 0;
    for (int i = 1; i <= n; i++) {
        int remainder = prefixSum[i] % k;
        if (countMap.find(remainder) != countMap.end()) {
            count += countMap[remainder];
        }
        countMap[remainder]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`, as we make a single pass through the array to calculate the prefix sums and then another pass to count the `k`-even subarrays.
> - **Space Complexity:** $O(n)$, as in the worst case, every prefix sum modulo `k` could be unique, leading to a hashmap of size $n$.
> - **Optimality proof:** This approach is optimal because it achieves a linear time complexity, which is the best possible time complexity for this problem given that we must at least read the input array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Prefix sum arrays, hashmaps, and modulo arithmetic.
- Problem-solving patterns: Using prefix sums to efficiently calculate subarray sums and hashmaps to count occurrences of specific values.
- Optimization techniques: Avoiding unnecessary iterations and using data structures to reduce time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty input array, or incorrectly calculating the prefix sums.
- Edge cases to watch for: Empty array, single-element array, array with all elements being multiples of `k`.
- Performance pitfalls: Using a brute force approach that generates all possible subarrays, leading to a high time complexity.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure correctness and efficiency.