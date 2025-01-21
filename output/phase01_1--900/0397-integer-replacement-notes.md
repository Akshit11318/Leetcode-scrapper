## Integer Replacement
**Problem Link:** https://leetcode.com/problems/integer-replacement/description

**Problem Statement:**
- Input: An integer `n`.
- Constraints: $1 \leq n \leq 2^{31} - 1$.
- Expected output: The minimum number of operations required to reduce `n` to 1.
- Key requirements: You can perform two types of operations:
  - If `n` is even, you can divide it by 2.
  - If `n` is odd, you can either add 1 or subtract 1.
- Example test cases:
  - Input: `n = 8`, Output: `3` (Explanation: `8 -> 4 -> 2 -> 1`).
  - Input: `n = 7`, Output: `4` (Explanation: `7 -> 8 -> 4 -> 2 -> 1` or `7 -> 6 -> 3 -> 2 -> 1`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible operations at each step and recursively find the minimum number of operations.
- This approach involves exploring all possible paths from `n` to 1 and counting the number of operations in each path.
- However, this approach is inefficient due to the large number of possible paths.

```cpp
class Solution {
public:
    int integerReplacement(int n) {
        return helper(n);
    }
    
    int helper(int n) {
        if (n == 1) return 0;
        if (n % 2 == 0) return 1 + helper(n / 2);
        return 1 + min(helper(n - 1), helper(n + 1));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the input number. This is because in the worst case, the function makes two recursive calls for each number from `n` down to 1.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible operations at each step, leading to an exponential time complexity and a linear space complexity due to recursion.

---

### Better Approach

There isn't a significantly better intermediate approach than the brute force for this problem. The optimal approach is to observe the pattern and make decisions based on the last two bits of the number.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to observe the pattern of operations and decide whether to add or subtract 1 when `n` is odd based on the last two bits of `n`.
- If `n` ends in `01`, it's optimal to add 1 to make it end in `10`, which can then be divided by 2.
- If `n` ends in `11`, it's optimal to subtract 1 to make it end in `10`, which can then be divided by 2.
- For numbers ending in `00`, we can simply divide by 2.
- For numbers ending in `10`, we can also divide by 2.

```cpp
class Solution {
public:
    int integerReplacement(int n) {
        long long N = n; // To handle the case when n is INT_MAX
        int result = 0;
        while (N > 1) {
            if (N % 2 == 0) {
                N /= 2;
            } else if (N % 4 == 1 || N == 3) {
                N--;
            } else {
                N++;
            }
            result++;
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input number. This is because we perform a constant number of operations for each bit in the binary representation of `n`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to reduce `n` to 1 by making the best decision at each step based on the last two bits of `n`.

---

### Alternative Approach

There isn't a significantly different alternative approach for this problem that offers unique insights or trade-offs.

---

### Final Notes

**Learning Points:**
- The importance of observing patterns and making decisions based on the binary representation of numbers.
- How to optimize recursive solutions by avoiding unnecessary recursive calls.
- The use of bit manipulation to solve problems efficiently.

**Mistakes to Avoid:**
- Not considering the case when `n` is `INT_MAX` and avoiding overflow.
- Not optimizing the solution to reduce the number of operations.
- Not handling edge cases properly.

---