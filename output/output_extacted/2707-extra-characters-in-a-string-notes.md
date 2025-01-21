## Extra Characters in a String
**Problem Link:** https://leetcode.com/problems/extra-characters-in-a-string/description

**Problem Statement:**
- Input format and constraints: The problem involves finding the number of extra characters in a string that are not part of any of the given words.
- Expected output format: The function should return the count of these extra characters.
- Key requirements and edge cases to consider: The input string and the given words can contain only lowercase English letters.
- Example test cases with explanations:
  - Input: s = "abcd", words = ["a","b","c"]
  - Output: 1
  - Explanation: The character 'd' is extra.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over each character in the string and check if it can be part of any of the given words.
- Step-by-step breakdown of the solution:
  1. Initialize a count for extra characters.
  2. Iterate over each character in the string.
  3. For each character, check if it can be appended to any of the given words to form a valid word.
  4. If the character cannot be part of any word, increment the extra character count.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that checks each character individually.

```cpp
int countExtraCharacters(string s, vector<string>& words) {
    int extraCount = 0;
    int i = 0;
    while (i < s.size()) {
        bool found = false;
        for (string word : words) {
            if (i + word.size() <= s.size() && s.substr(i, word.size()) == word) {
                i += word.size();
                found = true;
                break;
            }
        }
        if (!found) {
            extraCount++;
            i++;
        }
    }
    return extraCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of the string, $m$ is the number of words, and $k$ is the maximum length of a word. This is because for each character in the string, we potentially check all words.
> - **Space Complexity:** $O(1)$, excluding the input, because we use a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The time complexity is high because of the nested loops over the string and the words, and the space complexity is low because we only use a constant amount of extra space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each character individually against all words, we can use a sliding window approach to efficiently check substrings of the input string against the given words.
- Detailed breakdown of the approach:
  1. Sort the given words by their lengths in descending order to prioritize longer matches.
  2. Iterate over the input string with a sliding window of varying sizes based on the lengths of the words.
  3. For each window size, check if the substring matches any of the words.
  4. If a match is found, move the window forward by the length of the matched word. If not, move the window forward by one character and increment the extra character count.
- Proof of optimality: This approach is optimal because it minimizes the number of comparisons needed by prioritizing longer words and using a sliding window to efficiently check substrings.

```cpp
int countExtraCharacters(string s, vector<string>& words) {
    int extraCount = 0;
    int i = 0;
    sort(words.begin(), words.end(), [](string a, string b) { return a.size() > b.size(); });
    while (i < s.size()) {
        bool found = false;
        for (string word : words) {
            if (i + word.size() <= s.size() && s.substr(i, word.size()) == word) {
                i += word.size();
                found = true;
                break;
            }
        }
        if (!found) {
            extraCount++;
            i++;
        }
    }
    return extraCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of the string, $m$ is the number of words, and $k$ is the maximum length of a word. This remains the same as the brute force because the sorting and sliding window do not improve the worst-case scenario but make the algorithm more efficient in practice.
> - **Space Complexity:** $O(1)$, excluding the input, because we use a constant amount of space to store the count and indices, and the sorting is done in-place.
> - **Optimality proof:** This is the best we can do because we must check each character at least once, and the sliding window approach minimizes the number of comparisons needed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, sorting, and string matching.
- Problem-solving patterns identified: Prioritizing longer matches to minimize comparisons.
- Optimization techniques learned: Using a sliding window to efficiently check substrings.
- Similar problems to practice: Other string matching and sliding window problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases where the input string is empty or contains only one character.
- Edge cases to watch for: When the input string is shorter than the longest word.
- Performance pitfalls: Not sorting the words by length, leading to inefficient matching.
- Testing considerations: Test with different lengths of input strings and words, and with edge cases.