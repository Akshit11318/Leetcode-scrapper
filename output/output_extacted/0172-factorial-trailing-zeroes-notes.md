## Factorial Trailing Zeroes

**Problem Link:** https://leetcode.com/problems/factorial-trailing-zeroes/description

**Problem Statement:**
- Input: An integer `n` representing the input number.
- Output: The number of trailing zeroes in `n!`.
- Key requirements and edge cases: The input `n` is guaranteed to be a non-negative integer, and the output should be an integer representing the number of trailing zeroes in `n!`.
- Example test cases:
  - Input: `n = 3`
  - Output: `0`
  - Explanation: `3! = 6`, which has no trailing zeroes.
  - Input: `n = 5`
  - Output: `1`
  - Explanation: `5! = 120`, which has one trailing zero.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate `n!` and count the trailing zeroes.
- Step-by-step breakdown:
  1. Calculate `n!` using a loop or recursive function.
  2. Convert `n!` to a string.
  3. Count the trailing zeroes in the string representation of `n!`.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solve the problem.

```cpp
class Solution {
public:
    int trailingZeroes(int n) {
        long long factorial = 1;
        for (int i = 1; i <= n; i++) {
            factorial *= i;
        }
        int count = 0;
        while (factorial % 10 == 0) {
            count++;
            factorial /= 10;
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input number. This is because we are calculating `n!` using a loop.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the variables.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we are using a loop to calculate `n!`, and the space complexity is $O(1)$ because we are not using any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that trailing zeroes in `n!` are caused by the multiplication of 2 and 5, as $10 = 2 \times 5$.
- Since there are always more factors of 2 than 5 in `n!`, we only need to count the factors of 5.
- Detailed breakdown:
  1. Initialize a variable `count` to store the number of trailing zeroes.
  2. Use a loop to calculate the factors of 5 in `n!`.
  3. In each iteration, divide `n` by the current power of 5 and add the result to `count`.
- Proof of optimality: This approach is optimal because it directly counts the factors of 5 in `n!`, which is the bottleneck for trailing zeroes.

```cpp
class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        int i = 5;
        while (n / i >= 1) {
            count += n / i;
            i *= 5;
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input number. This is because we are using a loop that divides `n` by increasing powers of 5.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it directly counts the factors of 5 in `n!`, which is the bottleneck for trailing zeroes.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the importance of understanding the underlying mathematics of a problem.
- The problem-solving pattern identified is to look for the bottleneck or limiting factor in a problem.
- The optimization technique learned is to directly count the factors of 5 in `n!` instead of calculating `n!` and counting the trailing zeroes.

**Mistakes to Avoid:**
- A common implementation error is to use a brute force approach that calculates `n!` and counts the trailing zeroes, which can lead to overflow and performance issues.
- An edge case to watch for is when `n` is 0, in which case the output should be 0.
- A performance pitfall is to use a recursive function to calculate `n!`, which can lead to stack overflow and performance issues.