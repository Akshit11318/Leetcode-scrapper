## Check If Array Is Good
**Problem Link:** https://leetcode.com/problems/check-if-array-is-good/description

**Problem Statement:**
- Input format: An array `nums` of integers.
- Constraints: The array can have any length, and integers can be positive or negative.
- Expected output format: A boolean indicating whether the array is "good".
- Key requirements and edge cases to consider: An array is "good" if for every index `i`, the sum of the elements in the range `[0, i]` is greater than or equal to the sum of the elements in the range `[i + 1, n - 1]`, where `n` is the length of the array.
- Example test cases:
  - Input: `nums = [3,4,2,5]`
    - Output: `True`
    - Explanation: The sums are `[3, 7, 9, 14]` for the first range and `[10, 9, 7, 5]` for the second range. The condition is met for all indices.
  - Input: `nums = [2,3,0,2]`
    - Output: `False`
    - Explanation: For `i = 3`, the sum in the first range is `7` (`2 + 3 + 0 + 2`), and the sum in the second range is `0` (empty range), but for `i = 0`, the sum in the first range is `2`, and in the second range is `5`, violating the condition.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each index `i` in the array, calculate the sum of the elements from `0` to `i` and the sum of the elements from `i + 1` to the end of the array. Compare these sums to determine if the array is "good".
- Step-by-step breakdown of the solution:
  1. Initialize a variable to track if the array is "good".
  2. Loop through each index `i` in the array.
  3. For each `i`, calculate the sum of the elements in the range `[0, i]`.
  4. Calculate the sum of the elements in the range `[i + 1, n - 1]`.
  5. Compare the sums. If the sum of the elements in the first range is ever less than the sum in the second range, mark the array as not "good" and exit the loop.
- Why this approach comes to mind first: It directly implements the condition given in the problem statement.

```cpp
bool isGoodArray(vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        int sumFirstRange = 0;
        int sumSecondRange = 0;
        for (int j = 0; j <= i; j++) {
            sumFirstRange += nums[j];
        }
        for (int j = i + 1; j < n; j++) {
            sumSecondRange += nums[j];
        }
        if (sumFirstRange < sumSecondRange) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because for each element in the array, we potentially sum all elements in the array again.
> - **Space Complexity:** $O(1)$ since we only use a constant amount of space to store the sums and the loop variables.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of recalculating the sums for each index `i`, we can maintain a running sum from the start of the array and only need to calculate the sum from `i + 1` to the end once.
- Detailed breakdown of the approach:
  1. Calculate the total sum of the array.
  2. Initialize a running sum starting from `0`.
  3. Loop through the array, at each index `i`:
    - Add the current element to the running sum.
    - Subtract the current element from the total sum (to get the sum from `i + 1` to the end).
    - Compare the running sum with the adjusted total sum. If the running sum is ever less than the adjusted total sum, return `false`.
  4. If the loop completes without finding any index where the condition is violated, return `true`.
- Proof of optimality: This approach reduces the time complexity to linear because we only make a single pass through the array, calculating the necessary sums in constant time per element.

```cpp
bool isGoodArray(vector<int>& nums) {
    int n = nums.size();
    int totalSum = 0;
    for (int num : nums) {
        totalSum += num;
    }
    int runningSum = 0;
    for (int i = 0; i < n; i++) {
        runningSum += nums[i];
        if (runningSum < (totalSum - runningSum)) {
            return false;
        }
        // Alternatively, totalSum -= nums[i]; and compare runningSum with totalSum directly
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we make two passes through the array: one to calculate the total sum and another to check the condition for each index.
> - **Space Complexity:** $O(1)$ since we only use a constant amount of space to store the sums and the loop variables.
> - **Optimality proof:** This is optimal because we must at least read the input once, which takes $O(n)$ time. Our solution achieves this lower bound.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Maintaining running sums to avoid redundant calculations.
- Problem-solving patterns identified: Looking for ways to reduce the number of operations by storing and updating intermediate results.
- Optimization techniques learned: Avoiding nested loops by calculating necessary values in a single pass.
- Similar problems to practice: Other problems involving array sums, prefix sums, or maintaining running totals.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating running sums or total sums.
- Edge cases to watch for: Empty arrays or arrays with a single element.
- Performance pitfalls: Using unnecessary nested loops or data structures.
- Testing considerations: Ensure to test with arrays of varying lengths and with both positive and negative numbers.