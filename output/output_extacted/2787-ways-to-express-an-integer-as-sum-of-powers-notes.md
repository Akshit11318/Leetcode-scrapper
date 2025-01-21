# Ways to Express an Integer as Sum of Powers
**Problem Link:** https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, find the number of ways to express it as a sum of powers of 3.
- Expected output format: The number of ways to express `n` as a sum of powers of 3.
- Key requirements and edge cases to consider: The integer `n` can range from 1 to 10^9, and we need to handle cases where `n` is not a power of 3.
- Example test cases with explanations:
  - If `n = 3`, there is only one way to express it as a sum of powers of 3, which is `3^1`.
  - If `n = 4`, there are two ways to express it as a sum of powers of 3, which are `3^0 + 3^1` and `3^2`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to try all possible combinations of powers of 3 and count the ones that sum up to `n`.
- Step-by-step breakdown of the solution:
  1. Initialize a counter to store the number of ways to express `n` as a sum of powers of 3.
  2. Iterate over all possible powers of 3, from `3^0` to `3^k`, where `k` is the largest integer such that `3^k` is less than or equal to `n`.
  3. For each power of 3, recursively try all possible combinations of powers of 3 that sum up to `n`.
  4. If a combination sums up to `n`, increment the counter.
- Why this approach comes to mind first: This approach is intuitive because it tries all possible combinations of powers of 3, which guarantees finding all possible ways to express `n` as a sum of powers of 3.

```cpp
int powerSum(int n, int i, int currSum) {
    if (currSum > n) return 0;
    if (currSum == n) return 1;
    int result = powerSum(n, i + 1, currSum);
    result += powerSum(n, i + 1, currSum + pow(3, i));
    return result;
}

int powerSum(int n) {
    return powerSum(n, 0, 0);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the input integer. This is because in the worst case, we try all possible combinations of powers of 3.
> - **Space Complexity:** $O(n)$, where $n$ is the input integer. This is because of the recursive call stack.
> - **Why these complexities occur:** The brute force approach has high time complexity because it tries all possible combinations of powers of 3, which can be exponential in the size of the input. The space complexity is high because of the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The key insight is that each number can be represented as a sum of powers of 3 using a **_base 3_** representation.
- Detailed breakdown of the approach:
  1. Convert the input integer `n` to a **_base 3_** representation.
  2. Initialize a counter to store the number of ways to express `n` as a sum of powers of 3.
  3. Iterate over each digit in the **_base 3_** representation.
  4. For each digit, if it is greater than 1, increment the counter by the number of ways to express the remaining digits as a sum of powers of 3.
- Proof of optimality: This approach is optimal because it uses the **_base 3_** representation, which is the most efficient way to represent numbers as a sum of powers of 3.
- Why further optimization is impossible: Further optimization is impossible because we are already using the most efficient representation, which is the **_base 3_** representation.

```cpp
int powerSum(int n) {
    int result = 1;
    while (n > 0) {
        if (n % 3 == 2) result *= 2;
        n /= 3;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, where $n$ is the input integer. This is because we iterate over the digits of the **_base 3_** representation of `n`.
> - **Space Complexity:** $O(1)$, where $n$ is the input integer. This is because we only use a constant amount of space to store the result.
> - **Optimality proof:** The optimal approach has a time complexity of $O(log(n))$ because we iterate over the digits of the **_base 3_** representation of `n`, which has $log(n)$ digits. The space complexity is $O(1)$ because we only use a constant amount of space to store the result.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: **_base 3_** representation, recursive functions, and dynamic programming.
- Problem-solving patterns identified: using a more efficient representation to solve a problem.
- Optimization techniques learned: using a **_base 3_** representation to reduce the time complexity.
- Similar problems to practice: problems involving **_base 2_** or **_base 10_** representations.

**Mistakes to Avoid:**
- Common implementation errors: not handling the case where `n` is not a power of 3.
- Edge cases to watch for: `n` being 0 or 1.
- Performance pitfalls: using a brute force approach that tries all possible combinations of powers of 3.
- Testing considerations: testing the function with different inputs, including edge cases.