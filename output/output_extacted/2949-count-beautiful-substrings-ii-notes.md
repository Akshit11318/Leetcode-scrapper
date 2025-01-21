## Count Beautiful Substrings II
**Problem Link:** https://leetcode.com/problems/count-beautiful-substrings-ii/description

**Problem Statement:**
- Input format: a string `s` containing lowercase English letters.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output format: the number of beautiful substrings of `s`.
- Key requirements and edge cases to consider: a substring is considered beautiful if it has at least one vowel and no two vowels are the same.
- Example test cases with explanations: 
    - Input: `s = "aeiou#aa"`
    - Output: `16`
    - Explanation: There are 16 beautiful substrings in `s`: `a`, `e`, `i`, `o`, `u`, `ae`, `ai`, `ao`, `au`, `ea`, `ei`, `eo`, `eu`, `ia`, `ie`, `io`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: generate all possible substrings of `s`, then check each substring to see if it's beautiful.
- Step-by-step breakdown of the solution:
    1. Generate all possible substrings of `s`.
    2. For each substring, check if it contains at least one vowel.
    3. If it does, check if any two vowels are the same.
    4. If not, increment the count of beautiful substrings.
- Why this approach comes to mind first: it's a straightforward, brute-force solution that checks every possible substring.

```cpp
int countBeautifulSubstrings(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string substring = s.substr(i, j - i);
            if (isBeautiful(substring)) {
                count++;
            }
        }
    }
    return count;
}

bool isBeautiful(string substring) {
    bool hasVowel = false;
    unordered_set<char> vowels;
    for (char c : substring) {
        if (isVowel(c)) {
            hasVowel = true;
            if (vowels.find(c) != vowels.end()) {
                return false;
            }
            vowels.insert(c);
        }
    }
    return hasVowel;
}

bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `s`. This is because we generate all possible substrings ($O(n^2)$), and for each substring, we check if it's beautiful ($O(n)$).
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`. This is because we store each substring in memory.
> - **Why these complexities occur:** The brute-force approach generates all possible substrings, which leads to a high time complexity. The space complexity is relatively low because we only store each substring in memory for a short time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: instead of generating all possible substrings, we can use a sliding window approach to check all substrings in one pass.
- Detailed breakdown of the approach:
    1. Initialize two pointers, `left` and `right`, to the start of `s`.
    2. Move `right` to the right, expanding the window.
    3. For each position of `right`, check if the substring from `left` to `right` is beautiful.
    4. If it is, increment the count of beautiful substrings.
    5. Move `left` to the right, shrinking the window, until the substring is no longer beautiful.
- Proof of optimality: this approach checks all possible substrings in one pass, without generating them all explicitly.

```cpp
int countBeautifulSubstrings(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        unordered_set<char> vowels;
        for (int j = i; j < s.length(); j++) {
            if (isVowel(s[j])) {
                if (vowels.find(s[j]) != vowels.end()) {
                    break;
                }
                vowels.insert(s[j]);
            }
            if (!vowels.empty()) {
                count++;
            }
        }
    }
    return count;
}

bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `s`. This is because we use a nested loop to check all substrings.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`. This is because we store the vowels in the current substring in a set.
> - **Optimality proof:** This approach checks all possible substrings in one pass, without generating them all explicitly, which makes it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sliding window approach, use of sets to keep track of unique elements.
- Problem-solving patterns identified: optimizing brute-force solutions by reducing the number of operations.
- Optimization techniques learned: using a sliding window approach to reduce the time complexity.
- Similar problems to practice: other problems involving substrings, such as finding the longest palindromic substring.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as an empty input string.
- Edge cases to watch for: substrings with no vowels, substrings with duplicate vowels.
- Performance pitfalls: using a brute-force approach that generates all possible substrings.
- Testing considerations: testing with different input strings, including edge cases.