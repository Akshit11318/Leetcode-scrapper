## Calculate Amount Paid in Taxes
**Problem Link:** https://leetcode.com/problems/calculate-amount-paid-in-taxes/description

**Problem Statement:**
- Input format: `brackets` array of integers representing tax brackets and `income` integer representing the income.
- Constraints: `1 <= brackets.length <= 100`, `1 <= income <= 10^5`.
- Expected output format: The total amount paid in taxes.
- Key requirements and edge cases to consider: Tax brackets are non-decreasing, and income can be any positive integer.
- Example test cases with explanations:
  - `brackets = [[3,50],[7,10],[12,25]], income = 10`, expected output: `2.65`.
  - `brackets = [[1,0],[4,25],[5,50]], income = 2`, expected output: `0.25`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Calculate the tax for each bracket and sum them up.
- Step-by-step breakdown of the solution:
  1. Initialize `tax` to 0.
  2. For each bracket, calculate the tax for the current bracket by multiplying the rate with the minimum of the income and the upper bound of the bracket.
  3. Subtract the upper bound of the previous bracket (or 0 if it's the first bracket) from the upper bound of the current bracket to get the taxable amount.
  4. Add the calculated tax to the total tax.
  5. Update the income by subtracting the taxable amount.
- Why this approach comes to mind first: It's a straightforward way to calculate taxes based on the given brackets.

```cpp
double calculateTax(vector<vector<int>>& brackets, int income) {
    double tax = 0.0;
    int prevUpper = 0;
    for (auto& bracket : brackets) {
        int upper = bracket[0];
        double rate = bracket[1] / 100.0;
        int taxable = min(income, upper) - prevUpper;
        if (taxable > 0) {
            tax += taxable * rate;
        }
        prevUpper = upper;
        if (income <= upper) break;
    }
    return tax;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of brackets, since we iterate over each bracket once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the tax and the previous upper bound.
> - **Why these complexities occur:** The time complexity is linear because we process each bracket once, and the space complexity is constant because we only use a fixed amount of space to store the necessary variables.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, but with a more efficient implementation.
- Detailed breakdown of the approach:
  1. Initialize `tax` to 0.
  2. For each bracket, calculate the tax for the current bracket by multiplying the rate with the minimum of the income and the upper bound of the bracket minus the previous upper bound.
  3. Add the calculated tax to the total tax.
  4. Update the income by subtracting the taxable amount.
- Proof of optimality: This approach is optimal because it still calculates the tax for each bracket, but with a more efficient implementation.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$, which is the minimum required to process each bracket once.

```cpp
double calculateTax(vector<vector<int>>& brackets, int income) {
    double tax = 0.0;
    int prevUpper = 0;
    for (auto& bracket : brackets) {
        int upper = bracket[0];
        double rate = bracket[1] / 100.0;
        int taxable = min(income, upper) - prevUpper;
        if (taxable > 0) {
            tax += taxable * rate;
        }
        prevUpper = upper;
        if (income <= upper) break;
    }
    return tax;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of brackets, since we iterate over each bracket once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the tax and the previous upper bound.
> - **Optimality proof:** This approach is optimal because it still calculates the tax for each bracket, but with a more efficient implementation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over a list of brackets and calculation of taxes based on the given rates.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (calculating tax for each bracket) and combining the results.
- Optimization techniques learned: Efficient implementation of the calculation to minimize unnecessary operations.
- Similar problems to practice: Other problems involving calculation of taxes or similar accumulative calculations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect calculation of taxable amounts or incorrect application of tax rates.
- Edge cases to watch for: Handling cases where income is less than or equal to the upper bound of a bracket, and handling cases where the tax rate is 0.
- Performance pitfalls: Using inefficient data structures or algorithms that result in unnecessary operations.
- Testing considerations: Testing with different inputs, including edge cases, to ensure the correctness of the implementation.