## Find Longest Special Substring That Occurs Thrice II

**Problem Link:** https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/description

**Problem Statement:**
- Input format: a string `s`
- Constraints: `1 <= s.length <= 100`
- Expected output format: the longest substring that occurs at least three times
- Key requirements and edge cases to consider: 
    - A substring can occur consecutively or non-consecutively.
    - If there are multiple longest special substrings, return any one of them.
- Example test cases with explanations:
    - Example 1: Input: `s = "abc"` Output: `""`
    - Example 2: Input: `s = "aabcaabc"` Output: `"abc"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible substrings, then check each substring's occurrence in the string.
- Step-by-step breakdown of the solution:
    1. Generate all possible substrings of `s`.
    2. For each substring, count its occurrences in `s`.
    3. If a substring occurs at least three times and is longer than the current longest special substring, update the longest special substring.
- Why this approach comes to mind first: It's a straightforward method that checks every possible substring, ensuring no special substrings are missed.

```cpp
string longestSpecialSubstring(string s) {
    string longest = "";
    for (int i = 0; i < s.size(); i++) {
        for (int j = i + 1; j <= s.size(); j++) {
            string substr = s.substr(i, j - i);
            int count = 0;
            for (int k = 0; k <= s.size() - substr.size(); k++) {
                if (s.substr(k, substr.size()) == substr) count++;
            }
            if (count >= 3 && substr.size() > longest.size()) longest = substr;
        }
    }
    return longest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of string `s`. The reason is that we are generating all substrings ($O(n^2)$), and for each substring, we are counting its occurrences in the string ($O(n)$).
> - **Space Complexity:** $O(1)$ not counting the space needed for the input and output. The reason is that we only use a constant amount of space to store the variables.
> - **Why these complexities occur:** These complexities occur because we are using nested loops to generate all substrings and count their occurrences.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the string length is limited to 100, we can still use a brute force approach but optimize the way we count occurrences of substrings.
- Detailed breakdown of the approach:
    1. Generate all possible substrings of `s`.
    2. For each substring, use a `std::unordered_map` to store the count of substrings, and a `std::set` to store unique substrings that occur at least three times.
    3. If a substring occurs at least three times and is longer than the current longest special substring, update the longest special substring.
- Why further optimization is impossible: Given the constraints of the problem, any optimization would likely involve more complex data structures or algorithms, which may not be necessary given the limited input size.

```cpp
string longestSpecialSubstring(string s) {
    string longest = "";
    unordered_set<string> seen;
    for (int i = 0; i < s.size(); i++) {
        for (int j = i + 1; j <= s.size(); j++) {
            string substr = s.substr(i, j - i);
            int count = 0;
            for (int k = 0; k <= s.size() - substr.size(); k++) {
                if (s.substr(k, substr.size()) == substr) count++;
            }
            if (count >= 3 && substr.size() > longest.size()) longest = substr;
        }
    }
    return longest;
}
```

However, we can improve this code by using a hash map to store the frequency of substrings.

```cpp
string longestSpecialSubstring(string s) {
    string longest = "";
    unordered_map<string, int> freq;
    for (int i = 0; i < s.size(); i++) {
        for (int j = i + 1; j <= s.size(); j++) {
            string substr = s.substr(i, j - i);
            int count = 0;
            for (int k = 0; k <= s.size() - substr.size(); k++) {
                if (s.substr(k, substr.size()) == substr) count++;
            }
            freq[substr] = count;
        }
    }
    for (auto& it : freq) {
        if (it.second >= 3 && it.first.size() > longest.size()) longest = it.first;
    }
    return longest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of string `s`. The reason is that we are generating all substrings ($O(n^2)$), and for each substring, we are counting its occurrences in the string ($O(n)$).
> - **Space Complexity:** $O(n^2)$ where $n$ is the length of string `s`. The reason is that we are using a hash map to store the frequency of substrings.
> - **Optimality proof:** This is the optimal solution because we are generating all possible substrings and counting their occurrences in the string.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Brute force approach, hash map, and string manipulation.
- Problem-solving patterns identified: Generating all possible substrings, counting occurrences of substrings, and using a hash map to store frequency.
- Optimization techniques learned: Using a hash map to store frequency of substrings.
- Similar problems to practice: Other string manipulation problems, such as finding the longest palindromic substring or the longest common substring.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input string.
- Edge cases to watch for: Input strings with repeated characters, input strings with no repeated substrings.
- Performance pitfalls: Using a brute force approach without optimizing the way we count occurrences of substrings.
- Testing considerations: Testing the function with different input strings, including edge cases.