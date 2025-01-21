## Ways to Make a Fair Array
**Problem Link:** https://leetcode.com/problems/ways-to-make-a-fair-array/description

**Problem Statement:**
- Input format: An integer array `nums` of size `n`.
- Constraints: `1 <= n <= 10^5`, `1 <= nums[i] <= 10^5`.
- Expected output format: The number of ways to make the array fair by removing at most one element.
- Key requirements and edge cases to consider: The array is fair if the sum of all elements at even indices is equal to the sum of all elements at odd indices.
- Example test cases with explanations:
  - `nums = [1, 1, 1]`, the output should be `3` because we can remove any element to make the array fair.
  - `nums = [2, 1, 6, 4]`, the output should be `1` because we can only remove the element at index `2` to make the array fair.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible removals of one element and calculate the sum of even and odd indices for each case.
- Step-by-step breakdown of the solution:
  1. Calculate the sum of elements at even and odd indices for the original array.
  2. For each element in the array, remove it and calculate the sum of even and odd indices.
  3. Check if the sums are equal after removal. If they are, increment the count of ways to make the array fair.
- Why this approach comes to mind first: It's a straightforward and intuitive approach that checks all possible cases.

```cpp
int waysToMakeFair(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int evenSum = 0, oddSum = 0;
        for (int j = 0; j < n; j++) {
            if (j == i) continue;
            if (j % 2 == 0) evenSum += nums[j];
            else oddSum += nums[j];
        }
        if (evenSum == oddSum) count++;
    }
    // Check if the array is already fair
    int evenSum = 0, oddSum = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) evenSum += nums[i];
        else oddSum += nums[i];
    }
    if (evenSum == oddSum) count++;
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because we have a nested loop structure.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the sums and count.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, while the constant space usage keeps the space complexity linear.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of recalculating the sums for each removal, we can calculate the difference between the sums of even and odd indices and update it as we iterate through the array.
- Detailed breakdown of the approach:
  1. Calculate the initial difference between the sums of even and odd indices.
  2. Iterate through the array and update the difference as we go.
  3. Check if the difference becomes zero after removing an element. If it does, increment the count of ways to make the array fair.
- Proof of optimality: This approach has a linear time complexity, which is optimal because we must at least read the input array once.

```cpp
int waysToMakeFair(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    int evenSum = 0, oddSum = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) evenSum += nums[i];
        else oddSum += nums[i];
    }
    int diff = evenSum - oddSum;
    for (int i = 0; i < n; i++) {
        int newDiff = diff;
        if (i % 2 == 0) newDiff -= nums[i];
        else newDiff += nums[i];
        if (newDiff == 0) count++;
    }
    if (diff == 0) count++;
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we only iterate through the array once.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the sums and count.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity, which is the minimum required to read the input array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Updating sums and differences as we iterate through an array.
- Problem-solving patterns identified: Using a single pass through the array to calculate the required sums and differences.
- Optimization techniques learned: Avoiding recalculations by updating sums and differences incrementally.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the sums and differences correctly as we iterate through the array.
- Edge cases to watch for: Handling the case where the array is already fair.
- Performance pitfalls: Using a brute force approach with a quadratic time complexity.
- Testing considerations: Testing the code with arrays of different sizes and contents to ensure it works correctly.