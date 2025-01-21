## Palindrome Partitioning

**Problem Link:** https://leetcode.com/problems/palindrome-partitioning/description

**Problem Statement:**
- Input: A string `s`.
- Constraints: `1 <= s.length <= 16`.
- Expected Output: A list of all possible palindrome partitions of the string.
- Key Requirements: Each partition must be a palindrome.
- Edge Cases: Empty string, single character string, strings with repeating characters.

Example Test Cases:
- Input: `"aab"`
  - Expected Output: `[["a","a","b"],["aa","b"]]`
- Input: `"abba"`
  - Expected Output: `[["a","b","b","a"],["a","bb","a"],["abba"]]`

---

### Brute Force Approach

**Explanation:**
- Generate all possible partitions of the input string.
- For each partition, check if each substring is a palindrome.
- If a partition consists entirely of palindromes, add it to the result.

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> path;
        backtrack(s, 0, path, result);
        return result;
    }
    
    void backtrack(string& s, int start, vector<string>& path, vector<vector<string>>& result) {
        if (start == s.length()) {
            result.push_back(path);
            return;
        }
        
        for (int end = start; end < s.length(); ++end) {
            string substr = s.substr(start, end - start + 1);
            if (isPalindrome(substr)) {
                path.push_back(substr);
                backtrack(s, end + 1, path, result);
                path.pop_back();
            }
        }
    }
    
    bool isPalindrome(string& s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s[left] != s[right]) return false;
            ++left;
            --right;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we generate all possible partitions (exponential time) and for each partition, we check if each substring is a palindrome (linear time).
> - **Space Complexity:** $O(n)$, for storing the recursive call stack and the current partition.
> - **Why these complexities occur:** The brute force approach involves generating all possible partitions and checking each one, leading to exponential time complexity. The space complexity is linear due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Use a similar approach to the brute force, but with an optimization: instead of checking if a substring is a palindrome for each partition, precompute a table of palindromic substrings.
- This table can be used to quickly determine if a substring is a palindrome.

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        int n = s.length();
        vector<vector<bool>> isPalin(n, vector<bool>(n, false));
        for (int i = n - 1; i >= 0; --i) {
            isPalin[i][i] = true;
            for (int j = i + 1; j < n; ++j) {
                if (s[i] == s[j] && (j - i == 1 || isPalin[i + 1][j - 1])) {
                    isPalin[i][j] = true;
                }
            }
        }
        
        vector<vector<string>> result;
        vector<string> path;
        backtrack(s, 0, path, result, isPalin);
        return result;
    }
    
    void backtrack(string& s, int start, vector<string>& path, vector<vector<string>>& result, vector<vector<bool>>& isPalin) {
        if (start == s.length()) {
            result.push_back(path);
            return;
        }
        
        for (int end = start; end < s.length(); ++end) {
            if (isPalin[start][end]) {
                path.push_back(s.substr(start, end - start + 1));
                backtrack(s, end + 1, path, result, isPalin);
                path.pop_back();
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we still generate all possible partitions (exponential time), but we use a precomputed table to quickly check if a substring is a palindrome.
> - **Space Complexity:** $O(n^2)$, for storing the precomputed table of palindromic substrings.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity of checking if a substring is a palindrome from linear to constant time, while still generating all possible partitions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: backtracking, dynamic programming.
- Problem-solving patterns identified: precomputing tables to reduce time complexity.
- Optimization techniques learned: using precomputed tables to avoid redundant computations.
- Similar problems to practice: other partitioning problems, such as partitioning a string into words from a dictionary.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases correctly, not initializing variables properly.
- Edge cases to watch for: empty string, single character string, strings with repeating characters.
- Performance pitfalls: not using precomputed tables to reduce time complexity.
- Testing considerations: test with different input lengths, test with strings containing repeating characters.