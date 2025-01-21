## Count Almost Equal Pairs I
**Problem Link:** https://leetcode.com/problems/count-almost-equal-pairs-i/description

**Problem Statement:**
- Given a `0-indexed` integer array `nums` and an integer `k`, return the number of pairs of indices `(i, j)` where `0 <= i < j < nums.length` and `abs(nums[i] - nums[j]) <= k`.
- Input format and constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^5`, `0 <= k <= 10^5`.
- Expected output format: An integer representing the count of almost equal pairs.
- Key requirements and edge cases to consider: Pairs must be distinct indices, and the absolute difference must be within the given limit `k`.
- Example test cases with explanations:
  - For `nums = [1,2,3,4,5]` and `k = 3`, the pairs are `(0,1)`, `(0,2)`, `(0,3)`, `(1,2)`, `(1,3)`, `(1,4)`, `(2,3)`, `(2,4)`, `(3,4)`, resulting in `9` pairs.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all pairs of indices in the array and check if the absolute difference between the elements at these indices is within the limit `k`.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for the number of almost equal pairs.
  2. Iterate through the array with two nested loops to consider each pair of indices `(i, j)` where `i < j`.
  3. For each pair, calculate the absolute difference between `nums[i]` and `nums[j]`.
  4. If the absolute difference is less than or equal to `k`, increment the counter.
- Why this approach comes to mind first: It directly implements the problem statement, checking every possible pair without any optimization.

```cpp
int countAlmostEqualPairs(vector<int>& nums, int k) {
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
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`, because we are iterating through the array with two nested loops.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because we are using a constant amount of space to store the count and loop variables.
> - **Why these complexities occur:** The time complexity is quadratic because we are checking every pair of elements, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a `map` or `unordered_map` to store the frequency of each number in the array. Then, for each number, we can find the numbers that are within the limit `k` by checking the map for keys within the range `[num - k, num + k]`.
- Detailed breakdown of the approach:
  1. Create a map to store the frequency of each number in the array.
  2. Initialize a counter for the number of almost equal pairs.
  3. Iterate through the array, and for each number, calculate the range of numbers that are within the limit `k`.
  4. Use the map to find the numbers within this range and increment the counter accordingly.
- Proof of optimality: This approach reduces the time complexity from $O(n^2)$ to $O(n)$ because we are iterating through the array once and using the map for constant time lookups.

```cpp
int countAlmostEqualPairs(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    int count = 0;
    for (int num : nums) {
        for (int i = max(0, num - k); i <= min(100000, num + k); i++) {
            if (freq.find(i) != freq.end()) {
                count += freq[i];
            }
        }
        freq[num]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, where $n$ is the number of elements in `nums` and $k$ is the given limit. However, since $k$ is bounded by a constant (in this case, $10^5$), the time complexity can be considered as $O(n)$.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every number in the map.
> - **Optimality proof:** This is the optimal solution because we are iterating through the array once and using the map for constant time lookups, reducing the time complexity significantly compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a map to store frequency and iterating through the array to find almost equal pairs.
- Problem-solving patterns identified: Reducing the time complexity by using a data structure for efficient lookups.
- Optimization techniques learned: Using a map to avoid nested loops and reduce the time complexity from $O(n^2)$ to $O(nk)$, which is effectively $O(n)$ due to the bounded nature of $k$.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the counter or the map correctly.
- Edge cases to watch for: Ensuring that the range of numbers checked is within the valid range (e.g., `[0, 10^5]`) to avoid unnecessary iterations.
- Performance pitfalls: Using a data structure that does not provide constant time lookups, such as a list or a vector, which would increase the time complexity.
- Testing considerations: Testing the function with arrays of varying sizes and with different values of `k` to ensure correctness and performance.