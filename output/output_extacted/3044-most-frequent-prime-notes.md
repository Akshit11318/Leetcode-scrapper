## Most Frequent Prime
**Problem Link:** https://leetcode.com/problems/most-frequent-prime/description

**Problem Statement:**
- Input: An integer `n`.
- Constraints: `1 <= n <= 10^6`.
- Expected Output: The most frequent prime number in the range `[2, n]`.
- Key Requirements: 
    1. Identify prime numbers in the given range.
    2. Count the frequency of each prime number.
    3. Determine the prime number with the highest frequency.
- Edge Cases: 
    1. If `n` is less than 2, return -1 since there are no prime numbers in the range.
    2. If there are multiple prime numbers with the same highest frequency, return the smallest one.
- Example Test Cases:
    1. Input: `n = 10`, Output: `2` (Explanation: Prime numbers in the range [2, 10] are 2, 3, 5, 7. The frequency of each prime number is 1, so the smallest prime number is returned.)
    2. Input: `n = 100`, Output: `2` (Explanation: Prime numbers in the range [2, 100] are 2, 3, 5, 7, 11, ..., 97. The frequency of each prime number is 1, so the smallest prime number is returned.)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all prime numbers up to `n` and count their frequencies.
- Step-by-step breakdown:
    1. Create a boolean array `isPrime` of size `n+1` to mark prime numbers.
    2. Iterate through the array and mark multiples of each prime number as non-prime.
    3. Count the frequency of each prime number.
    4. Determine the prime number with the highest frequency.
- Why this approach comes to mind first: It is a straightforward method to solve the problem, but it is not efficient for large inputs.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int mostFrequentPrime(int n) {
    if (n < 2) return -1;
    
    std::vector<bool> isPrime(n+1, true);
    isPrime[0] = isPrime[1] = false;
    
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    std::unordered_map<int, int> primeFrequency;
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) {
            primeFrequency[i]++;
        }
    }
    
    int maxFrequency = 0;
    int mostFrequentPrime = -1;
    for (const auto& pair : primeFrequency) {
        if (pair.second > maxFrequency) {
            maxFrequency = pair.second;
            mostFrequentPrime = pair.first;
        }
    }
    
    return mostFrequentPrime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log \log n)$ (Explanation: The time complexity is dominated by the prime number generation algorithm, which has a time complexity of $O(n \log \log n)$. The frequency counting and maximum frequency determination have a time complexity of $O(n)$, which is dominated by the prime number generation.)
> - **Space Complexity:** $O(n)$ (Explanation: The space complexity is dominated by the boolean array `isPrime` and the unordered map `primeFrequency`, both of which have a size of $O(n)$.)
> - **Why these complexities occur:** The time complexity occurs because the prime number generation algorithm iterates through the array and marks multiples of each prime number as non-prime. The space complexity occurs because the algorithm uses a boolean array and an unordered map to store the prime numbers and their frequencies.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use the Sieve of Eratosthenes algorithm to generate prime numbers, which has a time complexity of $O(n \log \log n)$.
- Detailed breakdown:
    1. Create a boolean array `isPrime` of size `n+1` to mark prime numbers.
    2. Use the Sieve of Eratosthenes algorithm to generate prime numbers.
    3. Count the frequency of each prime number.
    4. Determine the prime number with the highest frequency.
- Proof of optimality: The Sieve of Eratosthenes algorithm is the most efficient algorithm for generating prime numbers up to a given number, with a time complexity of $O(n \log \log n)$. The frequency counting and maximum frequency determination have a time complexity of $O(n)$, which is dominated by the prime number generation.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int mostFrequentPrime(int n) {
    if (n < 2) return -1;
    
    std::vector<bool> isPrime(n+1, true);
    isPrime[0] = isPrime[1] = false;
    
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    std::unordered_map<int, int> primeFrequency;
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) {
            primeFrequency[i]++;
        }
    }
    
    int maxFrequency = 0;
    int mostFrequentPrime = -1;
    for (const auto& pair : primeFrequency) {
        if (pair.second > maxFrequency) {
            maxFrequency = pair.second;
            mostFrequentPrime = pair.first;
        } else if (pair.second == maxFrequency) {
            mostFrequentPrime = std::min(mostFrequentPrime, pair.first);
        }
    }
    
    return mostFrequentPrime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log \log n)$ (Explanation: The time complexity is dominated by the Sieve of Eratosthenes algorithm, which has a time complexity of $O(n \log \log n)$. The frequency counting and maximum frequency determination have a time complexity of $O(n)$, which is dominated by the prime number generation.)
> - **Space Complexity:** $O(n)$ (Explanation: The space complexity is dominated by the boolean array `isPrime` and the unordered map `primeFrequency`, both of which have a size of $O(n)$.)
> - **Optimality proof:** The Sieve of Eratosthenes algorithm is the most efficient algorithm for generating prime numbers up to a given number, with a time complexity of $O(n \log \log n)$. The frequency counting and maximum frequency determination have a time complexity of $O(n)$, which is dominated by the prime number generation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Sieve of Eratosthenes, frequency counting, maximum frequency determination.
- Problem-solving patterns: Using efficient algorithms to solve problems, optimizing solutions by reducing time and space complexity.
- Optimization techniques: Using the Sieve of Eratosthenes algorithm to generate prime numbers, reducing the time complexity of the solution.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the boolean array `isPrime` correctly, not using the Sieve of Eratosthenes algorithm to generate prime numbers.
- Edge cases to watch for: Handling the case where `n` is less than 2, handling the case where there are multiple prime numbers with the same highest frequency.
- Performance pitfalls: Using inefficient algorithms to generate prime numbers, not optimizing the solution to reduce time and space complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure that it works correctly and efficiently.