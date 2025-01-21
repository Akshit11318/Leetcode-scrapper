## Count Unique Characters of All Substrings of a Given String

**Problem Link:** https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` of length `n`. The string consists of lowercase English letters.
- Expected output format: The output should be the total number of unique characters in all substrings of the input string.
- Key requirements and edge cases to consider: The input string can be empty, and we need to handle this edge case. Also, we should consider that the input string can contain duplicate characters.
- Example test cases with explanations:
  - Example 1: Input: `s = "ABC"` Output: `10` Explanation: All substrings are "A", "AB", "ABC", "B", "BC", "C". There are 10 unique characters in these substrings.
  - Example 2: Input: `s = "ABA"` Output: `8` Explanation: All substrings are "A", "AB", "ABA", "B", "BA", "A". There are 8 unique characters in these substrings.
  - Example 3: Input: `s = "LEETCODE"` Output: `92` Explanation: All substrings are "L", "LE", "LEE", "LEET", "LEETC", "LEETCO", "LEETCOD", "LEETCODE", "E", "EE", "EET", "EETC", "EETCO", "EETCOD", "EETCODE", "T", "TC", "TCO", "TCOD", "TCODE", "C", "CO", "COD", "CODE", "O", "OD", "ODE", "D", "DE", "E". There are 92 unique characters in these substrings.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a brute force approach to generate all substrings of the input string and then count the unique characters in each substring.
- Step-by-step breakdown of the solution:
  1. Generate all substrings of the input string.
  2. For each substring, count the unique characters.
  3. Sum up the counts of unique characters for all substrings.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large input strings.

```cpp
int uniqueLetterString(string s) {
    int n = s.length();
    int res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            unordered_set<char> unique_chars;
            for (int k = i; k <= j; k++) {
                unique_chars.insert(s[k]);
            }
            res += unique_chars.size();
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. This is because we have three nested loops: two loops to generate all substrings and one loop to count the unique characters in each substring.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we use an unordered set to store the unique characters in each substring, and the maximum size of the set is $n$.
> - **Why these complexities occur:** The time complexity occurs because we use three nested loops, and the space complexity occurs because we use an unordered set to store the unique characters in each substring.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a different approach to calculate the number of unique characters in all substrings. For each character in the string, we can calculate the number of substrings that contain this character and the number of substrings that do not contain this character.
- Detailed breakdown of the approach:
  1. Initialize a variable `res` to store the total count of unique characters.
  2. For each character `c` in the string, calculate the number of substrings that contain `c`.
  3. For each character `c` in the string, calculate the number of substrings that do not contain `c`.
  4. Sum up the counts of unique characters for all characters.
- Why further optimization is impossible: This approach is optimal because we only need to iterate through the string once to calculate the counts of unique characters for all characters.

```cpp
int uniqueLetterString(string s) {
    int n = s.length();
    int res = 0;
    for (int i = 0; i < n; i++) {
        int left = i;
        int right = i;
        while (left >= 0 && s[left] != s[i]) left--;
        while (right < n && s[right] != s[i]) right++;
        res += (i - left) * (right - i);
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we have two nested loops: one loop to iterate through the string and one loop to calculate the number of substrings that contain each character.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input string. This is because we only use a constant amount of space to store the counts of unique characters.
> - **Optimality proof:** This approach is optimal because we only need to iterate through the string once to calculate the counts of unique characters for all characters.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of counting unique characters in all substrings of a given string.
- Problem-solving patterns identified: The problem requires the use of a different approach to calculate the number of unique characters in all substrings.
- Optimization techniques learned: The problem requires the use of optimization techniques to reduce the time complexity of the solution.
- Similar problems to practice: Similar problems include counting the number of unique characters in a given string, counting the number of substrings that contain a given character, and counting the number of substrings that do not contain a given character.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use a brute force approach to generate all substrings and count the unique characters in each substring.
- Edge cases to watch for: An edge case to watch for is an empty input string.
- Performance pitfalls: A performance pitfall is to use a solution with a high time complexity, such as $O(n^3)$.
- Testing considerations: A testing consideration is to test the solution with different input strings, including empty strings and strings with duplicate characters.