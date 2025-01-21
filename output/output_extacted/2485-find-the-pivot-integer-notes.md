## Find the Pivot Integer
**Problem Link:** https://leetcode.com/problems/find-the-pivot-integer/description

**Problem Statement:**
- Input format: An integer `x` representing the value to find the pivot integer for.
- Constraints: $1 \leq x \leq 1000$.
- Expected output format: The pivot integer `x` if it exists, otherwise `-1`.
- Key requirements and edge cases to consider: The pivot integer is an integer `x` such that the sum of all integers from `1` to `x` is equal to the sum of all integers from `x` to `1000`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all integers from `1` to `1000` and check if the sum of all integers from `1` to the current integer is equal to the sum of all integers from the current integer to `1000`.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `pivot` to `-1`.
  2. Iterate through all integers `i` from `1` to `1000`.
  3. For each `i`, calculate the sum of all integers from `1` to `i` and the sum of all integers from `i` to `1000`.
  4. If the two sums are equal, set `pivot` to `i`.
- Why this approach comes to mind first: It directly checks every possible integer, ensuring that the solution will be found if it exists.

```cpp
int find_pivot(int x) {
    int pivot = -1;
    for (int i = 1; i <= 1000; i++) {
        int sum1 = 0;
        int sum2 = 0;
        for (int j = 1; j <= i; j++) {
            sum1 += j;
        }
        for (int j = i; j <= 1000; j++) {
            sum2 += j;
        }
        if (sum1 == sum2) {
            pivot = i;
            break;
        }
    }
    return pivot;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the input integer `x`. The outer loop iterates $n$ times, and the inner loops also iterate up to $n$ times.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `pivot` variable and the loop counters.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space usage is due to the minimal memory required for the variables.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of calculating the sum of all integers from `1` to `i` and from `i` to `1000` for each `i`, we can use the formula for the sum of an arithmetic series: $sum = \frac{n(n + 1)}{2}$.
- Detailed breakdown of the approach:
  1. Calculate the total sum of all integers from `1` to `1000` using the formula.
  2. Iterate through all integers `i` from `1` to `1000`.
  3. For each `i`, calculate the sum of all integers from `1` to `i` using the formula.
  4. If the sum of all integers from `1` to `i` is equal to the total sum minus the sum of all integers from `1` to `i`, then `i` is the pivot integer.
- Proof of optimality: This approach has a linear time complexity, which is the best possible time complexity for this problem.

```cpp
int find_pivot(int x) {
    int pivot = -1;
    int total_sum = (1000 * 1001) / 2;
    for (int i = 1; i <= 1000; i++) {
        int sum1 = (i * (i + 1)) / 2;
        if (sum1 == total_sum - sum1 + i) {
            pivot = i;
            break;
        }
    }
    return pivot;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input integer `x`. The loop iterates $n$ times, and the calculations inside the loop take constant time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `pivot` variable and the loop counter.
> - **Optimality proof:** The linear time complexity is achieved by using the formula for the sum of an arithmetic series, which eliminates the need for nested loops.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using formulas to avoid unnecessary calculations and reduce time complexity.
- Problem-solving patterns identified: Looking for mathematical formulas or properties that can simplify the problem.
- Optimization techniques learned: Reducing the number of calculations by using formulas and eliminating nested loops.
- Similar problems to practice: Other problems that involve calculating sums or using mathematical formulas to simplify the solution.

**Mistakes to Avoid:**
- Common implementation errors: Not using the correct formula or not handling edge cases correctly.
- Edge cases to watch for: The input integer `x` can be any value between `1` and `1000`.
- Performance pitfalls: Using nested loops or not using formulas to simplify the calculations.
- Testing considerations: Test the function with different input values to ensure it returns the correct result.