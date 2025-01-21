## Count Vowel Substrings of a String

**Problem Link:** https://leetcode.com/problems/count-vowel-substrings-of-a-string/description

**Problem Statement:**
- Input format and constraints: Given a string `s`, return the number of substrings in `s` that are a vowel substring. A vowel substring is a substring that contains only vowels and has at least two different vowels.
- Expected output format: An integer representing the number of vowel substrings.
- Key requirements and edge cases to consider: Handle cases where the input string contains only one type of vowel, or when the string is empty.
- Example test cases with explanations:
  - Input: `s = "aeiou"` Output: `2` Explanation: The substrings "ae" and "ei" and "io" and "ou" and "ua" are vowel substrings.
  - Input: `s = "unicornarihan"` Output: `0` Explanation: There are no vowel substrings in the given string.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible substrings of the input string and check each one to see if it is a vowel substring.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of the input string.
  2. For each substring, check if it contains only vowels and has at least two different vowels.
  3. If a substring meets these conditions, increment a counter to keep track of the number of vowel substrings.
- Why this approach comes to mind first: It is a straightforward, intuitive approach that directly addresses the problem statement.

```cpp
#include <iostream>
#include <string>
using namespace std;

int countVowelSubstrings(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 2; j <= s.length(); j++) {
            string substr = s.substr(i, j - i);
            if (isVowelSubstr(substr)) {
                count++;
            }
        }
    }
    return count;
}

bool isVowelSubstr(string substr) {
    bool hasA = false, hasE = false, hasI = false, hasO = false, hasU = false;
    for (char c : substr) {
        if (c == 'a') hasA = true;
        else if (c == 'e') hasE = true;
        else if (c == 'i') hasI = true;
        else if (c == 'o') hasO = true;
        else if (c == 'u') hasU = true;
        else return false; // Not a vowel
    }
    int count = (hasA ? 1 : 0) + (hasE ? 1 : 0) + (hasI ? 1 : 0) + (hasO ? 1 : 0) + (hasU ? 1 : 0);
    return count >= 2; // At least two different vowels
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string, because we generate all substrings (which takes $O(n^2)$ time) and then check each one (which takes $O(n)$ time in the worst case).
> - **Space Complexity:** $O(n)$, because we need to store each substring, which can be up to $n$ characters long.
> - **Why these complexities occur:** The brute force approach is inefficient because it involves generating and checking all possible substrings, leading to a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all substrings and checking them, we can use a sliding window approach to efficiently scan the string for vowel substrings.
- Detailed breakdown of the approach:
  1. Initialize a set to keep track of the vowels in the current window.
  2. Initialize two pointers, `left` and `right`, to represent the current window.
  3. Move the `right` pointer to the right, expanding the window, and add vowels to the set.
  4. When a non-vowel character is encountered, move the `left` pointer to the right, shrinking the window, until only vowels are in the window.
  5. If the window contains at least two different vowels, increment the count of vowel substrings.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input string, resulting in a significant reduction in time complexity compared to the brute force approach.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int countVowelSubstrings(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        unordered_set<char> vowelSet;
        for (int j = i; j < s.length(); j++) {
            if (isVowel(s[j])) {
                vowelSet.insert(s[j]);
                if (vowelSet.size() >= 2) {
                    count++;
                }
            } else {
                break; // Non-vowel character, move to next window
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
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string, because in the worst case, we need to expand the window to the end of the string for each starting position.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the set of vowels in the current window.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find all vowel substrings, resulting in a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, set data structure.
- Problem-solving patterns identified: Using a set to keep track of unique elements in a window.
- Optimization techniques learned: Reducing time complexity by minimizing the number of operations required to solve the problem.
- Similar problems to practice: Other string processing problems that involve finding substrings or patterns.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty input string.
- Edge cases to watch for: Input strings containing only one type of vowel, or strings with no vowels.
- Performance pitfalls: Using inefficient algorithms or data structures, such as generating all substrings and checking them.
- Testing considerations: Thoroughly testing the solution with a variety of input cases to ensure correctness.