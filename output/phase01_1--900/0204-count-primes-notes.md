## Count Primes
**Problem Link:** https://leetcode.com/problems/count-primes/description

**Problem Statement:**
- Input format: An integer `n` representing the upper limit for finding primes.
- Constraints: `0 <= n <= 5 * 10^6`.
- Expected output format: The number of prime numbers less than `n`.
- Key requirements: Count all prime numbers less than `n`.
- Edge cases: Handle cases where `n` is less than or equal to 1, as there are no prime numbers in this range.

Example test cases:
- Input: `n = 10`
- Output: `4`
- Explanation: The prime numbers less than 10 are 2, 3, 5, and 7.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check each number from 2 up to `n-1` to see if it's prime.
- Step-by-step breakdown:
  1. Iterate over each number `i` from 2 to `n-1`.
  2. For each `i`, check if it's divisible by any number `j` from 2 up to the square root of `i`.
  3. If `i` is not divisible by any `j`, it's a prime number, so increment the count.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
class Solution {
public:
    int countPrimes(int n) {
        int count = 0;
        for (int i = 2; i < n; i++) {
            bool isPrime = true;
            for (int j = 2; j * j <= i; j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \sqrt{n})$, where $n$ is the input number. This is because for each number up to `n`, we potentially check divisibility up to its square root.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the count and loop variables.
> - **Why these complexities occur:** The nested loops structure causes the time complexity to be quadratic in relation to the square root of `n`, and the space complexity is constant because we don't use any data structures that scale with `n`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use the Sieve of Eratosthenes algorithm, which is an efficient method for finding all primes smaller than `n`.
- Detailed breakdown:
  1. Create a boolean array `isPrime` of size `n`, initialized with all `true` values.
  2. Iterate from 2 to the square root of `n`. For each prime `p` in this range, mark as `false` all the multiples of `p` in the `isPrime` array.
  3. Count the number of `true` values in the `isPrime` array, excluding the first two elements (0 and 1), as these are not prime.
- Proof of optimality: The Sieve of Eratosthenes has a time complexity of $O(n \log \log n)$, which is more efficient than the brute force approach for large `n`.

```cpp
class Solution {
public:
    int countPrimes(int n) {
        if (n <= 2) return 0;
        
        vector<bool> isPrime(n, true);
        isPrime[0] = isPrime[1] = false;
        
        for (int i = 2; i * i < n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) count++;
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log \log n)$, as the Sieve of Eratosthenes algorithm iterates over the numbers up to `n`, and for each prime, it marks its multiples, which results in this time complexity.
> - **Space Complexity:** $O(n)$, because we use a boolean array of size `n` to keep track of prime numbers.
> - **Optimality proof:** The Sieve of Eratosthenes is optimal for finding all primes up to `n` because it only requires a single pass through the numbers up to the square root of `n` to mark all non-prime numbers, resulting in the most efficient known algorithm for this problem.

---

### Final Notes

**Learning Points:**
- The Sieve of Eratosthenes is an efficient algorithm for finding all primes smaller than a given number `n`.
- Understanding the time and space complexities of algorithms is crucial for optimizing solutions.
- The brute force approach, while straightforward, is often less efficient than specialized algorithms like the Sieve of Eratosthenes.

**Mistakes to Avoid:**
- Not considering the constraints of the problem, such as the range of `n`, which can lead to inefficient solutions.
- Not optimizing the solution for large inputs, which can result in timeouts or incorrect results due to excessive computation time.
- Failing to handle edge cases, such as when `n` is less than or equal to 1, which requires returning 0 as there are no prime numbers in this range.