## Swap Adjacent in LR String

**Problem Link:** https://leetcode.com/problems/swap-adjacent-in-lr-string/description

**Problem Statement:**
- Input: Two strings `start` and `target`, both of length `n`.
- Expected output: Whether it is possible to transform `start` into `target` by swapping adjacent characters in `start`.
- Key requirements: 
  - The string `start` only contains the characters 'L', 'R', and 'X'.
  - 'L' and 'R' represent left and right respectively, and 'X' represents an empty space that can be used as a buffer for swapping.
- Example test cases:
  - `start = "RXL"`, `target = "LXR"`, return `True`.
  - `start = "LL"`, `target = "RR"`, return `False`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible combinations of swaps.
- We can generate all permutations of the string `start` by swapping adjacent characters and check if any of these permutations match `target`.
- However, this approach comes to mind first due to its simplicity, but it's inefficient for large inputs.

```cpp
class Solution {
public:
    bool canTransform(string start, string end) {
        if (start.length() != end.length()) return false;
        int n = start.length();
        
        // Generate all permutations
        vector<string> permutations;
        permute(start, 0, n - 1, permutations);
        
        // Check if any permutation matches target
        for (auto& perm : permutations) {
            if (perm == end) return true;
        }
        
        return false;
    }
    
    void permute(string str, int left, int right, vector<string>& permutations) {
        if (left == right) permutations.push_back(str);
        else {
            for (int i = left; i <= right; i++) {
                swap(str[left], str[i]);
                permute(str, left + 1, right, permutations);
                swap(str[left], str[i]); // backtrack
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ due to generating all permutations of the string.
> - **Space Complexity:** $O(n!)$ for storing all permutations.
> - **Why these complexities occur:** The brute force approach involves generating all possible permutations of the input string, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to compare the positions of 'L' and 'R' in both strings and check if the relative order is maintained.
- We can iterate through both strings simultaneously and check if the indices of 'L' and 'R' in `start` are less than or equal to their indices in `target`.
- This approach is optimal because it avoids unnecessary swaps and only checks the relative order of 'L' and 'R'.

```cpp
class Solution {
public:
    bool canTransform(string start, string end) {
        if (start.length() != end.length()) return false;
        int n = start.length();
        
        int i = 0, j = 0;
        while (i < n && j < n) {
            while (i < n && start[i] == 'X') i++;
            while (j < n && end[j] == 'X') j++;
            
            if (i == n && j == n) return true;
            if (i == n || j == n) return false;
            
            if (start[i] != end[j]) return false;
            if (start[i] == 'L' && i < j) return false;
            if (start[i] == 'R' && i > j) return false;
            
            i++; j++;
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the indices and characters.
> - **Optimality proof:** This approach is optimal because it only checks the relative order of 'L' and 'R' in the input strings, which is the minimum required to determine if a transformation is possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, relative order comparison.
- Problem-solving patterns identified: checking the relative order of specific characters in two strings.
- Optimization techniques learned: avoiding unnecessary swaps by comparing the relative order of characters.
- Similar problems to practice: string transformation problems, relative order comparison problems.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as empty strings or strings with different lengths.
- Edge cases to watch for: strings with multiple 'X' characters, strings with 'L' and 'R' characters in different orders.
- Performance pitfalls: using brute force approaches for large inputs, not optimizing the comparison of relative orders.
- Testing considerations: testing with different input lengths, testing with different combinations of 'L', 'R', and 'X' characters.