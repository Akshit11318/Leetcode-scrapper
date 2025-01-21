## Ugly Number
**Problem Link:** https://leetcode.com/problems/ugly-number/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input and asks to determine if it is an `ugly number`. An `ugly number` is defined as a positive integer whose only prime factors are `2`, `3`, or `5`.
- Expected output format: The function should return `true` if `n` is an `ugly number` and `false` otherwise.
- Key requirements and edge cases to consider: Handle `n = 0` and negative numbers as not `ugly`, and consider the prime factors of `n` to determine if it's `ugly`.
- Example test cases with explanations:
  - `n = 6` returns `true` because `6 = 2 * 3`.
  - `n = 8` returns `true` because `8 = 2 * 2 * 2`.
  - `n = 14` returns `false` because `14 = 2 * 7`, and `7` is not one of the allowed prime factors.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach is to check every number up to `n` to see if it's a factor of `n`, and then check if that factor is a prime number that is either `2`, `3`, or `5`. This approach is not efficient but straightforward.
- Step-by-step breakdown of the solution:
  1. Iterate through all numbers from `2` to `n`.
  2. For each number, check if it's a factor of `n`.
  3. If it's a factor, check if it's a prime number.
  4. If it's prime, check if it's `2`, `3`, or `5`.
  5. If any factor is not `2`, `3`, or `5`, return `false`.
- Why this approach comes to mind first: It's a simple, brute-force method that checks every possibility, which can be a starting point before optimizing.

```cpp
bool isUgly(int n) {
    if (n <= 0) return false; // Edge case: 0 and negative numbers are not ugly
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            bool isPrime = true;
            for (int j = 2; j * j <= i; j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime && i != 2 && i != 3 && i != 5) {
                return false; // Found a prime factor not 2, 3, or 5
            }
            while (n % i == 0) n /= i; // Divide n by the factor
        }
    }
    return true; // If no other prime factors are found, n is ugly
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{n} \cdot \sqrt{\frac{n}{2}})$, which simplifies to $O(n)$ due to the nested loop structure and division operation.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used.
> - **Why these complexities occur:** The nested loops for checking factors and primality contribute to the high time complexity, while the space complexity remains low due to the use of a fixed number of variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all factors, we can continuously divide `n` by `2`, `3`, and `5` as long as it's divisible. If `n` becomes `1`, it means all its prime factors were `2`, `3`, or `5`.
- Detailed breakdown of the approach:
  1. Check if `n` is less than or equal to `0` and return `false` if so.
  2. Continuously divide `n` by `2`, `3`, and `5` as long as it's divisible.
  3. If `n` becomes `1`, it means all factors were `2`, `3`, or `5`, so return `true`.
  4. If `n` is not `1` after the divisions, it means there's a prime factor other than `2`, `3`, or `5`, so return `false`.
- Proof of optimality: This approach directly addresses the definition of an `ugly number` by checking for the presence of only the allowed prime factors (`2`, `3`, `5`) without unnecessary checks.

```cpp
bool isUgly(int n) {
    if (n <= 0) return false;
    int[] primes = {2, 3, 5};
    for (int prime : primes) {
        while (n % prime == 0) {
            n /= prime;
        }
    }
    return n == 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, because in the worst case, we're dividing `n` by the smallest prime factor (`2`) until it's no longer divisible, which takes logarithmic time.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used to store the prime numbers and the variable `n`.
> - **Optimality proof:** This approach is optimal because it directly checks for the conditions that define an `ugly number` without any redundant operations, achieving the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prime factorization, division, and the importance of understanding the problem definition.
- Problem-solving patterns identified: Reducing a problem to its simplest form by directly addressing its core conditions.
- Optimization techniques learned: Eliminating unnecessary checks and using division to reduce the problem size.
- Similar problems to practice: Other problems involving prime numbers, factorization, and divisibility checks.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases (like `n = 0` or negative numbers), and not checking for the specific prime factors (`2`, `3`, `5`) correctly.
- Edge cases to watch for: Zero, negative numbers, and the number `1` itself.
- Performance pitfalls: Using brute-force methods that check every number or factor without optimization.
- Testing considerations: Ensure to test with various inputs, including edge cases and numbers with different prime factors.