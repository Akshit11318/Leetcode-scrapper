## Longest Happy String
**Problem Link:** https://leetcode.com/problems/longest-happy-string/description

**Problem Statement:**
- Input format and constraints: The input will be three integers `a`, `b`, and `c`, representing the number of `a`, `b`, and `c` characters available.
- Expected output format: The longest possible happy string.
- Key requirements and edge cases to consider: A happy string is a string that:
  - Contains only `a`, `b`, and `c`.
  - Does not have more than two consecutive `a`s or `b`s.
  - Does not have more than one consecutive `c`.
- Example test cases with explanations:
  - Input: `a = 1, b = 1, c = 7`, Output: `"ccbccacc"`
  - Input: `a = 7, b = 1, c = 0`, Output: `"aabaa"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of `a`, `b`, and `c` and check if the resulting string is happy.
- Step-by-step breakdown of the solution:
  1. Generate all possible strings of length `a + b + c`.
  2. For each string, check if it is happy by iterating over the characters and checking for consecutive `a`s, `b`s, and `c`s.
  3. If a string is happy, update the longest happy string found so far.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it is inefficient due to the large number of possible strings.

```cpp
#include <iostream>
#include <string>
using namespace std;

string longestHappyString(int a, int b, int c) {
    string res;
    int maxLen = 0;
    for (int i = 0; i <= a + b + c; i++) {
        for (int j = 0; j <= a + b + c; j++) {
            for (int k = 0; k <= a + b + c; k++) {
                if (i + j + k == a + b + c) {
                    string s;
                    for (int m = 0; m < i; m++) s += 'a';
                    for (int m = 0; m < j; m++) s += 'b';
                    for (int m = 0; m < k; m++) s += 'c';
                    if (isHappy(s)) {
                        if (s.length() > maxLen) {
                            maxLen = s.length();
                            res = s;
                        }
                    }
                }
            }
        }
    }
    return res;
}

bool isHappy(string s) {
    int aCount = 0, bCount = 0, cCount = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'a') {
            aCount++;
            bCount = 0;
            cCount = 0;
        } else if (s[i] == 'b') {
            bCount++;
            aCount = 0;
            cCount = 0;
        } else {
            cCount++;
            aCount = 0;
            bCount = 0;
        }
        if (aCount > 2 || bCount > 2 || cCount > 1) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{a+b+c})$ because there are $2^{a+b+c}$ possible strings.
> - **Space Complexity:** $O(a+b+c)$ because we need to store the longest happy string.
> - **Why these complexities occur:** The brute force approach tries all possible strings, resulting in exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a greedy approach to construct the longest happy string.
- Detailed breakdown of the approach:
  1. Initialize an empty string `res`.
  2. While there are still characters left (`a > 0`, `b > 0`, or `c > 0`), add the character that can be added the most times without violating the happy string condition.
  3. If a character cannot be added without violating the condition, add the next character that can be added.
- Proof of optimality: The greedy approach ensures that the longest possible string is constructed by always adding the character that can be added the most times.

```cpp
string longestHappyString(int a, int b, int c) {
    string res;
    while (a > 0 || b > 0 || c > 0) {
        if (res.length() >= 2 && res[res.length() - 1] == res[res.length() - 2] && res[res.length() - 1] == 'a') {
            if (b > 0) {
                res += 'b';
                b--;
            } else if (c > 0) {
                res += 'c';
                c--;
            } else {
                break;
            }
        } else if (res.length() >= 2 && res[res.length() - 1] == res[res.length() - 2] && res[res.length() - 1] == 'b') {
            if (a > 0) {
                res += 'a';
                a--;
            } else if (c > 0) {
                res += 'c';
                c--;
            } else {
                break;
            }
        } else if (res.length() >= 1 && res[res.length() - 1] == 'c') {
            if (a > 0) {
                res += 'a';
                a--;
            } else if (b > 0) {
                res += 'b';
                b--;
            } else {
                break;
            }
        } else {
            if (a >= b && a >= c) {
                res += 'a';
                a--;
            } else if (b >= a && b >= c) {
                res += 'b';
                b--;
            } else {
                res += 'c';
                c--;
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(a+b+c)$ because we iterate over the characters once.
> - **Space Complexity:** $O(a+b+c)$ because we need to store the longest happy string.
> - **Optimality proof:** The greedy approach ensures that the longest possible string is constructed by always adding the character that can be added the most times.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, string manipulation.
- Problem-solving patterns identified: Using a greedy approach to construct the longest possible string.
- Optimization techniques learned: Avoiding unnecessary iterations by using a greedy approach.
- Similar problems to practice: Other string manipulation problems, such as finding the longest palindromic substring.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the happy string condition correctly.
- Edge cases to watch for: When `a`, `b`, or `c` is 0, the string is empty.
- Performance pitfalls: Using a brute force approach, which results in exponential time complexity.
- Testing considerations: Test the function with different inputs, including edge cases.