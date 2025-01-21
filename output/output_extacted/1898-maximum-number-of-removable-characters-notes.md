## Maximum Number of Removable Characters

**Problem Link:** https://leetcode.com/problems/maximum-number-of-removable-characters/description

**Problem Statement:**
- Given a string `s`, a string `p`, and an array of integers `removable`, find the maximum number of removable characters in `s` that can be removed to get a subsequence of `p`.
- Input format: `s`, `p`, `removable`
- Expected output format: Maximum number of removable characters
- Key requirements: The characters in `s` must be removed in the order specified by `removable`.
- Example test cases:
  - `s = "abcab", p = "abc", removable = [0, 1, 2]`: The maximum number of removable characters is 2.
  - `s = "ab", p = "ba", removable = [0]`: The maximum number of removable characters is 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of removing characters from `s` and check if the resulting string is a subsequence of `p`.
- Step-by-step breakdown:
  1. Generate all possible combinations of removing characters from `s` based on `removable`.
  2. For each combination, create a new string by removing the corresponding characters from `s`.
  3. Check if the new string is a subsequence of `p`.
  4. Keep track of the maximum number of removable characters that result in a subsequence of `p`.
- Why this approach comes to mind first: It's a straightforward way to explore all possible solutions.

```cpp
class Solution {
public:
    int maximumRemovals(string s, string p, vector<int>& removable) {
        int n = removable.size();
        int maxRemovals = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            string temp = s;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    temp.erase(removable[i], 1);
                }
            }
            if (isSubsequence(temp, p)) {
                maxRemovals = max(maxRemovals, __builtin_popcount(mask));
            }
        }
        return maxRemovals;
    }
    
    bool isSubsequence(string s, string p) {
        int i = 0, j = 0;
        while (i < s.size() && j < p.size()) {
            if (s[i] == p[j]) {
                j++;
            }
            i++;
        }
        return j == p.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m \cdot n)$, where $n$ is the number of removable characters and $m$ is the length of `p`. This is because we generate all possible combinations of removing characters and check if each resulting string is a subsequence of `p`.
> - **Space Complexity:** $O(m)$, where $m$ is the length of `s`. This is because we create a temporary string for each combination of removing characters.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity due to generating all possible combinations of removing characters. The space complexity is linear because we only need to store the temporary string for each combination.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use binary search to find the maximum number of removable characters.
- Detailed breakdown:
  1. Initialize the search range to `[0, n]`, where `n` is the number of removable characters.
  2. For each mid point in the search range, create a new string by removing the corresponding characters from `s`.
  3. Check if the new string is a subsequence of `p`.
  4. If it is, update the search range to `[mid + 1, n]`. Otherwise, update the search range to `[0, mid]`.
- Proof of optimality: The binary search approach has a time complexity of $O(n \cdot m \cdot log(n))$, which is optimal because we need to check each character in `s` and `p` at least once.

```cpp
class Solution {
public:
    int maximumRemovals(string s, string p, vector<int>& removable) {
        int n = removable.size();
        int left = 0, right = n;
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            string temp = s;
            for (int i = 0; i < mid; i++) {
                temp.erase(removable[i], 1);
            }
            if (isSubsequence(temp, p)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
    
    bool isSubsequence(string s, string p) {
        int i = 0, j = 0;
        while (i < s.size() && j < p.size()) {
            if (s[i] == p[j]) {
                j++;
            }
            i++;
        }
        return j == p.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(n))$, where $n$ is the number of removable characters and $m$ is the length of `p`. This is because we use binary search to find the maximum number of removable characters and check if each resulting string is a subsequence of `p`.
> - **Space Complexity:** $O(m)$, where $m$ is the length of `s`. This is because we create a temporary string for each mid point in the search range.
> - **Optimality proof:** The binary search approach is optimal because it has a logarithmic factor in the time complexity, which is the best we can achieve for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Binary search, subsequence checking
- Problem-solving patterns: Using binary search to find the maximum or minimum value of a function
- Optimization techniques: Reducing the search space using binary search
- Similar problems to practice: Other problems that involve finding the maximum or minimum value of a function using binary search

**Mistakes to Avoid:**
- Common implementation errors: Not checking the base cases correctly, not updating the search range correctly
- Edge cases to watch for: When the input strings are empty, when the removable characters are not in the correct order
- Performance pitfalls: Using a brute force approach instead of binary search, not optimizing the subsequence checking function
- Testing considerations: Test the function with different input strings and removable characters, test the function with edge cases.