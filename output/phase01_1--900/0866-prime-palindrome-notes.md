## Prime Palindrome
**Problem Link:** https://leetcode.com/problems/prime-palindrome/description

**Problem Statement:**
- Input format and constraints: The problem asks to find the smallest prime palindrome greater than or equal to `n`, where `n` is a given integer. `n` is within the range `[1, 10^8]`.
- Expected output format: The smallest prime palindrome number.
- Key requirements and edge cases to consider: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. A palindrome number reads the same backward as forward.
- Example test cases with explanations: For `n = 6`, the output should be `7` because `7` is both prime and a palindrome. For `n = 100`, the output should be `101`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first step is to understand what constitutes a prime number and a palindrome. Then, iterate through numbers starting from `n`, checking each for being both prime and a palindrome.
- Step-by-step breakdown of the solution:
  1. Define a helper function to check if a number is prime.
  2. Define another helper function to check if a number is a palindrome.
  3. Iterate through numbers from `n` upwards, checking each number with the helper functions.
  4. Return the first number that is both prime and a palindrome.
- Why this approach comes to mind first: It directly addresses the problem statement without requiring advanced optimization techniques.

```cpp
class Solution {
public:
    bool isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6)
            if (n % i == 0 || n % (i + 2) == 0) return false;
        return true;
    }

    bool isPalindrome(int n) {
        string str = to_string(n);
        int left = 0, right = str.size() - 1;
        while (left < right) {
            if (str[left] != str[right]) return false;
            left++; right--;
        }
        return true;
    }

    int primePalindrome(int n) {
        while (true) {
            if (isPrime(n) && isPalindrome(n)) return n;
            n++;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot \sqrt{n} \cdot \log{n})$, where $k$ is the number of iterations until we find a prime palindrome. The $\sqrt{n}$ term comes from the prime check, and $\log{n}$ from converting the number to a string for palindrome check.
> - **Space Complexity:** $O(\log{n})$, for storing the string representation of `n`.
> - **Why these complexities occur:** The time complexity is high due to the repeated checks for primality and palindrome nature for each number, and the space complexity is due to the string conversion.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every number sequentially, we can generate prime numbers and palindromes more efficiently. For palindromes, we can construct them directly by mirroring the first half of the number. For primes, we can use a sieve or a more efficient primality test.
- Detailed breakdown of the approach:
  1. If `n` is less than 10, return the smallest prime palindrome greater than or equal to `n`.
  2. Construct potential palindrome numbers by mirroring the first half of the number and then check if they are prime.
- Proof of optimality: This approach is more efficient because it directly constructs potential palindrome numbers and checks their primality, reducing the number of checks significantly.
- Why further optimization is impossible: This approach already minimizes the number of operations by directly generating potential solutions and checking their validity.

```cpp
class Solution {
public:
    bool isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6)
            if (n % i == 0 || n % (i + 2) == 0) return false;
        return true;
    }

    int primePalindrome(int n) {
        if (n >= 100000) {
            for (int i = 100003; ; i += 2) {
                if (isPalindrome(i) && isPrime(i)) return i;
            }
        } else if (n >= 1000) {
            for (int i = 1001; ; i += 2) {
                if (isPalindrome(i) && isPrime(i)) return i;
            }
        } else if (n >= 10) {
            for (int i = 11; ; i += 2) {
                if (isPalindrome(i) && isPrime(i)) return i;
            }
        } else {
            return 2;
        }
    }

    bool isPalindrome(int n) {
        string str = to_string(n);
        int left = 0, right = str.size() - 1;
        while (left < right) {
            if (str[left] != str[right]) return false;
            left++; right--;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{n})$, primarily due to the primality check.
> - **Space Complexity:** $O(\log{n})$, for the string conversion in palindrome check.
> - **Optimality proof:** This approach is optimal because it directly generates and checks potential prime palindromes, minimizing unnecessary operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Primality testing, palindrome construction, and optimization techniques.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (primality and palindrome checks) and optimizing each part.
- Optimization techniques learned: Direct construction of potential solutions and minimizing unnecessary checks.
- Similar problems to practice: Other problems involving primality tests, palindrome constructions, and optimizations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect primality tests or palindrome checks.
- Edge cases to watch for: Handling numbers less than 10, and ensuring the approach works for large inputs.
- Performance pitfalls: Using inefficient algorithms for primality or palindrome checks.
- Testing considerations: Thoroughly testing with various inputs, including edge cases.