## Binary Subarrays With Sum

**Problem Link:** https://leetcode.com/problems/binary-subarrays-with-sum/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `target`.
- Constraints: `2 <= nums.length <= 10^5`, `1 <= target <= 10^6`.
- Expected output format: The number of binary subarrays with sum equal to `target`.
- Key requirements and edge cases to consider: Handling cases where `target` is not present in the array, and ensuring the solution is efficient for large inputs.
- Example test cases with explanations: For example, given `nums = [1,0,1,0,1]` and `target = 2`, the output should be `4` because there are four subarrays with sum `2`: `[1, 0, 1]`, `[1, 0, 1]`, `[0, 1]`, and `[0, 1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all possible subarrays and check their sum.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays from the input array `nums`.
  2. For each subarray, calculate its sum.
  3. If the sum equals `target`, increment the count of binary subarrays with sum `target`.
- Why this approach comes to mind first: It's a straightforward, exhaustive approach to ensure all possibilities are considered.

```cpp
int numSubarraysWithSum(vector<int>& nums, int target) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int sum = 0;
            for (int k = i; k <= j; k++) {
                sum += nums[k];
            }
            if (sum == target) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`. This is because we have three nested loops: two for generating subarrays and one for summing the elements in each subarray.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and other variables.
> - **Why these complexities occur:** The high time complexity is due to the brute force nature of generating all subarrays and summing their elements, which results in cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of summing each subarray from scratch, we can use a prefix sum array to efficiently calculate the sum of any subarray in constant time.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum array `prefixSum` where `prefixSum[i]` is the sum of the first `i` elements of `nums`.
  2. Initialize two pointers, `left` and `right`, to the start of the array.
  3. Use a hashmap `sumCount` to store the count of prefix sums seen so far.
  4. Iterate through the array, updating `right` and maintaining the sum of the current subarray.
  5. For each subarray sum, check if `sum - target` exists in `sumCount`. If it does, add the count of `sum - target` to the result.
- Proof of optimality: This approach reduces the time complexity to $O(n)$ because we only need to iterate through the array once and use constant time operations to calculate subarray sums and update counts.

```cpp
int numSubarraysWithSum(vector<int>& nums, int target) {
    int n = nums.size();
    int count = 0;
    int sum = 0;
    unordered_map<int, int> sumCount;
    sumCount[0] = 1; // Base case for sum == target when subarray starts at index 0
    
    for (int i = 0; i < n; i++) {
        sum += nums[i];
        if (sumCount.find(sum - target) != sumCount.end()) {
            count += sumCount[sum - target];
        }
        sumCount[sum]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. We iterate through the array once, and all operations within the loop take constant time.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every prefix sum in the hashmap.
> - **Optimality proof:** This solution is optimal because it achieves linear time complexity, which is the best we can do given that we must at least read the input array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sums, hashmap usage for efficient counting, and two-pointer technique.
- Problem-solving patterns identified: Reducing time complexity by avoiding redundant calculations and using data structures for efficient lookup.
- Optimization techniques learned: Using prefix sums to calculate subarray sums in constant time, and leveraging hashmaps for fast counting.
- Similar problems to practice: Problems involving subarray sums, such as finding the maximum subarray sum or the number of subarrays with a given property.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the sum or not handling edge cases properly.
- Edge cases to watch for: Empty input array, `target` being zero, or the array containing only zeros.
- Performance pitfalls: Using brute force approaches for large inputs, which can lead to timeouts or memory issues.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases, to ensure correctness and efficiency.