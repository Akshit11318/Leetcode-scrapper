## Smallest Integer Divisible by K
**Problem Link:** https://leetcode.com/problems/smallest-integer-divisible-by-k/description

**Problem Statement:**
- Input: An integer `k`.
- Constraints: `1 <= k <= 1000`.
- Expected Output: The smallest positive integer `x` such that `x` is divisible by `k`.
- Key Requirements and Edge Cases:
  - `k` will always be a positive integer.
  - The solution should handle the case where `k` is a prime number.
- Example Test Cases:
  - For `k = 1`, the output should be `1`.
  - For `k = 2`, the output should be `2`.
  - For `k = 3`, the output should be `3`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to start from `1` and check each number to see if it's divisible by `k`.
- We increment the number until we find one that is divisible by `k`.
- This approach comes to mind first because it directly addresses the problem statement.

```cpp
class Solution {
public:
    int smallestRepunitDivByK(int k) {
        int num = 1;
        int length = 1;
        while (true) {
            if (num % k == 0) return length;
            num = (num * 10 + 1) % k;
            length++;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, because in the worst case, we might have to check up to `k` numbers.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is due to the potential number of iterations in the while loop, and the space complexity is due to the minimal use of variables.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to recognize that the sequence of numbers we're checking forms a pattern that relates to the properties of `k`.
- Specifically, we can observe that if `k` is a factor of a number in the sequence `1, 11, 111, ...`, then it will also be a factor of the sum of that sequence up to a certain point.
- However, upon closer inspection, the provided brute force solution actually implements an efficient algorithm by utilizing the properties of modular arithmetic to avoid unnecessary computations.

```cpp
class Solution {
public:
    int smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) return -1; // Added early return for optimization
        int num = 1;
        int length = 1;
        while (true) {
            if (num % k == 0) return length;
            num = (num * 10 + 1) % k;
            length++;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, because in the worst case, we still might have to check up to `k` numbers, but the algorithm is optimized to terminate as soon as it finds a number divisible by `k`.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store our variables.
> - **Optimality proof:** This is the best possible complexity because we must at least check each potential remainder once to ensure we find the smallest integer divisible by `k`. The optimization of returning early when `k` is divisible by `2` or `5` improves practical performance but does not change the worst-case time complexity.

---

### Final Notes

**Learning Points:**
- The importance of recognizing patterns in sequences.
- Utilizing modular arithmetic to optimize computations.
- Early returns can significantly improve performance in certain cases.

**Mistakes to Avoid:**
- Not considering the properties of `k` that could simplify the computation.
- Failing to optimize the algorithm with early returns for special cases.
- Not understanding the implications of modular arithmetic in reducing unnecessary computations.