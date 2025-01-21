## Shortest Palindrome
**Problem Link:** https://leetcode.com/problems/shortest-palindrome/description

**Problem Statement:**
- Input: A string `s`.
- Constraints: The length of `s` is in the range `[1, 1000]`.
- Expected output: The shortest palindrome you can find by adding characters in front of `s`.
- Key requirements: The resulting string must be a palindrome.
- Example test cases:
  - Input: `"a"`
    - Output: `"a"`
  - Input: `"abcd"`
    - Output: `"dcbabcd"`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible prefixes of the reversed string and checking if the resulting string is a palindrome.
- Step-by-step breakdown:
  1. Reverse the input string `s`.
  2. For each prefix of the reversed string, append it to the front of the original string `s`.
  3. Check if the resulting string is a palindrome.
  4. Return the first palindrome found, as it will be the shortest due to the nature of the algorithm.

```cpp
string shortestPalindrome(string s) {
    string rev = s;
    reverse(rev.begin(), rev.end());
    for (int i = 0; i <= s.size(); ++i) {
        if (isPalindrome(s.substr(0, s.size() - i) + rev)) {
            return rev.substr(0, i) + s;
        }
    }
    // This line should never be reached due to the problem constraints
    return "";
}

bool isPalindrome(const string& s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        if (s[left] != s[right]) return false;
        ++left, --right;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the input string `s`. This is because in the worst case, we are checking every prefix of the reversed string, and for each, we are checking if the resulting string is a palindrome, which itself takes $O(n)$ time.
> - **Space Complexity:** $O(n)$ for storing the reversed string and the temporary palindromes.
> - **Why these complexities occur:** The brute force approach involves nested loops: one for generating prefixes and another implicit loop in the palindrome check. This leads to quadratic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a KMP (Knuth-Morris-Pratt) algorithm-like approach to efficiently find the longest proper prefix of `s` that is also a suffix.
- Detailed breakdown:
  1. Preprocess the string `s` to find the longest proper prefix that is also a suffix.
  2. The remaining part of the reversed string (not part of the suffix) is the prefix we need to add to `s` to make it a palindrome.

```cpp
string shortestPalindrome(string s) {
    string rev = s;
    reverse(rev.begin(), rev.end());
    string concat = s + "#" + rev;
    vector<int> lps(concat.size());
    for (int idx = 1; idx < concat.size(); ++idx) {
        int prev_lps = lps[idx - 1];
        while (prev_lps > 0 && concat[prev_lps] != concat[idx]) {
            prev_lps = lps[prev_lps - 1];
        }
        if (concat[prev_lps] == concat[idx]) ++prev_lps;
        lps[idx] = prev_lps;
    }
    return rev.substr(0, s.size() - lps.back()) + s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input string `s`. This is because we are making a single pass through the concatenated string to fill the `lps` array.
> - **Space Complexity:** $O(n)$ for storing the `lps` array and the reversed string.
> - **Optimality proof:** This approach is optimal because it makes a single pass through the data, using the KMP algorithm's efficiency to find the longest proper prefix that is also a suffix, which directly gives us the shortest palindrome.

---

### Final Notes

**Learning Points:**
- The KMP algorithm can be adapted for various string matching and manipulation tasks.
- Understanding how to apply known algorithms to new problems is crucial for efficient problem-solving.
- Preprocessing data (like creating the `lps` array) can significantly improve the efficiency of algorithms.

**Mistakes to Avoid:**
- Not considering the properties of palindromes and how they can be efficiently constructed.
- Overlooking the potential for using established algorithms like KMP for string manipulation tasks.
- Failing to optimize the solution by directly finding the longest proper prefix that is also a suffix.