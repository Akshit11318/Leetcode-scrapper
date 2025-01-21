## Greatest English Letter in Upper and Lower Case
**Problem Link:** https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/description

**Problem Statement:**
- Input format: A string `s` containing a mix of uppercase and lowercase English letters.
- Constraints: The input string `s` is non-empty and only contains English letters.
- Expected output format: The greatest English letter that appears in both uppercase and lowercase in `s`, or an empty string if no such letter exists.
- Key requirements and edge cases to consider:
  - Handling strings with no matching uppercase and lowercase letters.
  - Finding the greatest letter when there are multiple matches.
- Example test cases with explanations:
  - For the input "nZnZnBbCbcb", the output should be "Z".
  - For the input "dDzeEeEeZhYcCcApApAaAaAa", the output should be "d".
  - For the input "aAaAaAaAa", the output should be "a".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each character in the string, checking for both uppercase and lowercase versions of each letter.
- Step-by-step breakdown of the solution:
  1. Create a set to store unique letters found in both uppercase and lowercase.
  2. Iterate through the string, checking each character against all others to find matches.
  3. If a match is found (both uppercase and lowercase of the same letter), add it to the set.
  4. After iterating through the entire string, find the maximum letter in the set, which represents the greatest English letter appearing in both cases.
- Why this approach comes to mind first: It's straightforward and ensures that all possible combinations are considered, but it's inefficient due to its high time complexity.

```cpp
string greatestLetterInBothCases(string s) {
    unordered_set<char> found;
    for (int i = 0; i < s.size(); ++i) {
        for (int j = 0; j < s.size(); ++j) {
            if (i != j && tolower(s[i]) == tolower(s[j]) && (isupper(s[i]) && islower(s[j]) || islower(s[i]) && isupper(s[j]))) {
                found.insert(tolower(s[i]));
            }
        }
    }
    if (found.empty()) return "";
    char maxChar = *found.begin();
    for (char c : found) {
        if (c > maxChar) maxChar = c;
    }
    return string(1, toupper(maxChar));
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string, because we're using nested loops to compare each character with every other character.
> - **Space Complexity:** $O(n)$, because in the worst case, all characters could be stored in the set.
> - **Why these complexities occur:** The brute force approach checks every pair of characters, leading to a quadratic time complexity, and stores unique letters, leading to a linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing each character with every other, we can use two arrays (or vectors) to track the occurrence of uppercase and lowercase letters separately.
- Detailed breakdown of the approach:
  1. Initialize two boolean arrays, `lower` and `upper`, of size 26, representing the 26 English letters. These arrays will track whether a lowercase or uppercase letter has been seen.
  2. Iterate through the string once. For each character, mark the corresponding index in either the `lower` or `upper` array as true, depending on the case of the character.
  3. After the iteration, start from the end of the arrays (representing 'z' and 'Z') and move backwards. The first index where both `lower` and `upper` are true represents the greatest English letter that appears in both cases.
- Proof of optimality: This approach has a linear time complexity because it only requires a single pass through the string, making it more efficient than the brute force approach.

```cpp
string greatestLetterInBothCases(string s) {
    vector<bool> lower(26, false), upper(26, false);
    for (char c : s) {
        if (islower(c)) lower[c - 'a'] = true;
        else upper[c - 'A'] = true;
    }
    for (int i = 25; i >= 0; --i) {
        if (lower[i] && upper[i]) return string(1, 'A' + i);
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we're making a single pass through the string.
> - **Space Complexity:** $O(1)$, because the size of the boolean arrays is constant (26), regardless of the input size.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to solve the problem, achieving a linear time complexity with constant space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of reducing the number of comparisons and using data structures like arrays or vectors to track occurrences.
- Problem-solving patterns identified: Looking for ways to avoid nested loops and using boolean arrays to track the presence of elements.
- Optimization techniques learned: Minimizing iterations and using constant space when possible.
- Similar problems to practice: Problems involving finding maximum or minimum elements under certain conditions, or tracking occurrences of elements in a string or array.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly indexing arrays or vectors, or failing to handle edge cases like empty strings.
- Edge cases to watch for: Empty strings, strings with only one case (all uppercase or all lowercase), and strings with no matching letters.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexities.
- Testing considerations: Thoroughly testing the function with a variety of inputs, including edge cases, to ensure correctness and efficiency.