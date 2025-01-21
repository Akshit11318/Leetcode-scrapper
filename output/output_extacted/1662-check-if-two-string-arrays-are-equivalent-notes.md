## Check If Two String Arrays Are Equivalent
**Problem Link:** https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description

**Problem Statement:**
- Input format and constraints: Two string arrays `word1` and `word2`.
- Expected output format: A boolean indicating whether the two arrays are equivalent.
- Key requirements and edge cases to consider: 
  - The arrays can be of different lengths.
  - The strings within the arrays can be of different lengths.
  - The order of the strings and characters matters.
- Example test cases with explanations:
  - `word1 = ["ab", "c"]`, `word2 = ["a", "bc"]` should return `true` because when concatenated, both arrays form the same string `"abc"`.
  - `word1 = ["a", "cb"]`, `word2 = ["ab", "c"]` should return `false` because the concatenated strings are different.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Concatenate all strings in both arrays and compare the resulting strings.
- Step-by-step breakdown of the solution:
  1. Initialize two empty strings to store the concatenated strings from `word1` and `word2`.
  2. Iterate through each string in `word1` and `word2`, concatenating them to their respective strings.
  3. Compare the two concatenated strings for equality.
- Why this approach comes to mind first: It directly addresses the problem statement by comparing the arrays after making them comparable.

```cpp
class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string str1, str2;
        // Concatenate all strings in word1
        for (const auto& word : word1) {
            str1 += word;
        }
        // Concatenate all strings in word2
        for (const auto& word : word2) {
            str2 += word;
        }
        // Compare the concatenated strings
        return str1 == str2;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the total number of characters in `word1` and $m$ is the total number of characters in `word2`. This is because we iterate through each character in both arrays once.
> - **Space Complexity:** $O(n + m)$, because we create two new strings that store the concatenated strings from `word1` and `word2`.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each character in the input arrays. The space complexity is also linear because the size of the output strings is directly proportional to the size of the input.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of concatenating all strings first and then comparing, we can compare the strings character by character as we concatenate them. This approach avoids creating additional strings and thus reduces memory usage.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one for each array, to keep track of the current string and character index in that string.
  2. Iterate through the characters of the strings in `word1` and `word2` simultaneously, comparing them.
  3. If a mismatch is found, immediately return `false`.
  4. If one array is exhausted before the other and there are remaining characters in the other array, return `false`.
  5. If both arrays are fully traversed without finding any mismatches, return `true`.
- Proof of optimality: This approach has the same time complexity as the brute force approach but reduces the space complexity by avoiding the creation of additional strings.

```cpp
class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        int i = 0, j = 0; // Array indices
        int p = 0, q = 0; // String indices within the arrays
        
        while (i < word1.size() && j < word2.size()) {
            if (word1[i][p] != word2[j][q]) {
                return false;
            }
            p++; q++;
            if (p == word1[i].size()) {
                i++; p = 0;
            }
            if (q == word2[j].size()) {
                j++; q = 0;
            }
        }
        
        // Check if one array has remaining characters
        return i == word1.size() && j == word2.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are as defined before. This remains the same as the brute force approach because we still examine each character once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input arrays, because we only use a constant amount of space to store our pointers and indices.
> - **Optimality proof:** This is optimal because we have reduced the space complexity to constant while maintaining the same time complexity as the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and pointer management.
- Problem-solving patterns identified: Reducing memory usage by avoiding unnecessary string concatenation.
- Optimization techniques learned: Using pointers to iterate through strings without creating additional strings.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the end of strings or arrays, leading to out-of-bounds errors.
- Edge cases to watch for: Empty arrays or strings, arrays of different lengths.
- Performance pitfalls: Creating unnecessary intermediate data structures, such as strings.
- Testing considerations: Ensure to test with arrays of varying lengths, including empty arrays, and with strings of different lengths.