## Minimum Swaps to Make Strings Equal

**Problem Link:** https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/description

**Problem Statement:**
- Input: Two binary strings `s1` and `s2` of the same length.
- Expected output: The minimum number of swaps required to make `s1` and `s2` equal.
- Key requirements and edge cases to consider:
  - Both strings have the same length.
  - The strings are binary, meaning they only contain `0`s and `1`s.
  - A swap operation involves exchanging two characters in the same position in both strings.
- Example test cases with explanations:
  - Input: `s1 = "1111", s2 = "0000"`; Output: `2` (swap the first and second characters, then the third and fourth characters).
  - Input: `s1 = "0100", s2 = "0010"`; Output: `1` (swap the first and second characters).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible permutations of swaps and check which one results in the minimum number of swaps to make `s1` and `s2` equal.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for the minimum number of swaps.
  2. Generate all possible permutations of swaps.
  3. For each permutation, apply the swaps to `s1` and check if it becomes equal to `s2`.
  4. If `s1` becomes equal to `s2`, update the minimum number of swaps.
- Why this approach comes to mind first: It's a straightforward approach that tries all possible solutions.

```cpp
#include <iostream>
#include <string>
#include <algorithm>

int minSwaps(string s1, string s2) {
    int n = s1.length();
    int min_swaps = n;
    for (int mask = 0; mask < (1 << n); mask++) {
        string temp_s1 = s1;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                // Swap characters at position i and i + 1
                swap(temp_s1[i], temp_s1[(i + 1) % n]);
            }
        }
        if (temp_s1 == s2) {
            min_swaps = min(min_swaps, __builtin_popcount(mask));
        }
    }
    return min_swaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the strings. This is because we generate all possible permutations of swaps (which takes $O(2^n)$ time) and apply each permutation to `s1` (which takes $O(n)$ time).
> - **Space Complexity:** $O(n)$, where $n$ is the length of the strings. This is because we need to store the temporary string `temp_s1`.
> - **Why these complexities occur:** The brute force approach tries all possible solutions, resulting in exponential time complexity. The space complexity is linear because we only need to store a single temporary string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible permutations of swaps, we can observe that a swap operation can only change the parity of the number of differences between `s1` and `s2`.
- Detailed breakdown of the approach:
  1. Count the number of differences between `s1` and `s2`.
  2. If the number of differences is even, we can make `s1` and `s2` equal by swapping pairs of different characters.
  3. If the number of differences is odd, we cannot make `s1` and `s2` equal by swapping characters.
- Proof of optimality: This approach is optimal because it only checks the parity of the number of differences between `s1` and `s2`, which is sufficient to determine the minimum number of swaps required.

```cpp
int minSwaps(string s1, string s2) {
    int n = s1.length();
    int diff = 0;
    for (int i = 0; i < n; i++) {
        if (s1[i] != s2[i]) {
            diff++;
        }
    }
    if (diff % 2 == 1) {
        return -1; // Cannot make s1 and s2 equal
    }
    int swaps = 0;
    for (int i = 0; i < n; i++) {
        if (s1[i] != s2[i]) {
            if (s1[i] == '1') {
                swaps++;
            }
        }
    }
    return swaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the strings. This is because we only need to iterate through the strings once to count the number of differences.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the strings. This is because we only need to store a few variables to keep track of the number of differences and swaps.
> - **Optimality proof:** This approach is optimal because it only checks the parity of the number of differences between `s1` and `s2`, which is sufficient to determine the minimum number of swaps required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Parity checking, swap operations.
- Problem-solving patterns identified: Observing the effect of swap operations on the parity of differences between strings.
- Optimization techniques learned: Avoiding unnecessary computations by only checking the parity of differences.
- Similar problems to practice: Other problems involving parity checking and swap operations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as when the input strings are empty or have different lengths.
- Edge cases to watch for: When the input strings have an odd number of differences, it is impossible to make them equal by swapping characters.
- Performance pitfalls: Trying all possible permutations of swaps, which results in exponential time complexity.
- Testing considerations: Test the function with different input strings, including edge cases and large inputs.