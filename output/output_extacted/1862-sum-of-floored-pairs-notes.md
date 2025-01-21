## Sum of Floored Pairs
**Problem Link:** https://leetcode.com/problems/sum-of-floored-pairs/description

**Problem Statement:**
- Input: An integer array `nums`.
- Expected output: The sum of all `floor(nums[i] / nums[j])` where `i < j`.
- Key requirements: 
  - `1 <= nums.length <= 10^5`
  - `1 <= nums[i] <= 10^6`
- Edge cases:
  - Empty input array
  - Single-element array
- Example test cases:
  - Input: `[2, 5, 9]`
    - Explanation: For `i = 0` and `j = 1`, `floor(2/5) = 0`. For `i = 0` and `j = 2`, `floor(2/9) = 0`. For `i = 1` and `j = 2`, `floor(5/9) = 0`. Sum is `0`.
  - Input: `[7, 7, 7, 7]`
    - Explanation: For any pair, `floor(nums[i] / nums[j]) = floor(7/7) = 1`. Since there are `6` pairs (`4C2`), the sum is `6`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate `floor(nums[i] / nums[j])` for all pairs of `i` and `j` where `i < j`.
- Step-by-step breakdown:
  1. Iterate over the `nums` array for `i`.
  2. For each `i`, iterate over the remaining elements `j` where `i < j`.
  3. Calculate `floor(nums[i] / nums[j])` for each pair `(i, j)`.
  4. Sum up all the calculated values.

```cpp
int sumOfFlooredPairs(vector<int>& nums) {
    int n = nums.size();
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            sum += nums[i] / nums[j];
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where `n` is the number of elements in `nums`. This is because we are iterating over all pairs of elements.
> - **Space Complexity:** $O(1)$, excluding the input array, because we are only using a constant amount of space to store the sum.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, and the single variable for sum causes the constant space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: For a given `nums[i]`, we can calculate the contribution of all `nums[j]` where `j > i` by considering how many times `nums[j]` can divide `nums[i]` without remainder.
- Detailed breakdown:
  1. For each `nums[i]`, iterate over possible divisors `d` from `1` to `nums[i]`.
  2. For each `d`, count how many `nums[j]` satisfy `d <= nums[j] < d + 1` and `nums[i] / d <= nums[j] < (nums[i] / d) + 1`.
  3. The contribution of `nums[i]` to the sum is then `d * count` for each `d`, summed over all `d`.

However, a more efficient approach involves observing the pattern of division and realizing that for each `nums[i]`, the values of `floor(nums[i] / nums[j])` are discrete and can be counted efficiently by iterating over all possible values of `floor(nums[i] / nums[j])` for each `nums[i]`.

```cpp
int sumOfFlooredPairs(vector<int>& nums) {
    int maxVal = *max_element(nums.begin(), nums.end());
    vector<int> count(maxVal + 1, 0);
    for (int num : nums) count[num]++;
    
    int sum = 0;
    for (int i = 0; i < nums.size(); ++i) {
        for (int j = 1; j <= maxVal; ++j) {
            if (nums[i] < j) break;
            int cnt = 0;
            for (int k = j; k <= maxVal; k += j) {
                cnt += count[k];
            }
            sum += (nums[i] / j) * cnt;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n * maxVal)$, where `n` is the number of elements in `nums` and `maxVal` is the maximum value in `nums`.
> - **Space Complexity:** $O(maxVal)$, for storing the count of each number.
> - **Optimality proof:** This approach is more efficient than the brute force because it avoids redundant calculations by counting the occurrences of each divisor and its multiples, thus reducing the number of divisions required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Efficient counting, avoiding redundant calculations.
- Problem-solving patterns: Identifying discrete patterns in continuous problems.
- Optimization techniques: Using counts to reduce the number of operations.
- Similar problems to practice: Other problems involving efficient counting and division.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect loop bounds, missing edge cases.
- Edge cases to watch for: Empty input array, single-element array, maximum value in the array.
- Performance pitfalls: Using brute force for large inputs, not optimizing division operations.
- Testing considerations: Test with various input sizes and values to ensure correctness and efficiency.