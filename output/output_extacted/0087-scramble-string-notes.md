## Scramble String
**Problem Link:** https://leetcode.com/problems/scramble-string/description

**Problem Statement:**
- Input format and constraints: Given two strings `s1` and `s2` of the same length, determine if `s2` is a scrambled version of `s1`.
- Expected output format: Return `true` if `s2` is a scrambled version of `s1`, `false` otherwise.
- Key requirements and edge cases to consider: Both strings are non-empty and contain only lowercase letters.
- Example test cases with explanations:
  - `s1 = "great", s2 = "rgeat"`: `true` because `s2` is a scrambled version of `s1`.
  - `s1 = "abcde", s2 = "caebd"`: `false` because `s2` is not a scrambled version of `s1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible permutation of `s1` to see if any of them are equal to `s2`.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of `s1`.
  2. For each permutation, check if it is equal to `s2`.
  3. If a match is found, return `true`.
  4. If no match is found after checking all permutations, return `false`.
- Why this approach comes to mind first: It is a straightforward solution that checks every possible outcome.

```cpp
class Solution {
public:
    bool isScramble(string s1, string s2) {
        if (s1.size() != s2.size()) return false;
        if (s1 == s2) return true;
        
        // Generate all permutations of s1
        vector<string> perms = getPermutations(s1);
        
        // Check each permutation
        for (string perm : perms) {
            if (perm == s2) return true;
        }
        
        return false;
    }
    
    vector<string> getPermutations(string str) {
        if (str.size() == 1) {
            return {str};
        }
        
        vector<string> result;
        for (int i = 0; i < str.size(); i++) {
            string remaining = str.substr(0, i) + str.substr(i + 1);
            vector<string> perms = getPermutations(remaining);
            for (string perm : perms) {
                result.push_back(str[i] + perm);
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of `s1`, due to generating all permutations of `s1`.
> - **Space Complexity:** $O(n!)$, as we need to store all permutations of `s1`.
> - **Why these complexities occur:** Generating all permutations of a string has a time and space complexity of $O(n!)$ because there are $n!$ possible permutations of a string of length $n$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all permutations of `s1`, we can use dynamic programming to build up a solution.
- Detailed breakdown of the approach:
  1. Create a recursive function that checks if a substring of `s1` is a scrambled version of a substring of `s2`.
  2. Use memoization to store the results of subproblems to avoid redundant computation.
- Proof of optimality: This approach has a time complexity of $O(n^4)$, which is optimal because we need to consider all possible splits of the strings.

```cpp
class Solution {
public:
    bool isScramble(string s1, string s2) {
        unordered_map<string, unordered_set<string>> memo;
        return isScrambleHelper(s1, s2, memo);
    }
    
    bool isScrambleHelper(string s1, string s2, unordered_map<string, unordered_set<string>>& memo) {
        string key = s1 + "," + s2;
        if (memo.count(key)) return memo[key].count(s2);
        
        if (s1.size() != s2.size()) return false;
        if (s1 == s2) return true;
        
        string sortedS1 = s1;
        string sortedS2 = s2;
        sort(sortedS1.begin(), sortedS1.end());
        sort(sortedS2.begin(), sortedS2.end());
        if (sortedS1 != sortedS2) return false;
        
        for (int i = 1; i < s1.size(); i++) {
            if ((isScrambleHelper(s1.substr(0, i), s2.substr(0, i), memo) && isScrambleHelper(s1.substr(i), s2.substr(i), memo)) ||
                (isScrambleHelper(s1.substr(0, i), s2.substr(s2.size() - i), memo) && isScrambleHelper(s1.substr(i), s2.substr(0, s2.size() - i), memo))) {
                memo[key].insert(s2);
                return true;
            }
        }
        
        memo[key].insert("");
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the length of `s1`, due to the recursive function and memoization.
> - **Space Complexity:** $O(n^4)$, as we need to store the results of subproblems in the memoization table.
> - **Optimality proof:** This approach is optimal because we need to consider all possible splits of the strings, and the time complexity of $O(n^4)$ is the best we can achieve.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization, and recursion.
- Problem-solving patterns identified: Breaking down a problem into smaller subproblems and using memoization to avoid redundant computation.
- Optimization techniques learned: Using memoization to store the results of subproblems and avoiding redundant computation.
- Similar problems to practice: Other problems that involve dynamic programming and memoization, such as the Fibonacci sequence and the longest common subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as when the input strings are empty or have different lengths.
- Edge cases to watch for: When the input strings are empty or have different lengths, and when the strings are not scrambled versions of each other.
- Performance pitfalls: Not using memoization to avoid redundant computation, which can lead to a time complexity of $O(n!)$ instead of $O(n^4)$.
- Testing considerations: Testing the function with different input strings, including edge cases, to ensure that it works correctly.