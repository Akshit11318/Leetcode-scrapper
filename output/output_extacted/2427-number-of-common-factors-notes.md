## Number of Common Factors
**Problem Link:** https://leetcode.com/problems/number-of-common-factors/description

**Problem Statement:**
- Input format and constraints: Given two positive integers `a` and `b`, find the number of common factors of `a` and `b`.
- Expected output format: Return the number of common factors as an integer.
- Key requirements and edge cases to consider: The input integers are within the range of 1 to $10^{12}$, and the number of common factors should be calculated efficiently.
- Example test cases with explanations:
  - For `a = 12` and `b = 15`, the common factors are 1 and 3, so the output should be 2.
  - For `a = 25` and `b = 30`, the common factors are 1 and 5, so the output should be 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating through all numbers from 1 to the minimum of `a` and `b` to check if each number is a factor of both `a` and `b`.
- Step-by-step breakdown of the solution:
  1. Initialize a counter variable `count` to 0.
  2. Iterate through all numbers `i` from 1 to the minimum of `a` and `b`.
  3. For each `i`, check if `i` is a factor of both `a` and `b` by verifying if `a % i == 0` and `b % i == 0`.
  4. If `i` is a factor of both `a` and `b`, increment the `count` variable.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it directly checks all possible factors of `a` and `b`.

```cpp
int commonFactors(int a, int b) {
    int count = 0;
    for (int i = 1; i <= min(a, b); i++) {
        if (a % i == 0 && b % i == 0) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(min(a, b))$, where $a$ and $b$ are the input integers. This is because we iterate through all numbers from 1 to the minimum of `a` and `b`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counter variable.
> - **Why these complexities occur:** The time complexity is high because we check every possible factor, and the space complexity is low because we only use a single variable to store the count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all numbers up to the minimum of `a` and `b`, we can find the greatest common divisor (GCD) of `a` and `b` and then count the number of factors of the GCD.
- Detailed breakdown of the approach:
  1. Calculate the GCD of `a` and `b` using the Euclidean algorithm.
  2. Initialize a counter variable `count` to 0.
  3. Iterate through all numbers `i` from 1 to the square root of the GCD.
  4. For each `i`, check if `i` is a factor of the GCD by verifying if `GCD % i == 0`.
  5. If `i` is a factor of the GCD, increment the `count` variable. If `i` is not equal to its corresponding factor (i.e., `GCD / i`), increment the `count` variable again.
- Proof of optimality: This approach is optimal because it reduces the number of iterations from $O(min(a, b))$ to $O(\sqrt{GCD(a, b)})$, which is significantly faster for large inputs.

```cpp
int commonFactors(int a, int b) {
    int gcd = calculateGCD(a, b);
    int count = 0;
    for (int i = 1; i * i <= gcd; i++) {
        if (gcd % i == 0) {
            if (i * i == gcd) {
                count++;
            } else {
                count += 2;
            }
        }
    }
    return count;
}

int calculateGCD(int a, int b) {
    if (b == 0) {
        return a;
    }
    return calculateGCD(b, a % b);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{GCD(a, b)})$, where $GCD(a, b)$ is the greatest common divisor of `a` and `b`. This is because we iterate through all numbers from 1 to the square root of the GCD.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counter variable and the GCD.
> - **Optimality proof:** The time complexity is optimal because we only check factors up to the square root of the GCD, and the space complexity is optimal because we only use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The Euclidean algorithm for calculating the GCD, and the technique of counting factors by iterating up to the square root of a number.
- Problem-solving patterns identified: Reducing the problem size by finding the GCD, and using the properties of factors to optimize the solution.
- Optimization techniques learned: Using the square root of a number to reduce the number of iterations, and using the properties of GCD to simplify the problem.
- Similar problems to practice: Other problems involving GCD, LCM, and factor counting, such as finding the number of divisors of a number or calculating the sum of divisors.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as when `a` or `b` is 0, and not using the optimal approach for calculating the GCD.
- Edge cases to watch for: When `a` or `b` is 0, and when `a` and `b` are very large numbers.
- Performance pitfalls: Using the brute force approach for large inputs, and not optimizing the solution by using the properties of GCD and factors.
- Testing considerations: Testing the solution with different inputs, including edge cases, and verifying the correctness of the output.