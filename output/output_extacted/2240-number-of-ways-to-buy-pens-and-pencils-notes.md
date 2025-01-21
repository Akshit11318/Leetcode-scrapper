## Number of Ways to Buy Pens and Pencils
**Problem Link:** https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/description

**Problem Statement:**
- Input format and constraints: The problem takes two integers, `pricePen` and `pricePencil`, representing the price of a pen and a pencil, respectively, and an integer `total`, representing the total amount of money available to spend.
- Expected output format: The function should return the number of ways to buy pens and pencils with the given total amount of money.
- Key requirements and edge cases to consider: The function should handle cases where the total amount of money is less than the price of a pen or a pencil, as well as cases where the total amount of money is exactly equal to the price of a pen or a pencil.
- Example test cases with explanations:
  - If `pricePen = 1`, `pricePencil = 1`, and `total = 4`, the function should return `5` because there are 5 ways to buy pens and pencils: `(0 pens, 4 pencils)`, `(1 pen, 3 pencils)`, `(2 pens, 2 pencils)`, `(3 pens, 1 pencil)`, and `(4 pens, 0 pencils)`.
  - If `pricePen = 10`, `pricePencil = 1`, and `total = 9`, the function should return `10` because there are 10 ways to buy pens and pencils: `(0 pens, 9 pencils)`, `(1 pen, 8 pencils)`, ..., `(9 pens, 0 pencils)`, but since we can't buy a pen with the remaining money, we have to stop at `(0 pens, 9 pencils)`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can iterate over all possible numbers of pens that can be bought with the given total amount of money, and for each number of pens, calculate the remaining amount of money that can be spent on pencils.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `ways` to store the number of ways to buy pens and pencils.
  2. Iterate over all possible numbers of pens that can be bought with the given total amount of money.
  3. For each number of pens, calculate the remaining amount of money that can be spent on pencils.
  4. If the remaining amount of money is non-negative, increment the `ways` variable by 1.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it involves iterating over all possible numbers of pens.

```cpp
int waysToBuyPensPencils(int pricePen, int pricePencil, int total) {
    int ways = 0;
    for (int pens = 0; pens <= total / pricePen; pens++) {
        int remaining = total - pens * pricePen;
        if (remaining >= 0) {
            ways++;
        }
    }
    return ways;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{total}{pricePen})$ because we iterate over all possible numbers of pens that can be bought with the given total amount of money.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store the `ways` variable.
> - **Why these complexities occur:** The time complexity occurs because we iterate over all possible numbers of pens, and the space complexity occurs because we use a constant amount of space to store the `ways` variable.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use the formula for the number of ways to buy pens and pencils, which is $\frac{total}{pricePencil} + 1$ if $total$ is divisible by $pricePencil$, and $\frac{total}{pricePencil} + 1$ if $total$ is not divisible by $pricePencil$.
- Detailed breakdown of the approach:
  1. Calculate the number of ways to buy pens and pencils using the formula.
  2. Return the calculated number of ways.
- Proof of optimality: This approach is optimal because it uses a constant amount of time and space, regardless of the input size.
- Why further optimization is impossible: Further optimization is impossible because we have reduced the time complexity to $O(1)$, which is the best possible time complexity.

```cpp
int waysToBuyPensPencils(int pricePen, int pricePencil, int total) {
    return total / pricePencil + 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we use a constant amount of time to calculate the number of ways.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store the result.
> - **Optimality proof:** This approach is optimal because it uses a constant amount of time and space, regardless of the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of using formulas to solve problems efficiently.
- Problem-solving patterns identified: The problem identifies the pattern of using formulas to reduce the time complexity of a problem.
- Optimization techniques learned: The problem teaches the technique of using formulas to optimize the time complexity of a problem.
- Similar problems to practice: Similar problems to practice include problems that involve using formulas to solve problems efficiently.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use a brute force approach instead of using a formula to solve the problem.
- Edge cases to watch for: An edge case to watch for is when the total amount of money is less than the price of a pen or a pencil.
- Performance pitfalls: A performance pitfall is to use a brute force approach instead of using a formula to solve the problem.
- Testing considerations: A testing consideration is to test the function with different input values to ensure that it works correctly.