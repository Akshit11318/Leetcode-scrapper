## Score of a String
**Problem Link:** https://leetcode.com/problems/score-of-a-string/description

**Problem Statement:**
- Input: A binary string `s`.
- Constraints: `1 <= s.length <= 500`.
- Expected Output: An integer representing the score of the string.
- Key Requirements: The score of a string is the number of non-empty substrings that start and end with the same character.
- Edge Cases: Consider strings with only one character, strings with alternating characters, and strings with repeated sequences.

**Example Test Cases:**
- Input: `s = "aba"` - Output: `6` (Substrings: "a", "ab", "aba", "b", "ba")
- Input: `s = "aaa"` - Output: `6` (Substrings: "a", "aa", "aaa")

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible substrings and count those that start and end with the same character.
- Step-by-step breakdown:
  1. Generate all substrings of the input string.
  2. For each substring, check if the first and last characters are the same.
  3. If they are, increment the score counter.

```cpp
int scoreOfStrings(string s) {
    int score = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string substring = s.substr(i, j - i);
            if (substring[0] == substring[substring.length() - 1]) {
                score++;
            }
        }
    }
    return score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of the string, due to generating all substrings and checking each one.
> - **Space Complexity:** $O(n)$ for storing the substrings.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate substrings and then checks each substring, leading to cubic time complexity. The space complexity is linear due to the storage of substrings.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all substrings, observe the pattern of how the score increases as we extend the string from left to right.
- Detailed breakdown:
  1. Initialize a score counter to 0.
  2. Iterate over the string, maintaining a count of the current character and the total count of all characters seen so far.
  3. For each character, calculate the number of substrings that end with this character and start with the same character, considering all previous occurrences of this character.

```cpp
int scoreOfStrings(string s) {
    int n = s.length();
    int score = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (s[i] == s[j]) {
                score++;
            }
        }
    }
    return score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the string, due to the nested loops over the string.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Optimality proof:** This approach directly counts the substrings that start and end with the same character without generating all substrings, making it more efficient than the brute force approach. Further optimization is challenging due to the inherent need to consider all substrings.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, substring generation, and character counting.
- Problem-solving patterns identified: Avoiding brute force by finding patterns or shortcuts in the problem.
- Optimization techniques learned: Reducing the number of iterations and avoiding unnecessary operations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect substring generation, failure to handle edge cases.
- Edge cases to watch for: Empty strings, strings with a single character, and strings with repeated sequences.
- Performance pitfalls: Using inefficient algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing with various input sizes and edge cases to ensure correctness and performance.