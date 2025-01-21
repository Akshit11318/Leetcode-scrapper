## Replace the Substring for Balanced String

**Problem Link:** https://leetcode.com/problems/replace-the-substring-for-balanced-string/description

**Problem Statement:**
- Input: A string `s` containing only the characters 'Q' and 'W'.
- Constraints: $1 \leq s.length \leq 10^5$
- Expected output: The minimum length of a substring that needs to be replaced to make `s` balanced.
- Key requirements: A string is considered balanced if it has an equal number of 'Q's and 'W's.
- Example test cases:
  - Input: "QWER"
    - Output: 0
  - Input: "QQWE"
    - Output: 1
  - Input: "QQQW"
    - Output: 2

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the minimum length of a substring that needs to be replaced, we can try all possible substrings and check if replacing them makes the string balanced.
- Step-by-step breakdown:
  1. Iterate over all possible substrings of `s`.
  2. For each substring, replace it with a balanced string (i.e., equal number of 'Q's and 'W's).
  3. Check if the resulting string is balanced.
  4. Keep track of the minimum length of a substring that needs to be replaced to make `s` balanced.

```cpp
int balancedString(string s) {
    int n = s.length();
    int res = n;
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            string temp = s;
            for (int k = i; k <= j; ++k) {
                if (temp[k] == 'Q') temp[k] = 'W';
                else temp[k] = 'Q';
            }
            if (isBalanced(temp)) res = min(res, j - i + 1);
        }
    }
    return res;
}

bool isBalanced(string s) {
    int q = 0, w = 0;
    for (char c : s) {
        if (c == 'Q') ++q;
        else ++w;
    }
    return q == w;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. This is because we are iterating over all possible substrings and for each substring, we are replacing it and checking if the resulting string is balanced.
> - **Space Complexity:** $O(n)$, as we are creating a temporary string to store the modified string.
> - **Why these complexities occur:** These complexities occur because of the brute force approach, which tries all possible substrings and replacements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: To make the string balanced, we need to replace a substring with an equal number of 'Q's and 'W's. We can use a sliding window approach to find the minimum length of a substring that needs to be replaced.
- Detailed breakdown:
  1. Calculate the frequency of 'Q's and 'W's in the string.
  2. Initialize two pointers, `left` and `right`, to the start of the string.
  3. Move the `right` pointer to the right and update the frequency of 'Q's and 'W's in the current window.
  4. If the window is balanced, move the `left` pointer to the right and update the frequency of 'Q's and 'W's in the current window.
  5. Keep track of the minimum length of a substring that needs to be replaced to make `s` balanced.

```cpp
int balancedString(string s) {
    int n = s.length();
    int res = n;
    int q = 0, w = 0;
    for (char c : s) {
        if (c == 'Q') ++q;
        else ++w;
    }
    if (q == w) return 0;
    int left = 0;
    for (int right = 0; right < n; ++right) {
        if (s[right] == 'Q') --q;
        else --w;
        while (q <= w) {
            res = min(res, right - left + 1);
            if (s[left] == 'Q') ++q;
            else ++w;
            ++left;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we are iterating over the string twice, once to calculate the frequency of 'Q's and 'W's, and once to find the minimum length of a substring that needs to be replaced.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the frequency of 'Q's and 'W's and the minimum length of a substring that needs to be replaced.
> - **Optimality proof:** This approach is optimal because it uses a sliding window approach to find the minimum length of a substring that needs to be replaced, which has a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, frequency calculation, and optimization techniques.
- Problem-solving patterns identified: Using a sliding window approach to find the minimum length of a substring that needs to be replaced.
- Optimization techniques learned: Using a sliding window approach to reduce the time complexity from $O(n^3)$ to $O(n)$.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the frequency of 'Q's and 'W's correctly in the sliding window approach.
- Edge cases to watch for: When the input string is already balanced, the function should return 0.
- Performance pitfalls: Using a brute force approach, which has a high time complexity.
- Testing considerations: Testing the function with different input strings, including edge cases, to ensure it returns the correct result.