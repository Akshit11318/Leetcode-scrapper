## Longest Palindrome
**Problem Link:** https://leetcode.com/problems/longest-palindrome/description

**Problem Statement:**
- Input: A string `s` containing only letters and digits.
- Constraints: The string `s` can be empty or contain up to 1000 characters.
- Expected Output: The length of the longest palindrome that can be built using the characters of `s`.
- Key Requirements:
  - A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
  - We can use each character in `s` only as many times as it appears in `s`.
- Example Test Cases:
  - Input: `s = "abccccdd"`
    - Output: `8`
    - Explanation: The longest palindrome is `"dccbacd"`.
  - Input: `s = "a"`
    - Output: `1`
    - Explanation: The longest palindrome is `"a"`.

---

### Brute Force Approach

**Explanation:**
- Initial Thought Process: Generate all possible palindromes and check which one is the longest.
- Step-by-Step Breakdown:
  1. Generate all permutations of the input string `s`.
  2. For each permutation, check if it is a palindrome.
  3. Keep track of the length of the longest palindrome found.
- Why This Approach Comes to Mind First: It's a straightforward approach that checks all possibilities.

```cpp
#include <iostream>
#include <string>
#include <algorithm>

bool isPalindrome(const std::string& s) {
    int left = 0;
    int right = s.length() - 1;
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int longestPalindrome(const std::string& s) {
    int maxLength = 0;
    do {
        if (isPalindrome(s)) {
            maxLength = std::max(maxLength, (int)s.length());
        }
    } while (std::next_permutation(s.begin(), s.end()));
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of the string `s`. This is because we generate all permutations of `s`.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we need to store the current permutation.
> - **Why These Complexities Occur:** Generating all permutations of a string of length $n$ results in $n!$ permutations, leading to a time complexity of $O(n!)$. The space complexity is $O(n)$ because we need to store the current permutation.

---

### Optimal Approach (Required)

**Explanation:**
- Key Insight: A palindrome can have at most one character that appears an odd number of times. All other characters must appear in pairs.
- Detailed Breakdown:
  1. Count the frequency of each character in the string `s`.
  2. Initialize a variable `length` to 0, which will store the length of the longest palindrome.
  3. Iterate over the frequency counts. For each character:
    - If the frequency is even, add it to `length`.
    - If the frequency is odd, add `frequency - 1` to `length` and set a flag `hasOdd` to `true`.
  4. If `hasOdd` is `true`, increment `length` by 1 (because we can add the single character to the middle of the palindrome).
- Proof of Optimality: This approach considers all possible palindromes that can be formed using the characters of `s` and chooses the longest one.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int longestPalindrome(const std::string& s) {
    std::unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    
    int length = 0;
    bool hasOdd = false;
    for (const auto& pair : freq) {
        if (pair.second % 2 == 0) {
            length += pair.second;
        } else {
            length += pair.second - 1;
            hasOdd = true;
        }
    }
    
    if (hasOdd) {
        length++;
    }
    
    return length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we iterate over the string once to count the frequency of each character.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we need to store the frequency counts.
> - **Optimality Proof:** This approach considers all possible palindromes that can be formed using the characters of `s` and chooses the longest one, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key Algorithmic Concepts: Counting frequency, iterating over a map, and considering edge cases.
- Problem-Solving Patterns: Identifying the key insight that leads to the optimal solution.
- Optimization Techniques: Avoiding unnecessary iterations and using a flag to simplify the code.

**Mistakes to Avoid:**
- Common Implementation Errors: Not considering the case where a character appears an odd number of times.
- Edge Cases: Not handling the case where the input string is empty.
- Performance Pitfalls: Not using a map to count the frequency of each character, resulting in a higher time complexity.
- Testing Considerations: Testing the function with different input strings, including empty strings and strings with only one character.