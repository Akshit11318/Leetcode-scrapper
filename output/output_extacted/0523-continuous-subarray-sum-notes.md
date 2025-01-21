## Continuous Subarray Sum
**Problem Link:** https://leetcode.com/problems/continuous-subarray-sum/description

**Problem Statement:**
- Given an integer array `nums` and an integer `k`, return `true` if there is a continuous subarray of `nums` whose sum is a multiple of `k`, otherwise return `false`.
- The input array `nums` contains integers, both positive and negative, and the integer `k` is non-zero.
- The expected output is a boolean value indicating whether such a subarray exists.
- Key requirements include handling arrays of varying lengths and dealing with both positive and negative integers, as well as edge cases where `k` is very large or the array is empty.
- Example test cases include arrays with obvious subarrays that sum to multiples of `k`, arrays without such subarrays, and edge cases like empty arrays or `k` being 1.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subarray to see if its sum is a multiple of `k`.
- Step-by-step, this involves iterating over the array to generate all possible subarrays, calculating the sum of each, and checking if this sum is divisible by `k`.
- This approach comes to mind first because it directly addresses the problem statement without requiring complex optimizations.

```cpp
bool checkSubarraySum(vector<int>& nums, int k) {
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += nums[j];
            if (sum % k == 0 && j - i + 1 > 0) {
                return true;
            }
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each element, we potentially iterate over the rest of the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the sum and indices.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space usage is due to only using a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a prefix sum array and a hashmap to store the prefix sums modulo `k`. This way, if we encounter the same remainder again, it means the sum of the subarray between these two points is a multiple of `k`.
- Detailed breakdown: Initialize a hashmap with a default value for the sum 0 at index -1 (to handle the case where the sum of the entire array is a multiple of `k`). Then, iterate over the array, calculating the prefix sum modulo `k` at each step. If this remainder is already in the hashmap and the distance between the current index and the stored index is greater than 1, return true.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array, reducing the time complexity significantly compared to the brute force approach.

```cpp
bool checkSubarraySum(vector<int>& nums, int k) {
    unordered_map<int, int> prefixSum;
    prefixSum[0] = -1; // For handling the case where the sum of the entire array is a multiple of k
    int currentSum = 0;
    for (int i = 0; i < nums.size(); i++) {
        currentSum = (currentSum + nums[i]) % k;
        if (currentSum == 0 && i > 0) return true; // Sum of subarray from start to current index is a multiple of k
        if (prefixSum.find(currentSum) != prefixSum.end() && i - prefixSum[currentSum] > 1) {
            return true; // Found a subarray whose sum is a multiple of k
        }
        if (prefixSum.find(currentSum) == prefixSum.end()) {
            prefixSum[currentSum] = i;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every prefix sum in the hashmap.
> - **Optimality proof:** This is optimal because we cannot do better than a single pass through the data for this kind of problem, given that we must consider all elements.

---

### Final Notes

**Learning Points:**
- The importance of prefix sums in solving subarray problems efficiently.
- How to use hashmaps to store and quickly look up prefix sums modulo a given number.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Not considering edge cases, such as an empty array or `k` being 1.
- Failing to initialize the hashmap correctly to handle the sum of the entire array being a multiple of `k`.
- Not checking the distance between the current index and the stored index to ensure the subarray has more than one element.