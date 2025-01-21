## Check If One String Swap Can Make Strings Equal

**Problem Link:** https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description

**Problem Statement:**
- Input format and constraints: Two strings `s1` and `s2` of the same length.
- Expected output format: A boolean indicating whether one string swap can make the strings equal.
- Key requirements and edge cases to consider: Handling strings of different lengths, empty strings, and strings with different characters.
- Example test cases with explanations:
  - `s1 = "bank", s2 = "kanb"`: Returns `true` because one string swap can make the strings equal.
  - `s1 = "attack", s2 = "defend"`: Returns `false` because no string swap can make the strings equal.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible swaps of characters in `s1` and check if any of them make `s1` equal to `s2`.
- Step-by-step breakdown of the solution:
  1. Iterate over each character in `s1`.
  2. For each character, try swapping it with every other character in `s1`.
  3. After each swap, check if `s1` is equal to `s2`.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by brute force.

```cpp
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int n = s1.length();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // Create a copy of s1 to perform the swap
                string temp = s1;
                swap(temp[i], temp[j]);
                if (temp == s2) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string. This is because we have two nested loops that iterate over the string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we create a copy of the string for each swap.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, and the creation of a copy of the string for each swap causes the space complexity to be linear.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We only need to consider the positions where `s1` and `s2` differ.
- Detailed breakdown of the approach:
  1. Find the positions where `s1` and `s2` differ.
  2. If there are more than 2 positions where they differ, return `false`.
  3. If there are exactly 2 positions where they differ, check if swapping the characters at these positions makes `s1` equal to `s2`.
- Proof of optimality: This approach is optimal because we only consider the positions where `s1` and `s2` differ, which reduces the number of swaps we need to check.
- Why further optimization is impossible: We need to check all positions where `s1` and `s2` differ to ensure that we don't miss any possible swaps.

```cpp
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int n = s1.length();
        vector<int> diff;
        for (int i = 0; i < n; i++) {
            if (s1[i] != s2[i]) {
                diff.push_back(i);
            }
        }
        if (diff.size() == 0) {
            return true;
        } else if (diff.size() == 2) {
            return s1[diff[0]] == s2[diff[1]] && s1[diff[1]] == s2[diff[0]];
        } else {
            return false;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we only iterate over the string once to find the positions where `s1` and `s2` differ.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the string. This is because we only use a constant amount of space to store the positions where `s1` and `s2` differ.
> - **Optimality proof:** This approach is optimal because we only consider the positions where `s1` and `s2` differ, which reduces the number of swaps we need to check.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, swapping, and comparison.
- Problem-solving patterns identified: Finding the positions where two strings differ and checking if swapping the characters at these positions makes the strings equal.
- Optimization techniques learned: Reducing the number of swaps to check by only considering the positions where the strings differ.
- Similar problems to practice: String comparison and manipulation problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as empty strings or strings of different lengths.
- Edge cases to watch for: Handling strings with different characters and checking for equality.
- Performance pitfalls: Using a brute force approach that checks all possible swaps, which can be inefficient for large strings.
- Testing considerations: Testing the function with different input strings and edge cases to ensure it works correctly.