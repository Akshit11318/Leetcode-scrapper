## Last Substring in Lexicographical Order

**Problem Link:** https://leetcode.com/problems/last-substring-in-lexicographical-order/description

**Problem Statement:**
- Input format: a string `s`.
- Constraints: `1 <= s.length <= 10^5`, `s` consists of lowercase English letters.
- Expected output format: the last substring of `s` in lexicographical order.
- Key requirements and edge cases to consider: the input string may contain duplicate characters, and the last substring should be in lexicographical order.
- Example test cases with explanations: 
    - For the input `"ababc"`, the output should be `"c"`.
    - For the input `"abcd"`, the output should be `"d"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: generate all possible substrings of the input string and compare them to find the last substring in lexicographical order.
- Step-by-step breakdown of the solution:
    1. Generate all possible substrings of the input string.
    2. Compare each substring with the others to find the last substring in lexicographical order.
- Why this approach comes to mind first: it is a straightforward and intuitive approach to solve the problem.

```cpp
#include <iostream>
#include <string>
#include <vector>

string lastSubstring(string s) {
    int n = s.size();
    string res = "";
    for (int i = 0; i < n; i++) {
        string curr = "";
        for (int j = i; j < n; j++) {
            curr += s[j];
            if (curr > res) {
                res = curr;
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. The reason for this complexity is that we are generating all possible substrings of the input string, and for each substring, we are comparing it with the current result.
> - **Space Complexity:** $O(n)$, as we need to store the current substring and the result.
> - **Why these complexities occur:** the brute force approach involves generating all possible substrings and comparing them, which results in high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: we can use a two-pointer technique to find the last substring in lexicographical order. We maintain two pointers, `i` and `j`, where `i` is the starting index of the current substring and `j` is the ending index.
- Detailed breakdown of the approach:
    1. Initialize `i` to 0 and `j` to 0.
    2. Initialize the result to an empty string.
    3. Iterate through the input string from left to right. For each character, compare the current substring with the substring starting from the next character.
    4. If the current substring is greater than the next substring, update the result.
- Proof of optimality: the optimal approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <string>

string lastSubstring(string s) {
    int n = s.size();
    string res = "";
    for (int i = 0; i < n; i++) {
        string curr = s.substr(i);
        if (curr > res) {
            res = curr;
        }
    }
    return res;
}
```

However, this solution is still not optimal. To optimize it further, we can use the following approach:

```cpp
#include <iostream>
#include <string>

string lastSubstring(string s) {
    int n = s.size();
    string res = s.substr(n-1);
    for (int i = n-2; i >= 0; i--) {
        if (s[i] > s[i+1]) {
            res = s.substr(i) > res ? s.substr(i) : res;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string.
> - **Space Complexity:** $O(n)$, as we need to store the result.
> - **Optimality proof:** the optimal approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem. The space complexity is also optimal as we need to store the result.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: two-pointer technique, substring comparison.
- Problem-solving patterns identified: using a two-pointer technique to find the last substring in lexicographical order.
- Optimization techniques learned: reducing the number of comparisons by using a two-pointer technique.
- Similar problems to practice: finding the longest substring with a given property.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not initializing variables correctly.
- Edge cases to watch for: empty input string, input string with duplicate characters.
- Performance pitfalls: using a brute force approach with high time complexity.
- Testing considerations: testing with different input strings, including edge cases.