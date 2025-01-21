## The Kth Factor of N
**Problem Link:** https://leetcode.com/problems/the-kth-factor-of-n/description

**Problem Statement:**
- Input format and constraints: The problem takes two integers, `n` and `k`, where `n` is the number for which we need to find factors, and `k` is the position of the factor in the sorted list of factors.
- Expected output format: The `k`th factor of `n`.
- Key requirements and edge cases to consider: Handle cases where `n` is a prime number, `k` is larger than the number of factors of `n`, and where `n` is a perfect square.
- Example test cases with explanations: For `n = 12` and `k = 3`, the output should be `4` because the factors of `12` are `1, 2, 3, 4, 6, 12`, and the third factor is `3`. However, in a sorted list of factors, `3` is indeed the third factor but in the sequence of generating factors, we might encounter it differently.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all factors of `n` by checking every number from `1` to `n` to see if it divides `n` without a remainder.
- Step-by-step breakdown of the solution:
  1. Iterate over all numbers from `1` to `n`.
  2. For each number, check if it is a factor of `n` by verifying if `n` modulo the number equals `0`.
  3. If it is a factor, add it to a list of factors.
  4. After checking all numbers, sort the list of factors.
  5. Return the `k`th element in the sorted list of factors.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement without requiring advanced mathematical insights.

```cpp
#include <vector>
#include <algorithm>

int kthFactor(int n, int k) {
    std::vector<int> factors;
    for (int i = 1; i <= n; ++i) {
        if (n % i == 0) {
            factors.push_back(i);
        }
    }
    std::sort(factors.begin(), factors.end());
    if (k > factors.size()) {
        return -1; // or throw an exception
    }
    return factors[k - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the input number. The iteration to find factors takes $O(n)$ time, and sorting the factors takes $O(n \log n)$ time in the worst case.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store all numbers from `1` to `n` in the `factors` vector.
> - **Why these complexities occur:** The brute force approach checks every possible factor and then sorts them, leading to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all numbers up to `n`, we can iterate up to the square root of `n` because a larger factor of `n` must be a multiple of a smaller factor that has already been checked.
- Detailed breakdown of the approach:
  1. Initialize an empty vector to store factors.
  2. Iterate from `1` to the square root of `n`.
  3. For each number `i` in this range, if `n` is divisible by `i`, then both `i` and `n/i` are factors.
  4. Store these factors in the vector, ensuring not to duplicate the square root of `n` if `n` is a perfect square.
  5. Sort the factors and check if `k` is within the range of the number of factors found.
  6. If `k` exceeds the number of factors found, iterate from the square root of `n` down to `1`, checking for factors in the same manner but storing them in reverse order.
- Proof of optimality: This approach is optimal because it minimizes the number of iterations required to find all factors of `n` by leveraging the property that factors come in pairs.

```cpp
#include <vector>
#include <algorithm>
#include <cmath>

int kthFactor(int n, int k) {
    std::vector<int> factors;
    for (int i = 1; i * i <= n; ++i) {
        if (n % i == 0) {
            factors.push_back(i);
            if (i * i != n) {
                factors.push_back(n / i);
            }
        }
    }
    std::sort(factors.begin(), factors.end());
    if (k > factors.size()) {
        return -1; // or throw an exception
    }
    return factors[k - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{n} \log n)$, where the $\sqrt{n}$ comes from iterating up to the square root of `n`, and $\log n$ from sorting the factors.
> - **Space Complexity:** $O(\sqrt{n})$, as we store factors in a vector, and in the worst case, we might store up to $\sqrt{n}$ factors.
> - **Optimality proof:** This is optimal because we minimize the number of iterations by only going up to the square root of `n` and leveraging factor pairs, reducing both time and space complexities significantly compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration optimization, factorization, and sorting.
- Problem-solving patterns identified: Leveraging mathematical properties (factor pairs) to reduce computational complexity.
- Optimization techniques learned: Minimizing iterations by using mathematical insights.
- Similar problems to practice: Finding prime factors, checking for primality, and other factorization-related problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the case when `n` is a perfect square, or failing to sort factors before returning the `k`th one.
- Edge cases to watch for: When `k` exceeds the number of factors of `n`, or when `n` is a prime number.
- Performance pitfalls: Using the brute force approach for large inputs due to its high time complexity.
- Testing considerations: Ensure to test with various inputs, including perfect squares, prime numbers, and large values of `n` and `k`.