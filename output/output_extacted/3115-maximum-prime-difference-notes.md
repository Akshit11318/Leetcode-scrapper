## Maximum Prime Difference
**Problem Link:** https://leetcode.com/problems/maximum-prime-difference/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, find the maximum difference between two primes in the range `[2, n]`.
- Expected output format: The maximum difference between two primes.
- Key requirements and edge cases to consider:
  - Handle cases where `n` is less than 2.
  - Identify prime numbers in the given range.
  - Calculate differences between all pairs of primes.
- Example test cases with explanations:
  - For `n = 10`, the primes are 2, 3, 5, 7. The maximum difference is 7 - 2 = 5.
  - For `n = 15`, the primes are 2, 3, 5, 7, 11, 13. The maximum difference is 13 - 2 = 11.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all numbers in the range `[2, n]`, check if each number is prime, and then calculate the difference between all pairs of primes.
- Step-by-step breakdown of the solution:
  1. Create a function to check if a number is prime.
  2. Iterate over the range `[2, n]` and filter out non-prime numbers.
  3. Calculate the differences between all pairs of primes.
  4. Find the maximum difference.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each number for primality and calculating differences between primes.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

bool isPrime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i * i <= num; ++i) {
        if (num % i == 0) return false;
    }
    return true;
}

int maxPrimeDifference(int n) {
    std::vector<int> primes;
    for (int i = 2; i <= n; ++i) {
        if (isPrime(i)) primes.push_back(i);
    }
    int maxDiff = 0;
    for (int i = 0; i < primes.size(); ++i) {
        for (int j = i + 1; j < primes.size(); ++j) {
            maxDiff = std::max(maxDiff, primes[j] - primes[i]);
        }
    }
    return maxDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot \sqrt{n})$ due to the nested loops for checking primality and calculating differences.
> - **Space Complexity:** $O(n)$ for storing prime numbers.
> - **Why these complexities occur:** The brute force approach involves checking each number for primality, which has a time complexity of $O(\sqrt{n})$, and then comparing each pair of primes, leading to $O(n^2)$ complexity for the comparisons.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every number for primality and then comparing pairs, we can use the Sieve of Eratosthenes algorithm to efficiently find all primes up to `n`, and then simply find the maximum and minimum primes to calculate the maximum difference.
- Detailed breakdown of the approach:
  1. Implement the Sieve of Eratosthenes to find all primes up to `n`.
  2. Find the maximum and minimum primes in the set of primes.
  3. Calculate the maximum difference as the difference between the maximum and minimum primes.
- Proof of optimality: This approach is optimal because it uses the most efficient known algorithm for finding all primes up to a given number (Sieve of Eratosthenes) and then calculates the maximum difference in linear time.

```cpp
#include <iostream>
#include <vector>

int maxPrimeDifference(int n) {
    std::vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i * i <= n; ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    int minPrime = -1, maxPrime = -1;
    for (int i = 2; i <= n; ++i) {
        if (isPrime[i]) {
            if (minPrime == -1) minPrime = i;
            maxPrime = i;
        }
    }
    return maxPrime - minPrime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log \log n)$ due to the Sieve of Eratosthenes.
> - **Space Complexity:** $O(n)$ for the sieve.
> - **Optimality proof:** This approach is optimal because it uses the most efficient algorithm for finding primes and then calculates the maximum difference in linear time, resulting in a significant improvement over the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sieve of Eratosthenes, efficient prime number generation.
- Problem-solving patterns identified: Using known efficient algorithms for sub-problems.
- Optimization techniques learned: Avoiding unnecessary computations by using the most efficient algorithms for sub-problems.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables, incorrect loop bounds.
- Edge cases to watch for: Handling cases where `n` is less than 2.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Ensure to test with various inputs, including edge cases.