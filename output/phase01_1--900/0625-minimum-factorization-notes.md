## Minimum Factorization
**Problem Link:** https://leetcode.com/problems/minimum-factorization/description

**Problem Statement:**
- Input: a single integer `n`
- Constraints: `n` is in the range `[2, 10^9]`
- Expected output: the minimum number of factors that multiply together to give `n`, or `-1` if no such factorization exists
- Key requirements: find the minimum number of factors, considering that `1` is not considered a factor
- Edge cases: handle cases where `n` is a prime number, or where `n` has multiple distinct prime factors

**Example Test Cases:**
- Input: `n = 12`, Output: `3` (Explanation: `2 * 2 * 3 = 12`)
- Input: `n = 7`, Output: `-1` (Explanation: `7` is a prime number and cannot be factored further)
- Input: `n = 15`, Output: `4` (Explanation: `3 * 5 = 15`, but we can also consider `3 * 5` as `3 * 5 * 1 * 1`, so we get `4`)

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of factors to find the minimum number of factors that multiply together to give `n`.
- Step-by-step breakdown:
  1. Iterate through all numbers from `2` to `sqrt(n)`.
  2. For each number, check if it is a factor of `n`.
  3. If it is a factor, recursively factorize the remaining number.
  4. Keep track of the minimum number of factors found so far.

```cpp
int minFactors(int n) {
    int min = INT_MAX;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            int factors = 1 + minFactors(n / i);
            min = std::min(min, factors);
        }
    }
    return min == INT_MAX ? -1 : min;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{log(n)}) = O(n)$ (Explanation: in the worst-case scenario, we have to try all numbers up to `n` to find the minimum number of factors)
> - **Space Complexity:** $O(log(n))$ (Explanation: the maximum depth of the recursion tree is `log(n)` due to the recursive nature of the algorithm)
> - **Why these complexities occur:** The brute force approach tries all possible combinations of factors, resulting in exponential time complexity. The space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a prime factorization approach to find the minimum number of factors.
- Detailed breakdown:
  1. Find the prime factors of `n` using a sieve or a prime factorization algorithm.
  2. For each prime factor, calculate the power of the factor in the factorization of `n`.
  3. The minimum number of factors is the sum of the powers of all prime factors.

```cpp
int minFactors(int n) {
    int factors = 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            int power = 0;
            while (n % i == 0) {
                n /= i;
                power++;
            }
            factors += power;
        }
    }
    if (n > 1) {
        factors++;
    }
    return factors;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(sqrt(n))$ (Explanation: we only need to iterate up to `sqrt(n)` to find all prime factors)
> - **Space Complexity:** $O(1)$ (Explanation: we only use a constant amount of space to store the factors and powers)
> - **Optimality proof:** The prime factorization approach is optimal because it directly calculates the minimum number of factors without trying all possible combinations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: prime factorization, recursive algorithms
- Problem-solving patterns: using a sieve or prime factorization algorithm to find prime factors
- Optimization techniques: using a prime factorization approach to reduce time complexity
- Similar problems to practice: finding the maximum number of factors, finding the number of distinct prime factors

**Mistakes to Avoid:**
- Not considering the case where `n` is a prime number
- Not handling the case where `n` has multiple distinct prime factors
- Using a brute force approach without considering the time complexity
- Not optimizing the algorithm using a prime factorization approach