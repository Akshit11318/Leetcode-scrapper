## Happy Number

**Problem Link:** [https://leetcode.com/problems/happy-number/description](https://leetcode.com/problems/happy-number/description)

**Problem Statement:**
- Input format: An integer `n`.
- Constraints: $1 \leq n \leq 2^{31} - 1$.
- Expected output format: A boolean indicating whether `n` is a happy number.
- Key requirements: A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
- Example test cases:
  - Input: `n = 19`
    - Explanation: 
      1. Square and sum of digits: $1^2 + 9^2 = 82$
      2. Square and sum of digits: $8^2 + 2^2 = 68$
      3. Square and sum of digits: $6^2 + 8^2 = 100$
      4. Square and sum of digits: $1^2 + 0^2 + 0^2 = 1$
    - Output: `true`
  - Input: `n = 20`
    - Explanation: 
      1. Square and sum of digits: $2^2 + 0^2 = 4$
      2. Square and sum of digits: $4^2 = 16$
      3. Square and sum of digits: $1^2 + 6^2 = 37$
      4. Square and sum of digits: $3^2 + 7^2 = 58$
      5. Square and sum of digits: $5^2 + 8^2 = 89$
      6. Square and sum of digits: $8^2 + 9^2 = 145$
      7. Square and sum of digits: $1^2 + 4^2 + 5^2 = 42$
      8. Square and sum of digits: $4^2 + 2^2 = 20$
      - This enters a cycle that doesn't include 1.
    - Output: `false`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to continuously apply the process of squaring and summing the digits of a number until it reaches 1 or a cycle is detected.
- However, the brute force approach doesn't efficiently detect cycles, leading to potential infinite loops.

```cpp
bool isHappy(int n) {
    while (n != 1) {
        int sum = 0;
        while (n) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        n = sum;
        // No cycle detection, potentially leading to infinite loop.
    }
    return true; // If it reaches 1, it's happy.
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\infty)$ in the worst case due to the lack of cycle detection, which can lead to an infinite loop.
> - **Space Complexity:** $O(1)$, as it only uses a constant amount of space.
> - **Why these complexities occur:** The brute force approach doesn't account for the possibility of entering a cycle that doesn't include 1, leading to an infinite loop.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight to the optimal solution is recognizing that a number is happy if and only if it eventually reaches 1. If it doesn't reach 1, it must enter a cycle.
- To detect cycles efficiently, we can use a `unordered_set` to store the numbers we've seen. If we encounter a number that's already in the set, we know we've entered a cycle, and the number is not happy.

```cpp
#include <unordered_set>

bool isHappy(int n) {
    std::unordered_set<int> seen;
    while (n != 1 && seen.find(n) == seen.end()) {
        seen.insert(n);
        int sum = 0;
        while (n) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        n = sum;
    }
    return n == 1; // Returns true if n is 1 (happy), false otherwise.
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log n)$, because the number of digits in `n` (and thus the number of iterations) is proportional to the logarithm of `n`.
> - **Space Complexity:** $O(log n)$, as in the worst case, we might store all the numbers in the sequence until we reach 1 or detect a cycle.
> - **Optimality proof:** This is optimal because we must at least read the input and perform the necessary calculations to determine if a number is happy. The use of an `unordered_set` for cycle detection is efficient, with an average time complexity of $O(1)$ for insertions and lookups.

---

### Final Notes

**Learning Points:**
- The importance of cycle detection in iterative algorithms.
- The use of `unordered_set` for efficient storage and lookup of unique elements.
- Understanding the definition of a happy number and its implications for algorithm design.

**Mistakes to Avoid:**
- Not considering the possibility of cycles in iterative processes.
- Failing to optimize cycle detection, potentially leading to inefficient algorithms.
- Not validating the input or handling edge cases properly.