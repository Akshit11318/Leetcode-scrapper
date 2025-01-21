## Count the Number of Consistent Strings
**Problem Link:** https://leetcode.com/problems/count-the-number-of-consistent-strings/description

**Problem Statement:**
- Input format and constraints: The problem takes in two parameters: a list of strings `words` and a string `allowed`.
- Expected output format: The function should return the count of consistent strings.
- Key requirements and edge cases to consider: A consistent string is one that only contains characters present in the `allowed` string. The function should iterate through each word in the `words` list and check if it's consistent.
- Example test cases with explanations: For example, given `words = ["ad","bd","aaab","baa","badab"]` and `allowed = "ab"`, the function should return `2` because only `"ad"` and `"aaab"` are consistent.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through each word in the `words` list and check if it's consistent by verifying if each character in the word is present in the `allowed` string.
- Step-by-step breakdown of the solution:
  1. Initialize a counter to keep track of consistent strings.
  2. Iterate through each word in the `words` list.
  3. For each word, iterate through each character and check if it's present in the `allowed` string.
  4. If all characters in the word are present in the `allowed` string, increment the counter.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
int countConsistentStrings(vector<string>& words, string allowed) {
    int count = 0;
    for (const auto& word : words) {
        bool isConsistent = true;
        for (const auto& char_ : word) {
            if (allowed.find(char_) == string::npos) {
                isConsistent = false;
                break;
            }
        }
        if (isConsistent) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of words, $m$ is the maximum length of a word, and $k$ is the length of the `allowed` string. This is because for each word, we're potentially scanning the entire `allowed` string for each character in the word.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the counter and other variables.
> - **Why these complexities occur:** The nested loops cause the time complexity to be cubic in the worst case, and the space complexity is constant because we're not using any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of scanning the `allowed` string for each character in each word, we can create a set of allowed characters for constant-time lookup.
- Detailed breakdown of the approach:
  1. Create a set of characters from the `allowed` string.
  2. Iterate through each word in the `words` list.
  3. For each word, check if all its characters are present in the set of allowed characters.
  4. If a word is consistent, increment the counter.
- Proof of optimality: This approach is optimal because it reduces the time complexity of checking if a character is allowed from linear to constant, resulting in a significant improvement for large inputs.

```cpp
int countConsistentStrings(vector<string>& words, string allowed) {
    unordered_set<char> allowedChars(allowed.begin(), allowed.end());
    int count = 0;
    for (const auto& word : words) {
        bool isConsistent = true;
        for (const auto& char_ : word) {
            if (allowedChars.find(char_) == allowedChars.end()) {
                isConsistent = false;
                break;
            }
        }
        if (isConsistent) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because we're scanning each word once and performing constant-time lookups for each character.
> - **Space Complexity:** $O(k)$, where $k$ is the length of the `allowed` string, because we're storing the allowed characters in a set.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input once, and our approach does so with minimal additional overhead.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Set data structures for efficient lookup, iteration over strings and vectors.
- Problem-solving patterns identified: Improving brute force solutions by reducing the complexity of nested operations.
- Optimization techniques learned: Using sets for constant-time membership tests.
- Similar problems to practice: Other string processing and set manipulation problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases like empty input strings or words.
- Edge cases to watch for: Handling words or allowed strings with special characters.
- Performance pitfalls: Using linear search instead of constant-time lookup data structures.
- Testing considerations: Thoroughly testing with various input sizes and edge cases to ensure correctness and performance.