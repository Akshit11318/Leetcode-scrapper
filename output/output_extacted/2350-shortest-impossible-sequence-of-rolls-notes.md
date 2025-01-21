## Shortest Impossible Sequence of Rolls

**Problem Link:** https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/description

**Problem Statement:**
- Input: `n` (the number of rolls) and `k` (the number of sides on each die)
- Output: The length of the shortest sequence that cannot be obtained by rolling `n` dice with `k` sides each
- Key requirements: The sequence should be as short as possible and impossible to obtain
- Example test cases:
  - Input: `n = 2`, `k = 6`, Output: `7` (because the sequence `7` cannot be obtained by rolling two 6-sided dice)
  - Input: `n = 3`, `k = 6`, Output: `10` (because the sequence `10` cannot be obtained by rolling three 6-sided dice)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible sequences of rolls and check if they can be obtained by rolling `n` dice with `k` sides each.
- We start by generating all possible sequences of length `1`, then `2`, and so on, until we find a sequence that cannot be obtained.
- This approach comes to mind first because it is straightforward and easy to understand.

```cpp
class Solution {
public:
    int shortestSequence(int n, int k) {
        int maxSum = n * k;
        for (int len = 1; len <= maxSum; len++) {
            bool found = false;
            for (int i = 1; i <= maxSum - len + 1; i++) {
                bool seqFound = true;
                for (int j = 0; j < len; j++) {
                    bool rollFound = false;
                    for (int roll = 1; roll <= k; roll++) {
                        if (i + j + roll - 1 <= maxSum) {
                            rollFound = true;
                            break;
                        }
                    }
                    if (!rollFound) {
                        seqFound = false;
                        break;
                    }
                }
                if (seqFound) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                return len;
            }
        }
        return -1; // should not reach here
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k \cdot (n \cdot k)^2)$ (because we generate all possible sequences and check if they can be obtained by rolling `n` dice with `k` sides each)
> - **Space Complexity:** $O(1)$ (because we only use a constant amount of space to store the variables)
> - **Why these complexities occur:** The time complexity is high because we generate all possible sequences, and the space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a mathematical formula to calculate the length of the shortest sequence that cannot be obtained by rolling `n` dice with `k` sides each.
- The formula is based on the fact that the number of possible sequences of length `len` is `k^n`, and the number of possible sums is `n * k`.
- We can calculate the length of the shortest sequence that cannot be obtained by finding the smallest `len` such that `k^n > len * (n * k)`.
- This approach is optimal because it uses a mathematical formula to calculate the length of the shortest sequence, rather than generating all possible sequences.

```cpp
class Solution {
public:
    int shortestSequence(int n, int k) {
        return n * k - n + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ (because we only use a constant amount of time to calculate the length of the shortest sequence)
> - **Space Complexity:** $O(1)$ (because we only use a constant amount of space to store the variables)
> - **Optimality proof:** This approach is optimal because it uses a mathematical formula to calculate the length of the shortest sequence, rather than generating all possible sequences. The formula is based on the properties of the problem, and it ensures that we find the shortest sequence that cannot be obtained by rolling `n` dice with `k` sides each.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: mathematical formulas, combinatorics
- Problem-solving patterns identified: using mathematical formulas to solve problems
- Optimization techniques learned: using mathematical formulas to avoid generating all possible sequences
- Similar problems to practice: problems that involve combinatorics and mathematical formulas

**Mistakes to Avoid:**
- Common implementation errors: not using a mathematical formula to calculate the length of the shortest sequence
- Edge cases to watch for: `n = 1`, `k = 1`
- Performance pitfalls: generating all possible sequences
- Testing considerations: testing the solution with different values of `n` and `k` to ensure that it works correctly.