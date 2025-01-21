## Minimum Number of Operations to Make All Array Elements Equal to 1

**Problem Link:** https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description

**Problem Statement:**
- Input: An integer array `nums`.
- Output: The minimum number of operations to make all elements equal to 1.
- Key requirements and edge cases:
  - The array may contain duplicate elements.
  - All elements must be reduced to 1.
  - The array may be empty.
- Example test cases:
  - For `nums = [3, 2, 1]`, the output should be `3`.
  - For `nums = [2, 2, 2]`, the output should be `2`.
  - For `nums = [1, 1, 1]`, the output should be `0`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the array and counting the number of operations required to reduce each element to 1.
- Step-by-step breakdown:
  1. Initialize a variable `operations` to 0.
  2. Iterate through the array `nums`.
  3. For each element `num`, calculate the number of operations required to reduce it to 1 by subtracting 1 until `num` equals 1 and increment `operations` accordingly.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that directly addresses the problem statement.

```cpp
int minOperations(vector<int>& nums) {
    int operations = 0;
    for (int num : nums) {
        while (num > 1) {
            num -= 1;
            operations += 1;
        }
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of elements in the array and $m$ is the maximum value in the array. This is because in the worst case, we might need to subtract 1 from the largest number in the array until it reaches 1.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `operations` variable.
> - **Why these complexities occur:** The time complexity is high because of the nested loop structure (the while loop inside the for loop), and the space complexity is low because we only use a single variable to keep track of the operations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The number of operations required to reduce a number to 1 is simply the number minus 1. This is because we can subtract 1 from the number until it reaches 1, which takes `num - 1` operations.
- Detailed breakdown: We can directly calculate the number of operations for each number in the array without needing a while loop.
- Proof of optimality: This approach is optimal because it directly calculates the minimum number of operations required without any unnecessary iterations.

```cpp
int minOperations(vector<int>& nums) {
    int operations = 0;
    for (int num : nums) {
        operations += num - 1;
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we only iterate through the array once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `operations` variable.
> - **Optimality proof:** This is the optimal solution because it achieves the minimum possible time complexity of $O(n)$ by directly calculating the number of operations for each element in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct calculation and iteration.
- Problem-solving patterns identified: Looking for patterns or formulas that can simplify the problem.
- Optimization techniques learned: Avoiding unnecessary iterations and using direct calculations.
- Similar problems to practice: Other problems involving array iterations and optimizations.

**Mistakes to Avoid:**
- Common implementation errors: Using unnecessary loops or iterations.
- Edge cases to watch for: Handling empty arrays or arrays with duplicate elements.
- Performance pitfalls: Using high time complexity algorithms when simpler ones are available.
- Testing considerations: Testing with various input sizes and edge cases to ensure correctness and performance.