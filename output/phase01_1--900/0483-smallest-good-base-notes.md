## Smallest Good Base

**Problem Link:** https://leetcode.com/problems/smallest-good-base/description

**Problem Statement:**
- Input: A string `n` representing a positive integer.
- Expected output: The smallest good base for `n`.
- Key requirements: A good base for `n` is an integer `base` such that all digits of `n` in base `base` are 1. In other words, `n` in base `base` should be a sequence of 1s.
- Example test cases:
  - Input: `n = "13"`
    - Output: `"9"` because `13` in base `9` is `14` which is not a sequence of 1s, but `13` in base `8` is `15` which is also not a sequence of 1s. However, `13` in base `3` is `111` which is a sequence of 1s.
  - Input: `n = "4681"`
    - Output: `"8"` because `4681` in base `8` is `11101` which is not a sequence of 1s. However, `4681` in base `6` is not a sequence of 1s either. But, there is no base that can represent `4681` as a sequence of 1s.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible bases from `2` to `n` (inclusive) and check if `n` can be represented as a sequence of 1s in that base.
- We start by converting the number `n` to each possible base and then check if all digits are `1`.
- This approach comes to mind first because it is straightforward and does not require any specific insight or optimization.

```cpp
class Solution {
public:
    string smallestGoodBase(string n) {
        long long num = stoll(n);
        for (long long base = 2; base <= num; base++) {
            long long cur = 1;
            long long sum = 0;
            bool isGood = true;
            while (sum < num) {
                sum += cur;
                cur *= base;
                if (sum == num) break;
                if (sum > num) {
                    isGood = false;
                    break;
                }
            }
            if (isGood) return to_string(base);
        }
        return to_string(num - 1);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ because in the worst case, we are trying all possible bases from `2` to `n` and for each base, we are performing a constant amount of work.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store our variables.
> - **Why these complexities occur:** These complexities occur because we are using a simple iterative approach to try all possible bases.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to realize that the number of digits in base `base` is $\log_{base} n$.
- We can use this insight to directly calculate the maximum possible base and then try all bases from the maximum possible base down to `2`.
- This approach is optimal because it reduces the number of bases we need to try, resulting in a significant improvement in performance.

```cpp
class Solution {
public:
    string smallestGoodBase(string n) {
        long long num = stoll(n);
        long long maxBase = (long long)sqrt(num);
        for (long long base = maxBase; base >= 2; base--) {
            long long sum = 0;
            long long cur = 1;
            while (sum < num) {
                sum += cur;
                cur *= base;
                if (sum == num) return to_string(base);
                if (sum > num) break;
            }
        }
        return to_string(num - 1);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{n})$ because in the worst case, we are trying all possible bases from the maximum possible base down to `2`.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store our variables.
> - **Optimality proof:** This is the optimal solution because we are trying all possible bases in the most efficient order, resulting in the minimum number of iterations required to find the smallest good base.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: brute force approach, optimization techniques.
- Problem-solving patterns identified: trying all possible bases, using insights to reduce the number of iterations.
- Optimization techniques learned: using the maximum possible base to reduce the number of iterations.
- Similar problems to practice: finding the smallest number that can be represented as a sequence of 1s in a given base.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not using the correct data types.
- Edge cases to watch for: when `n` is `1`, when `n` is a power of `2`.
- Performance pitfalls: trying all possible bases without using any optimization techniques.
- Testing considerations: testing with large inputs, testing with edge cases.