## Longest Happy Prefix
**Problem Link:** https://leetcode.com/problems/longest-happy-prefix/description

**Problem Statement:**
- Input format and constraints: The input is a string `s`. The length of `s` is between 1 and 10^5. `s` consists of lowercase English letters.
- Expected output format: The function should return the longest prefix which is also a suffix.
- Key requirements and edge cases to consider: The prefix should also be a suffix, and it should be the longest such string. If there's no such string, the function should return an empty string.
- Example test cases with explanations:
  - Input: "level"
    - Output: "l"
    - Explanation: The string "l" is both a prefix and a suffix.
  - Input: "ababab"
    - Output: "ababab"
    - Explanation: The entire string is both a prefix and a suffix.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to check every prefix of the string and see if it's also a suffix.
- Step-by-step breakdown of the solution:
  1. Start with the entire string as the prefix.
  2. Check if the prefix is equal to the suffix. If it is, return the prefix.
  3. If not, reduce the length of the prefix by one character and repeat the process until the prefix is empty.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It involves checking every possible prefix and suffix, which guarantees that we'll find the longest happy prefix if it exists.

```cpp
string longestPrefix(string s) {
    for (int i = s.length(); i > 0; --i) {
        string prefix = s.substr(0, i);
        if (s.substr(s.length() - i, i) == prefix) {
            return prefix;
        }
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the string. This is because in the worst case, we're checking every prefix and suffix, and the string operations (substr) take $O(n)$ time.
> - **Space Complexity:** $O(n)$ because we're creating new strings (prefix and suffix) of maximum length $n$.
> - **Why these complexities occur:** The string operations and the nested loop structure cause these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every prefix and suffix, we can use the KMP (Knuth-Morris-Pratt) algorithm to find the longest prefix that is also a suffix.
- Detailed breakdown of the approach:
  1. Initialize a `lps` (longest proper prefix which is also a suffix) array of size $n$, where $n$ is the length of the string.
  2. Fill the `lps` array using the KMP algorithm.
  3. The last element of the `lps` array will be the length of the longest prefix that is also a suffix.
- Proof of optimality: This approach is optimal because it uses the KMP algorithm, which has a time complexity of $O(n)$.

```cpp
string longestPrefix(string s) {
    int n = s.length();
    vector<int> lps(n, 0);
    int len = 0;
    for (int i = 1; i < n; ++i) {
        while (len > 0 && s[i] != s[len]) {
            len = lps[len - 1];
        }
        if (s[i] == s[len]) {
            len++;
        }
        lps[i] = len;
    }
    return s.substr(0, lps[n - 1]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string. This is because we're filling the `lps` array in a single pass.
> - **Space Complexity:** $O(n)$ because we're creating a `lps` array of size $n$.
> - **Optimality proof:** The KMP algorithm is known to be optimal for string matching and prefix/suffix problems, making this approach the most efficient solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The KMP algorithm and its application to prefix/suffix problems.
- Problem-solving patterns identified: Using a `lps` array to keep track of the longest proper prefix which is also a suffix.
- Optimization techniques learned: Using the KMP algorithm to reduce the time complexity from $O(n^2)$ to $O(n)$.
- Similar problems to practice: Other string matching and prefix/suffix problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as an empty string or a string with a single character.
- Edge cases to watch for: Strings with repeated characters or strings with no happy prefix.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing the function with different types of strings, including edge cases and large inputs.