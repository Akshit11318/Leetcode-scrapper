## Minimum Number of Swaps to Make the String Balanced
**Problem Link:** https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description

**Problem Statement:**
- Input: A string `s` consisting of only `L` and `R` characters.
- Constraints: `1 <= s.length <= 1000`, `s` only contains `L` and `R`.
- Expected Output: The minimum number of swaps required to balance the string, where a string is considered balanced if all `L`s are on the left of all `R`s.
- Key Requirements: Find the minimum number of swaps to make the string balanced.
- Edge Cases: Empty string, single character string, string with only `L`s or only `R`s.

**Example Test Cases:**
- Input: `s = "LLR"` - Output: `1`
- Input: `s = "RRL"` - Output: `2`
- Input: `s = "LLRR"` - Output: `0`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible permutations of the string and count the number of swaps needed for each permutation to become balanced.
- Step-by-step breakdown:
  1. Generate all permutations of the input string.
  2. For each permutation, check if it's balanced by verifying all `L`s are on the left of all `R`s.
  3. Count the minimum number of swaps needed to transform the original string into a balanced permutation.

```cpp
#include <algorithm>
#include <string>

int minSwaps(string s) {
    int minSwaps = INT_MAX;
    do {
        string temp = s;
        int swaps = 0;
        for (int i = 0; i < temp.size(); ++i) {
            if (temp[i] != s[i]) {
                // Find the next character that should be at the current position
                for (int j = i + 1; j < temp.size(); ++j) {
                    if (temp[j] == s[i]) {
                        // Swap characters
                        swap(temp[i], temp[j]);
                        swaps++;
                        break;
                    }
                }
            }
        }
        // Check if the string is balanced
        bool balanced = true;
        bool seenR = false;
        for (char c : temp) {
            if (c == 'R') seenR = true;
            if (c == 'L' && seenR) {
                balanced = false;
                break;
            }
        }
        if (balanced) minSwaps = min(minSwaps, swaps);
    } while (next_permutation(s.begin(), s.end()));
    return minSwaps == INT_MAX ? -1 : minSwaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the length of the string. This is because we generate all permutations of the string (which is $n!$) and for each permutation, we potentially iterate through the string to find and swap characters.
> - **Space Complexity:** $O(n)$, as we need to store the current permutation of the string.
> - **Why these complexities occur:** The high time complexity is due to generating all permutations, and the space complexity is because we need to store the permutation and potentially a copy of it for swapping.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that to balance the string, we only need to ensure that all `L`s are on the left of all `R`s. This can be achieved by finding the first `R` that is on the left of an `L` and swapping it with the `L`. We repeat this process until no such `R` and `L` pair exists.
- However, a more efficient approach involves counting the number of `L`s and `R`s and then using two pointers to find the minimum number of swaps required to balance the string.

```cpp
#include <string>

int minSwaps(string s) {
    int countL = 0, countR = 0;
    for (char c : s) {
        if (c == 'L') countL++;
        else countR++;
    }
    
    int swaps = 0;
    int seenL = 0;
    for (int i = 0; i < countL; ++i) {
        if (s[i] == 'R') swaps++;
    }
    return swaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we make a single pass through the string to count `L`s and `R`s and then another pass to count the swaps needed.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counts and the swap count.
> - **Optimality proof:** This approach is optimal because it directly addresses the requirement to balance the string by counting the minimum number of swaps needed to move all `L`s to the left of all `R`s without unnecessary operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: permutation generation, string manipulation, and two-pointer technique.
- Problem-solving patterns identified: breaking down the problem into smaller, manageable parts (e.g., counting `L`s and `R`s).
- Optimization techniques learned: reducing time complexity by avoiding unnecessary operations (e.g., generating all permutations).

**Mistakes to Avoid:**
- Common implementation errors: incorrect permutation generation, failure to handle edge cases.
- Edge cases to watch for: empty string, single character string, string with only `L`s or only `R`s.
- Performance pitfalls: high time complexity due to unnecessary operations.
- Testing considerations: thoroughly test the function with various inputs, including edge cases.