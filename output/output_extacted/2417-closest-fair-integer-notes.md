## Closest Fair Integer
**Problem Link:** https://leetcode.com/problems/closest-fair-integer/description

**Problem Statement:**
- Input: An integer `n`.
- Output: The closest integer `x` to `n` such that `x` is a fair integer, i.e., the number of `1`s in the binary representation of `x` equals the number of `0`s. If there are multiple such integers, return the one with the smallest absolute difference with `n`. If there's a tie, return the smaller integer.
- Key requirements and edge cases to consider:
  - Handle negative numbers and zero.
  - Consider cases where `n` itself is a fair integer.
- Example test cases with explanations:
  - For `n = 1`, the closest fair integer is `2` (binary `10`), with one `1` and one `0`.
  - For `n = 3`, the closest fair integer is `2` (binary `10`), because `3` (binary `11`) is not fair.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through integers starting from `n` and check each for being fair.
- Step-by-step breakdown of the solution:
  1. Define a function to count the number of `1`s and `0`s in the binary representation of a number.
  2. Starting from `n`, check each integer (both increasing and decreasing) to see if it's fair.
  3. The first fair integer found is the closest, given the nature of the search.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int n = nums[0];
        int minDiff = INT_MAX;
        int result = INT_MIN;
        
        for (int i = n; ; i++) {
            if (isFair(i)) {
                int diff = abs(i - n);
                if (diff < minDiff) {
                    minDiff = diff;
                    result = i;
                } else if (diff == minDiff && i < result) {
                    result = i;
                }
            }
            if (i - n > minDiff) break; // No need to continue searching further
        }
        
        for (int i = n - 1; ; i--) {
            if (isFair(i)) {
                int diff = abs(i - n);
                if (diff < minDiff) {
                    minDiff = diff;
                    result = i;
                } else if (diff == minDiff && i < result) {
                    result = i;
                }
            }
            if (n - i > minDiff) break; // No need to continue searching further
        }
        
        return result;
    }
    
    bool isFair(int num) {
        int ones = 0, zeros = 0;
        while (num > 0) {
            if (num & 1) ones++;
            else zeros++;
            num >>= 1;
        }
        return ones == zeros;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input number, because in the worst case, we might have to iterate up to $n$ to find a fair integer.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space.
> - **Why these complexities occur:** The iteration to find the closest fair integer and the bitwise operations to check for fairness contribute to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Recognize that fair integers have a specific pattern in their binary representation, which can be generated iteratively.
- Detailed breakdown of the approach:
  1. Generate fair integers iteratively, starting from the smallest.
  2. Keep track of the closest fair integer to `n` as we generate them.
- Proof of optimality: This approach ensures we consider all possible fair integers in ascending order, stopping as soon as we've found the closest one, thus optimizing the search.

```cpp
class Solution {
public:
    int findClosestNumber(int n) {
        int minDiff = INT_MAX;
        int result = INT_MIN;
        int i = 0;
        
        while (true) {
            if (isFair(i)) {
                int diff = abs(i - n);
                if (diff < minDiff) {
                    minDiff = diff;
                    result = i;
                } else if (diff == minDiff && i < result) {
                    result = i;
                }
            }
            if (i > n + minDiff) break; // No need to continue searching further
            i++;
        }
        
        i = INT_MAX;
        while (true) {
            if (i <= n - minDiff) break;
            if (isFair(i)) {
                int diff = abs(i - n);
                if (diff < minDiff) {
                    minDiff = diff;
                    result = i;
                } else if (diff == minDiff && i < result) {
                    result = i;
                }
            }
            i--;
        }
        
        return result;
    }
    
    bool isFair(int num) {
        int ones = 0, zeros = 0;
        while (num > 0) {
            if (num & 1) ones++;
            else zeros++;
            num >>= 1;
        }
        return ones == zeros;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, because we are essentially searching through numbers of up to $\log n$ bits to find the closest fair integer.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it systematically checks all possible fair integers closest to `n`, stopping as soon as it finds the closest one, thus minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iterative generation of fair integers, bitwise operations for checking fairness.
- Problem-solving patterns identified: Systematic search for the closest match, optimizing the search by stopping early when a closer match is found.
- Optimization techniques learned: Early termination of the search when a closer fair integer is found.
- Similar problems to practice: Other problems involving binary representations and fairness conditions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the fairness check or the iterative search.
- Edge cases to watch for: Handling negative numbers, zero, and the case where `n` itself is a fair integer.
- Performance pitfalls: Failing to terminate the search early when a closer fair integer is found, leading to unnecessary iterations.
- Testing considerations: Thoroughly testing with various inputs, including edge cases and large numbers, to ensure correctness and performance.