## Find Mirror Score of a String
**Problem Link:** https://leetcode.com/problems/find-mirror-score-of-a-string/description

**Problem Statement:**
- Input format: a string `s` containing lowercase English letters.
- Constraints: `1 <= s.length <= 100`.
- Expected output format: the mirror score of the string.
- Key requirements: calculate the mirror score by comparing the string with its reverse.
- Edge cases: consider the case when the input string is a palindrome.

**Example Test Cases:**
- Input: `s = "aba"`
  Output: `2`
  Explanation: The mirror score of "aba" is 2 because "aba" spelled backwards is "aba", and 2 characters match.
- Input: `s = "abc"`
  Output: `0`
  Explanation: The mirror score of "abc" is 0 because "abc" spelled backwards is "cba", and no characters match.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves comparing each character of the string with the corresponding character in its reverse.
- Step-by-step breakdown:
  1. Reverse the input string.
  2. Iterate over the characters in the original string and compare them with the characters in the reversed string.
  3. Increment a counter for each matching character.
- This approach comes to mind first because it directly addresses the problem statement.

```cpp
int mirrorScore(string s) {
    int n = s.length();
    string reversed = s;
    reverse(reversed.begin(), reversed.end());
    int score = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == reversed[i]) {
            score++;
        }
    }
    return score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we iterate over the string once to reverse it and once to compare characters.
> - **Space Complexity:** $O(n)$, because we create a reversed copy of the input string.
> - **Why these complexities occur:** The time complexity is linear due to the iteration over the string, and the space complexity is also linear because we need to store the reversed string.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is that we can compare characters from the start and end of the string, moving towards the center, without actually reversing the string.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one at the start and one at the end of the string.
  2. Compare the characters at the current positions of the pointers.
  3. If the characters match, increment the mirror score.
  4. Move the pointers towards the center of the string.
- Proof of optimality: This approach is optimal because it achieves the same result as the brute force approach but with reduced space complexity, as it does not require creating a reversed copy of the string.

```cpp
int mirrorScore(string s) {
    int n = s.length();
    int score = 0;
    for (int i = 0; i < n / 2; i++) {
        if (s[i] == s[n - i - 1]) {
            score++;
        }
    }
    // If the string has an odd length, the middle character is always a match
    if (n % 2 == 1) {
        score++;
    }
    return score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we iterate over half of the string.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the pointers and the score.
> - **Optimality proof:** This approach is optimal because it minimizes both time and space complexity by avoiding the creation of a reversed string and only iterating over half of the string.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: two-pointer technique, string manipulation.
- Problem-solving patterns identified: comparing characters from the start and end of a string.
- Optimization techniques learned: reducing space complexity by avoiding unnecessary string operations.
- Similar problems to practice: string manipulation and comparison problems.

**Mistakes to Avoid:**
- Common implementation errors: off-by-one errors when iterating over the string.
- Edge cases to watch for: handling strings of odd length correctly.
- Performance pitfalls: using inefficient string reversal methods.
- Testing considerations: testing with strings of varying lengths and contents.