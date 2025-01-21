## Unique Length-3 Palindromic Subsequences
**Problem Link:** https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` containing only lowercase letters. The length of `s` is between 2 and 100. We need to find all unique length-3 palindromic subsequences.
- Expected output format: Return the number of unique length-3 palindromic subsequences.
- Key requirements and edge cases to consider: A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. A palindrome is a sequence that reads the same backward as forward. We need to handle cases where the input string has repeated characters.
- Example test cases with explanations: For example, given the string "aabca", the unique length-3 palindromic subsequences are "aba" and "aca" and "aaa".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all unique length-3 palindromic subsequences, we can generate all possible subsequences of length 3 from the input string and check if they are palindromes.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of length 3 from the input string.
  2. For each subsequence, check if it is a palindrome.
  3. If it is a palindrome, add it to a set to keep track of unique palindromic subsequences.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to generating all possible subsequences.

```cpp
#include <iostream>
#include <set>
#include <string>

int count_unique_length_3_palindromic_subsequences(const std::string& s) {
    std::set<std::string> unique_palindromes;
    int n = s.length();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                std::string subsequence = "";
                subsequence += s[i];
                subsequence += s[j];
                subsequence += s[k];
                if (subsequence[0] == subsequence[2]) {
                    unique_palindromes.insert(subsequence);
                }
            }
        }
    }
    return unique_palindromes.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. This is because we are generating all possible subsequences of length 3.
> - **Space Complexity:** $O(n^3)$, where $n$ is the length of the input string. This is because in the worst case, we may need to store all possible subsequences of length 3 in the set.
> - **Why these complexities occur:** These complexities occur because we are generating all possible subsequences of length 3 and storing them in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can iterate over the input string and for each character, we can find the number of occurrences of the same character to its left and right. This will give us the number of unique length-3 palindromic subsequences.
- Detailed breakdown of the approach:
  1. Initialize a set to keep track of unique characters to the left of the current character.
  2. Initialize a set to keep track of unique characters to the right of the current character.
  3. For each character in the input string, iterate over the characters to its left and add them to the left set.
  4. For each character in the input string, iterate over the characters to its right and add them to the right set.
  5. For each character in the input string, calculate the number of unique length-3 palindromic subsequences by multiplying the size of the left set with the size of the right set.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal because we need to at least read the input string once.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

int count_unique_length_3_palindromic_subsequences(const std::string& s) {
    int n = s.length();
    int count = 0;
    for (int i = 0; i < n; i++) {
        std::unordered_set<char> left_chars;
        std::unordered_set<char> right_chars;
        for (int j = 0; j < i; j++) {
            left_chars.insert(s[j]);
        }
        for (int j = i + 1; j < n; j++) {
            right_chars.insert(s[j]);
        }
        for (const auto& left_char : left_chars) {
            if (right_chars.count(left_char)) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we are iterating over the input string and for each character, we are iterating over the characters to its left and right.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are using two sets to keep track of unique characters to the left and right of the current character.
> - **Optimality proof:** This approach is optimal because we need to at least read the input string once to find all unique length-3 palindromic subsequences.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of generating all possible subsequences and checking if they are palindromes.
- Problem-solving patterns identified: The problem requires iterating over the input string and using sets to keep track of unique characters.
- Optimization techniques learned: The problem demonstrates how to optimize the solution by using sets to keep track of unique characters.
- Similar problems to practice: Other problems that involve generating all possible subsequences and checking if they are palindromes.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a subsequence is a palindrome before adding it to the set.
- Edge cases to watch for: Handling cases where the input string has repeated characters.
- Performance pitfalls: Not using sets to keep track of unique characters, which can lead to a high time complexity.
- Testing considerations: Testing the solution with different input strings and edge cases to ensure it works correctly.