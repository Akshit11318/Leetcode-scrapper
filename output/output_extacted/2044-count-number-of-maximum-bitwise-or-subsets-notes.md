## Count Number of Maximum Bitwise OR Subsets

**Problem Link:** https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description

**Problem Statement:**
- Given an array `nums` of size `n`, find the number of subsets of `nums` that have the maximum bitwise OR value.
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 20`, `0 <= nums[i] <= 10^6`.
- Expected output format: The number of subsets with the maximum bitwise OR value.
- Key requirements and edge cases to consider: Handling empty arrays, arrays with a single element, and large arrays with varying bitwise OR values.
- Example test cases with explanations:
  - `nums = [3, 1]`: The subsets are `[3]`, `[1]`, and `[3,1]`. The maximum bitwise OR value is `3`, which is achieved by the subsets `[3]` and `[3,1]`. Therefore, the output is `2`.
  - `nums = [2, 2, 2]`: The subsets are `[2]`, `[2,2]`, and `[2,2,2]`. The maximum bitwise OR value is `2`, which is achieved by all subsets. Therefore, the output is `8`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsets of the input array and calculate the bitwise OR value for each subset.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the input array using a recursive approach or bit manipulation.
  2. For each subset, calculate the bitwise OR value by iterating over the elements and performing the bitwise OR operation.
  3. Keep track of the maximum bitwise OR value encountered so far and the number of subsets that achieve this value.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that involves generating all possible subsets and calculating their bitwise OR values.

```cpp
int countMaxOrSubsets(vector<int>& nums) {
    int n = nums.size();
    int maxOr = 0;
    int count = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int orVal = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                orVal |= nums[i];
            }
        }
        if (orVal > maxOr) {
            maxOr = orVal;
            count = 1;
        } else if (orVal == maxOr) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we generate all possible subsets (which takes $O(2^n)$ time) and calculate the bitwise OR value for each subset (which takes $O(n)$ time).
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum bitwise OR value and the count of subsets that achieve this value.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible subsets and calculate their bitwise OR values. The space complexity is low because we only use a constant amount of space to store the maximum bitwise OR value and the count of subsets.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force solution, but with a slight optimization. Instead of iterating over all possible subsets, we can use a bitmask to generate all possible subsets and calculate their bitwise OR values.
- Detailed breakdown of the approach:
  1. Initialize the maximum bitwise OR value and the count of subsets that achieve this value.
  2. Iterate over all possible subsets using a bitmask.
  3. For each subset, calculate the bitwise OR value by iterating over the elements and performing the bitwise OR operation.
  4. Update the maximum bitwise OR value and the count of subsets that achieve this value as needed.
- Proof of optimality: This approach is optimal because it has the same time complexity as the brute force solution, but with a slight optimization. We cannot do better than this because we must generate all possible subsets and calculate their bitwise OR values to find the maximum bitwise OR value.

```cpp
int countMaxOrSubsets(vector<int>& nums) {
    int n = nums.size();
    int maxOr = 0;
    int count = 0;
    for (int mask = 1; mask < (1 << n); mask++) {
        int orVal = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                orVal |= nums[i];
            }
        }
        if (orVal > maxOr) {
            maxOr = orVal;
            count = 1;
        } else if (orVal == maxOr) {
            count++;
        }
    }
    return count + (maxOr == 0);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we generate all possible subsets (which takes $O(2^n)$ time) and calculate the bitwise OR value for each subset (which takes $O(n)$ time).
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum bitwise OR value and the count of subsets that achieve this value.
> - **Optimality proof:** This approach is optimal because it has the same time complexity as the brute force solution, but with a slight optimization. We cannot do better than this because we must generate all possible subsets and calculate their bitwise OR values to find the maximum bitwise OR value.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, subset generation, and bitwise OR calculation.
- Problem-solving patterns identified: Using a bitmask to generate all possible subsets and calculating their bitwise OR values.
- Optimization techniques learned: Slight optimization by starting the bitmask iteration from 1 instead of 0.
- Similar problems to practice: Counting the number of subsets with a certain property (e.g., sum, product, etc.).

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the maximum bitwise OR value and the count of subsets, or using an incorrect bitmask iteration range.
- Edge cases to watch for: Handling empty arrays, arrays with a single element, and large arrays with varying bitwise OR values.
- Performance pitfalls: Using an inefficient approach to generate all possible subsets or calculate their bitwise OR values.
- Testing considerations: Testing the solution with various input arrays, including edge cases and large arrays.