## Three Divisors
**Problem Link:** https://leetcode.com/problems/three-divisors/description

**Problem Statement:**
- Input: An integer `n`.
- Output: Whether `n` has exactly three distinct positive divisors.
- Key requirements and edge cases to consider:
  - Handle the case where `n` is less than or equal to 1.
  - Identify the condition for a number to have exactly three divisors.
- Example test cases:
  - Input: `n = 2` - Output: `true` because the divisors of 2 are 1 and 2.
  - Input: `n = 4` - Output: `false` because the divisors of 4 are 1, 2, and 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check all numbers up to `n` to see if they are divisors of `n`.
- Step-by-step breakdown:
  1. Initialize a counter for divisors.
  2. Iterate from 1 to `n`.
  3. For each number, check if it is a divisor of `n`.
  4. If it is, increment the counter.
  5. After the loop, check if the counter equals 3.

```cpp
bool isThree(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) count++;
    }
    return count == 3;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we potentially check every number up to `n`.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Why these complexities occur:** The brute force approach checks every possible divisor, leading to linear time complexity, but it uses constant space since the space usage does not grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: A number has exactly three divisors if and only if it is the square of a prime number. This is because the only divisors of the square of a prime `p` are 1, `p`, and `p^2`.
- Detailed breakdown:
  1. Check if `n` is less than or equal to 1, in which case it cannot have three divisors.
  2. Check if `n` is a perfect square.
  3. If it is, find the square root of `n`.
  4. Check if the square root is a prime number.
  5. If it is prime, then `n` has exactly three divisors.

```cpp
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

bool isThree(int n) {
    if (n <= 1) return false;
    int sqrtN = sqrt(n);
    return sqrtN * sqrtN == n && isPrime(sqrtN);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{n})$ due to the prime check in the worst case.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it directly checks the necessary condition (being the square of a prime) without unnecessary iterations, making it more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Checking for prime numbers and perfect squares.
- Problem-solving patterns identified: Using mathematical properties to simplify a problem.
- Optimization techniques learned: Reducing the number of iterations by applying mathematical insights.

**Mistakes to Avoid:**
- Not considering the mathematical properties of numbers (e.g., the relationship between perfect squares and prime numbers).
- Failing to optimize the algorithm by not reducing the number of iterations based on the problem's constraints.
- Not handling edge cases properly (e.g., numbers less than or equal to 1).