## Longest Nice Substring
**Problem Link:** https://leetcode.com/problems/longest-nice-substring/description

**Problem Statement:**
- Input format: a string `s` consisting of lowercase English letters.
- Constraints: `1 <= s.length <= 100`.
- Expected output format: the longest nice substring of `s`. If there are multiple, return the one with the smallest starting index. If there are multiple answers with the same length, return the one with the smallest starting index.
- Key requirements: a string is nice if it has exactly one of each of the characters `a-z` (case-insensitive) and all the characters in the string are used.
- Edge cases: empty string, single character string, string with all characters the same.

**Example Test Cases:**
- Input: `s = "ybcde"`; Output: `"bcde"`.
- Input: `s = "dabcbc"`; Output: `"dabc"`.
- Input: `s = "abcd"`; Output: `"abcd"`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible substrings of the given string and check if each substring is nice.
- Step-by-step breakdown:
  1. Generate all possible substrings.
  2. For each substring, check if it is nice by verifying that it contains exactly one of each character and all characters in the substring are used.
  3. Keep track of the longest nice substring found so far.
- Why this approach comes to mind first: it is straightforward and ensures that all possible substrings are considered.

```cpp
#include <iostream>
#include <string>
using namespace std;

string longestNiceSubstring(string s) {
    int n = s.length();
    string longest = "";
    
    // Generate all possible substrings
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substr = s.substr(i, j - i);
            
            // Check if the substring is nice
            if (isNice(substr)) {
                if (substr.length() > longest.length()) {
                    longest = substr;
                }
            }
        }
    }
    
    return longest;
}

bool isNice(string s) {
    int n = s.length();
    int count[26] = {0};
    
    // Count the occurrences of each character
    for (char c : s) {
        count[tolower(c) - 'a']++;
    }
    
    // Check if the substring is nice
    for (int i = 0; i < 26; i++) {
        if (count[i] > 1) {
            return false;
        }
    }
    
    // Check if all characters in the substring are used
    for (char c : s) {
        if (count[tolower(c) - 'a'] == 0) {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. The outer two loops generate all possible substrings, and the inner loop checks if each substring is nice.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. The space complexity comes from the substrings generated.
> - **Why these complexities occur:** The brute force approach generates all possible substrings and checks each one, resulting in high time and space complexities.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a bitmask to represent the characters in the substring.
- Step-by-step breakdown:
  1. Iterate over all possible substrings.
  2. For each substring, use a bitmask to represent the characters in the substring.
  3. Check if the substring is nice by verifying that the bitmask has exactly one bit set for each character.
- Proof of optimality: this approach ensures that all possible substrings are considered and that the nice substrings are identified efficiently.

```cpp
string longestNiceSubstring(string s) {
    int n = s.length();
    string longest = "";
    
    // Iterate over all possible substrings
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substr = s.substr(i, j - i);
            
            // Use a bitmask to represent the characters in the substring
            int bitmask = 0;
            for (char c : substr) {
                bitmask |= 1 << (tolower(c) - 'a');
            }
            
            // Check if the substring is nice
            if (isNice(bitmask, substr)) {
                if (substr.length() > longest.length()) {
                    longest = substr;
                }
            }
        }
    }
    
    return longest;
}

bool isNice(int bitmask, string s) {
    int n = s.length();
    int count = 0;
    
    // Count the number of bits set in the bitmask
    for (int i = 0; i < 26; i++) {
        if ((bitmask >> i) & 1) {
            count++;
        }
    }
    
    // Check if the substring is nice
    return count == n;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. The outer two loops generate all possible substrings.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. The space complexity comes from the substrings generated.
> - **Optimality proof:** This approach ensures that all possible substrings are considered and that the nice substrings are identified efficiently, resulting in optimal time and space complexities.

---

### Final Notes

**Learning Points:**
- The importance of using bitmasks to represent character sets.
- The need to consider all possible substrings when solving string problems.
- The use of iterative approaches to solve string problems.

**Mistakes to Avoid:**
- Not considering all possible substrings.
- Not using bitmasks to represent character sets.
- Not optimizing the solution for time and space complexity.