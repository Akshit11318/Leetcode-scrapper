## [Pow(x, n)]
**Problem Link:** [https://leetcode.com/problems/powx-n/description](https://leetcode.com/problems/powx-n/description)

**Problem Statement:**
- Input format and constraints: The function `pow` takes two parameters, `x` and `n`, where `x` is a floating-point number and `n` is an integer.
- Expected output format: The function should return the value of `x` raised to the power of `n`.
- Key requirements and edge cases to consider: The function should handle cases where `n` is zero, negative, or positive, and `x` is zero or non-zero.
- Example test cases with explanations:
  - `pow(2.0, 3)` should return `8.0`
  - `pow(2.1, 3)` should return `9.261`
  - `pow(2.0, -3)` should return `0.125`
  - `pow(0.0, 0)` should return `1.0`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to simply multiply `x` by itself `n` times.
- Step-by-step breakdown of the solution: 
  1. Check if `n` is zero and return 1.0 if true.
  2. Initialize a variable `result` to 1.0.
  3. Multiply `result` by `x` `n` times.
- Why this approach comes to mind first: This approach is simple and easy to understand, but it's not efficient for large values of `n`.

```cpp
double myPow(double x, int n) {
    if (n == 0) return 1.0;
    double result = 1.0;
    for (int i = 0; i < abs(n); i++) {
        result *= x;
    }
    if (n < 0) return 1.0 / result;
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the absolute value of the exponent. This is because we are performing a constant amount of work `n` times.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result and other variables.
> - **Why these complexities occur:** The time complexity is high because we are using a loop to multiply `x` by itself `n` times, and the space complexity is low because we are not using any data structures that grow with the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the property of exponentiation that states $x^n = (x^{n/2})^2$ to reduce the number of multiplications required.
- Detailed breakdown of the approach: 
  1. Check if `n` is zero and return 1.0 if true.
  2. If `n` is negative, convert the problem to a positive exponent and invert the result at the end.
  3. Use a recursive approach to calculate $x^n$ by calculating $(x^{n/2})^2$.
- Proof of optimality: This approach has a time complexity of $O(log(n))$, which is optimal because we are reducing the size of the problem by half at each step.
- Why further optimization is impossible: This approach is optimal because it uses the minimum number of multiplications required to calculate $x^n$.

```cpp
double myPow(double x, int n) {
    if (n == 0) return 1.0;
    if (n < 0) {
        x = 1.0 / x;
        n = -n;
    }
    double halfPow = myPow(x, n / 2);
    if (n % 2 == 0) return halfPow * halfPow;
    return x * halfPow * halfPow;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, where $n$ is the absolute value of the exponent. This is because we are reducing the size of the problem by half at each step.
> - **Space Complexity:** $O(log(n))$, as we are using recursive calls to calculate the result.
> - **Optimality proof:** This approach is optimal because it uses the minimum number of multiplications required to calculate $x^n$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, divide-and-conquer approach, and exponentiation properties.
- Problem-solving patterns identified: Using the properties of mathematical operations to reduce the complexity of a problem.
- Optimization techniques learned: Using recursion to reduce the number of operations required.
- Similar problems to practice: Other problems that involve exponentiation or recursive approaches.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where `n` is zero, or not inverting the result when `n` is negative.
- Edge cases to watch for: When `x` is zero or `n` is very large.
- Performance pitfalls: Using a brute-force approach for large values of `n`.
- Testing considerations: Test the function with different values of `x` and `n`, including edge cases.