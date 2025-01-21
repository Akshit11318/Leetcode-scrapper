## Flip String to Monotone Increasing
**Problem Link:** https://leetcode.com/problems/flip-string-to-monotone-increasing/description

**Problem Statement:**
- Input: A string `s` consisting of characters '0' and '1'.
- Constraints: $1 \leq s.length \leq 200$
- Expected output: The minimum number of flips to make `s` monotone increasing.
- Key requirements: A string is monotone increasing if all '0's are on the left side of all '1's.
- Example test cases:
  - Input: `s = "00110"`
    - Output: `1`
    - Explanation: Flip the first '0' to '1', resulting in "11110".
  - Input: `s = "010110"`
    - Output: `2`
    - Explanation: Flip the first '0' to '1' and the third '0' to '1', resulting in "111110".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of flips to find the minimum number of flips required to make the string monotone increasing.
- Step-by-step breakdown:
  1. Generate all possible binary strings of the same length as the input string.
  2. For each binary string, check if it is monotone increasing.
  3. If it is monotone increasing, calculate the number of flips required to transform the input string into this binary string.
  4. Keep track of the minimum number of flips found.

```cpp
class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int minFlips = INT_MAX;
        for (int mask = 0; mask < (1 << s.size()); mask++) {
            string binaryString = "";
            for (int i = 0; i < s.size(); i++) {
                if ((mask & (1 << i)) != 0) {
                    binaryString += '1';
                } else {
                    binaryString += '0';
                }
            }
            if (isMonotoneIncreasing(binaryString)) {
                int flips = 0;
                for (int i = 0; i < s.size(); i++) {
                    if (s[i] != binaryString[i]) {
                        flips++;
                    }
                }
                minFlips = min(minFlips, flips);
            }
        }
        return minFlips;
    }

    bool isMonotoneIncreasing(string s) {
        bool seenOne = false;
        for (char c : s) {
            if (c == '1') {
                seenOne = true;
            } else if (seenOne) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string, because we generate all possible binary strings and check each one.
> - **Space Complexity:** $O(n)$, because we need to store each binary string.
> - **Why these complexities occur:** The brute force approach has high time complexity due to generating all possible binary strings and checking each one, which results in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of trying all possible combinations, we can use a single pass through the string to keep track of the minimum number of flips required to make the string monotone increasing.
- Detailed breakdown:
  1. Initialize two variables: `ones` to count the number of '1's seen so far, and `flips` to count the minimum number of flips required.
  2. Iterate through the string from left to right.
  3. For each '0' encountered, increment `flips` by the minimum of `ones` and the number of '1's remaining in the string.
  4. For each '1' encountered, increment `ones`.
  5. Return `flips` as the minimum number of flips required.

```cpp
class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int ones = 0;
        int flips = 0;
        for (char c : s) {
            if (c == '1') {
                ones++;
            } else {
                flips = min(flips + 1, ones);
            }
        }
        return flips;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because we make a single pass through the string and keep track of the minimum number of flips required, which is the most efficient way to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, single pass through the string.
- Problem-solving patterns identified: Using a single pass to keep track of the minimum number of flips required.
- Optimization techniques learned: Avoiding brute force approaches by using a single pass through the string.
- Similar problems to practice: Other string manipulation problems, such as finding the longest common subsequence or the minimum number of operations to transform one string into another.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not checking for edge cases.
- Edge cases to watch for: Empty string, string with only '0's or only '1's.
- Performance pitfalls: Using brute force approaches, not optimizing the solution.
- Testing considerations: Testing with different input strings, including edge cases.