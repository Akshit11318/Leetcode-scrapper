## Perfect Number
**Problem Link:** https://leetcode.com/problems/perfect-number/description

**Problem Statement:**
- Input: An integer `num`.
- Constraints: `1 <= num <= 10^8`.
- Expected Output: A boolean indicating whether `num` is a perfect number.
- Key Requirements: A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding the number itself.
- Example Test Cases:
  - Input: `num = 28`
  - Output: `true` (Explanation: `28` is a perfect number since its proper divisors are `1`, `2`, `4`, `7`, `14`, and the sum of these divisors is `28`.)
  - Input: `num = 6`
  - Output: `true` (Explanation: `6` is a perfect number since its proper divisors are `1`, `2`, `3`, and the sum of these divisors is `6`.)
  - Input: `num = 100`
  - Output: `false` (Explanation: The sum of the proper divisors of `100` is `1 + 2 + 4 + 5 + 10 + 20 + 25 + 50 = 117`, which is not equal to `100`.)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every number up to `num` to see if it's a divisor.
- Then, sum up all these divisors and check if the sum equals `num`.
- This approach comes to mind first because it directly implements the definition of a perfect number.

```cpp
class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) return false; // Edge case: numbers less than or equal to 1 are not perfect
        int sum = 1; // Start with 1 since 1 is a divisor of every number
        for (int i = 2; i <= num / 2; i++) { // Only need to check up to num / 2
            if (num % i == 0) {
                sum += i;
                if (i != num / i) sum += num / i; // Add both i and num / i as divisors if they are different
            }
        }
        return sum == num; // Check if the sum of divisors equals num
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{n}{2}) = O(n)$, where $n$ is the input number `num`. This is because in the worst case, we are checking every number up to $\frac{n}{2}$.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the sum and the current divisor.
> - **Why these complexities occur:** The time complexity is linear because we potentially check every number up to $\frac{n}{2}$, and the space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that a larger factor of the number must be a multiple of a smaller factor that has already been checked.
- This means we only need to check up to the square root of `num` for divisors, significantly reducing the number of checks.
- This approach is optimal because it minimizes the number of checks required to find all divisors.

```cpp
class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) return false; // Edge case: numbers less than or equal to 1 are not perfect
        int sum = 1; // Start with 1 since 1 is a divisor of every number
        for (int i = 2; i * i <= num; i++) { // Only need to check up to sqrt(num)
            if (num % i == 0) {
                sum += i;
                if (i * i != num) sum += num / i; // Add both i and num / i as divisors if they are different
            }
        }
        return sum == num; // Check if the sum of divisors equals num
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{n})$, where $n$ is the input number `num`. This is because we are checking up to the square root of `num`.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the sum and the current divisor.
> - **Optimality proof:** This is the best possible complexity because we must at least check up to the square root of `num` to ensure we find all divisors, and this approach does so in the most efficient manner.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include the use of loops to check for divisors and the optimization of only checking up to the square root of a number.
- Problem-solving patterns identified include breaking down a problem into smaller parts (in this case, checking each potential divisor) and optimizing the approach by reducing the number of checks needed.
- Optimization techniques learned include recognizing that larger factors are multiples of smaller factors and thus do not need to be explicitly checked.
- Similar problems to practice include finding prime numbers, checking for divisibility, and optimizing loops.

**Mistakes to Avoid:**
- Common implementation errors include not handling edge cases properly (e.g., numbers less than or equal to 1) and not optimizing the loop to reduce unnecessary checks.
- Edge cases to watch for include numbers that are perfect squares, as their square root is a divisor but should not be counted twice.
- Performance pitfalls include using inefficient algorithms that check every number up to `num` instead of optimizing to check up to the square root of `num`.
- Testing considerations include ensuring the function works correctly for a variety of inputs, including edge cases and both perfect and non-perfect numbers.