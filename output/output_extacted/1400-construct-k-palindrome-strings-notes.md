## Construct K Palindrome Strings
**Problem Link:** https://leetcode.com/problems/construct-k-palindrome-strings/description

**Problem Statement:**
- Input format and constraints: Given a string `s` and an integer `k`, determine if it is possible to construct `k` palindrome strings from the characters of `s`.
- Expected output format: Return `true` if it is possible to construct `k` palindrome strings, otherwise return `false`.
- Key requirements and edge cases to consider: The input string `s` can contain any characters, and `k` is a positive integer.
- Example test cases with explanations: For example, given `s = "annabelle"` and `k = 2`, the output should be `true` because we can construct two palindrome strings "anna" and "elle". However, given `s = "abc"` and `k = 3`, the output should be `false` because we cannot construct three palindrome strings from the characters of "abc".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible combinations of characters from the input string `s` and check if each combination forms a palindrome string.
- Step-by-step breakdown of the solution: 
  1. Generate all possible combinations of characters from the input string `s`.
  2. For each combination, check if it forms a palindrome string.
  3. If we can find `k` combinations that form palindrome strings, return `true`.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs because it generates all possible combinations of characters.

```cpp
#include <iostream>
#include <vector>
#include <string>

bool canConstruct(string s, int k) {
    int n = s.size();
    vector<int> count(26, 0);
    for (char c : s) {
        count[c - 'a']++;
    }
    int oddCount = 0;
    for (int i = 0; i < 26; i++) {
        if (count[i] % 2 != 0) {
            oddCount++;
        }
    }
    return k <= n && oddCount <= k;
}

int main() {
    string s = "annabelle";
    int k = 2;
    cout << boolalpha << canConstruct(s, k) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input string `s`. We iterate over the input string once to count the frequency of each character.
> - **Space Complexity:** $O(1)$ because we use a fixed-size array to store the frequency of each character.
> - **Why these complexities occur:** The time complexity is linear because we only iterate over the input string once, and the space complexity is constant because we use a fixed-size array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can determine if it is possible to construct `k` palindrome strings by counting the frequency of each character in the input string `s`.
- Detailed breakdown of the approach: 
  1. Count the frequency of each character in the input string `s`.
  2. Calculate the number of characters that have an odd count. A palindrome string can have at most one character with an odd count (the middle character).
  3. If the number of characters with an odd count is less than or equal to `k`, we can construct `k` palindrome strings.
- Proof of optimality: This approach is optimal because it only requires a single pass over the input string to count the frequency of each character.
- Why further optimization is impossible: We must iterate over the input string at least once to count the frequency of each character, so we cannot improve the time complexity further.

```cpp
#include <iostream>
#include <vector>
#include <string>

bool canConstruct(string s, int k) {
    int n = s.size();
    vector<int> count(26, 0);
    for (char c : s) {
        count[c - 'a']++;
    }
    int oddCount = 0;
    for (int i = 0; i < 26; i++) {
        if (count[i] % 2 != 0) {
            oddCount++;
        }
    }
    return k <= n && oddCount <= k;
}

int main() {
    string s = "annabelle";
    int k = 2;
    cout << boolalpha << canConstruct(s, k) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input string `s`. We iterate over the input string once to count the frequency of each character.
> - **Space Complexity:** $O(1)$ because we use a fixed-size array to store the frequency of each character.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the input string to count the frequency of each character.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting the frequency of each character in a string, determining if a string can be divided into palindrome substrings.
- Problem-solving patterns identified: Using a fixed-size array to store the frequency of each character, calculating the number of characters with an odd count.
- Optimization techniques learned: Reducing the problem to a single pass over the input string, using a fixed-size array to store the frequency of each character.
- Similar problems to practice: Determining if a string can be divided into anagrams, finding the longest palindrome substring in a string.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the count array, not checking if the number of characters with an odd count is less than or equal to `k`.
- Edge cases to watch for: Empty input string, `k` is greater than the length of the input string.
- Performance pitfalls: Using a dynamic-size array to store the frequency of each character, iterating over the input string multiple times.
- Testing considerations: Testing with different input strings, testing with different values of `k`.