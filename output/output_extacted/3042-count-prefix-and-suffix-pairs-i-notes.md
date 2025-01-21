## Count Prefix and Suffix Pairs I

**Problem Link:** https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`.
- Expected Output: The number of pairs of indices `(i, j)` such that `i < j` and `nums[i] + nums[j] == target`, where `target` is a given integer.
- Key Requirements: Count the pairs of indices that satisfy the given condition.
- Edge Cases: Consider cases where the input array is empty, or the target is not achievable with any pair of numbers in the array.

**Example Test Cases:**
- Input: `nums = [1, 1, 2, 2, 3], target = 3`.
- Expected Output: `4`.
- Explanation: The pairs of indices that satisfy the condition are `(0, 2)`, `(0, 3)`, `(1, 2)`, `(1, 3)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the number of pairs of indices that satisfy the condition, we can iterate over all pairs of indices and check if the sum of the corresponding numbers equals the target.
- Step-by-step breakdown of the solution:
  1. Iterate over all pairs of indices `(i, j)` in the input array.
  2. For each pair, check if `i < j` and `nums[i] + nums[j] == target`.
  3. If the condition is satisfied, increment the count of pairs.

```cpp
int countPairs(vector<int>& nums, int target) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] == target) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array, because we iterate over all pairs of indices.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the count of pairs.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it checks all pairs of indices, resulting in a quadratic number of operations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a `unordered_map` to store the frequency of each number in the input array, and then iterate over the array to find the number of pairs that satisfy the condition.
- Detailed breakdown of the approach:
  1. Create an `unordered_map` to store the frequency of each number in the input array.
  2. Iterate over the input array and for each number, find its complement with respect to the target.
  3. If the complement is already in the `unordered_map`, increment the count of pairs by the frequency of the complement.
  4. Update the frequency of the current number in the `unordered_map`.

```cpp
int countPairs(vector<int>& nums, int target) {
    unordered_map<int, int> freq;
    int count = 0;
    for (int num : nums) {
        int complement = target - num;
        if (freq.find(complement) != freq.end()) {
            count += freq[complement];
        }
        freq[num]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, because we iterate over the array once and perform constant-time operations for each element.
> - **Space Complexity:** $O(n)$, because we use an `unordered_map` to store the frequency of each number, which can have up to $n$ elements in the worst case.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the input array and uses a data structure that allows for constant-time lookups and updates.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using an `unordered_map` to store frequency information and iterating over the input array to find pairs that satisfy a condition.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and using a data structure to store intermediate results.
- Optimization techniques learned: Using a data structure with constant-time operations to reduce the time complexity of the algorithm.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the existence of a key in the `unordered_map` before accessing its value.
- Edge cases to watch for: Handling cases where the input array is empty or the target is not achievable with any pair of numbers in the array.
- Performance pitfalls: Using a data structure with high time complexity operations, such as a `vector` or `list`, to store frequency information.
- Testing considerations: Testing the algorithm with different input arrays and targets to ensure it produces the correct output.