## Prime Arrangements
**Problem Link:** https://leetcode.com/problems/prime-arrangements/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, return the number of ways to arrange the numbers in the range `[1, n]` such that all the prime numbers are at odd positions (1-indexed).
- Expected output format: The number of ways to arrange the numbers.
- Key requirements and edge cases to consider: The input `n` will be in the range `[1, 100]`.
- Example test cases with explanations:
  - For `n = 4`, there are 2 ways to arrange the numbers: `[2, 1, 3, 4]` and `[2, 3, 1, 4]`.
  - For `n = 5`, there are 2 ways to arrange the numbers: `[2, 1, 3, 4, 5]` and `[2, 3, 1, 4, 5]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of numbers from 1 to `n` and check if the prime numbers are at odd positions.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of numbers from 1 to `n`.
  2. For each permutation, check if the prime numbers are at odd positions.
  3. Count the number of valid permutations.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible arrangements.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

bool isPrime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return false;
    }
    return true;
}

void permute(std::vector<int>& nums, int start, int end, int& count) {
    if (start == end) {
        bool valid = true;
        for (int i = 0; i < nums.size(); i++) {
            if (isPrime(nums[i]) && (i + 1) % 2 == 0) {
                valid = false;
                break;
            }
        }
        if (valid) count++;
    } else {
        for (int i = start; i <= end; i++) {
            std::swap(nums[start], nums[i]);
            permute(nums, start + 1, end, count);
            std::swap(nums[start], nums[i]);
        }
    }
}

int numPrimeArrangements(int n) {
    std::vector<int> nums(n);
    for (int i = 0; i < n; i++) nums[i] = i + 1;
    int count = 0;
    permute(nums, 0, n - 1, count);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n!$ is the number of permutations and $n$ is the time complexity of checking if a number is prime.
> - **Space Complexity:** $O(n)$, where $n$ is the space required to store the permutation.
> - **Why these complexities occur:** The brute force approach generates all permutations of numbers from 1 to `n` and checks if the prime numbers are at odd positions, resulting in a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Count the number of prime numbers and non-prime numbers separately, and then calculate the number of ways to arrange them.
- Detailed breakdown of the approach:
  1. Count the number of prime numbers and non-prime numbers in the range `[1, n]`.
  2. Calculate the number of ways to arrange the prime numbers at odd positions.
  3. Calculate the number of ways to arrange the non-prime numbers at even positions.
  4. Return the product of the two arrangements.
- Proof of optimality: This approach has a much lower time complexity than the brute force approach and correctly calculates the number of ways to arrange the numbers.

```cpp
#include <iostream>

int numPrimeArrangements(int n) {
    int primes = 0;
    for (int i = 2; i <= n; i++) {
        bool isPrime = true;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) primes++;
    }
    int nonPrimes = n - primes;
    long long primeArrangements = 1;
    for (int i = 2; i <= primes; i++) primeArrangements *= i;
    long long nonPrimeArrangements = 1;
    for (int i = 2; i <= nonPrimes; i++) nonPrimeArrangements *= i;
    return (int)(primeArrangements * nonPrimeArrangements);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \sqrt{n})$, where $n$ is the time complexity of checking if a number is prime and $\sqrt{n}$ is the time complexity of the inner loop.
> - **Space Complexity:** $O(1)$, where the space complexity is constant.
> - **Optimality proof:** This approach has a much lower time complexity than the brute force approach and correctly calculates the number of ways to arrange the numbers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Permutations, prime numbers, and factorials.
- Problem-solving patterns identified: Counting and arrangement problems.
- Optimization techniques learned: Reducing time complexity by using mathematical formulas instead of brute force approaches.
- Similar problems to practice: Permutation and combination problems, prime number problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the number of prime numbers or non-prime numbers.
- Edge cases to watch for: Handling the case where `n` is 1 or 2.
- Performance pitfalls: Using a brute force approach for large inputs.
- Testing considerations: Testing the function with different inputs to ensure correctness.