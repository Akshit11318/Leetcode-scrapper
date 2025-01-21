## Number of Valid Words for Each Puzzle

**Problem Link:** https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/description

**Problem Statement:**
- Given a list of words and a list of puzzles, find the number of valid words for each puzzle. A word is valid for a puzzle if it can be formed by rearranging the letters in the puzzle.
- Input format: `words` (a list of strings) and `puzzles` (a list of strings)
- Expected output format: A list of integers, where each integer represents the number of valid words for the corresponding puzzle.
- Key requirements and edge cases to consider: The puzzles are always 7 characters long, and the words are always between 4 and 7 characters long.
- Example test cases with explanations:
  - Input: `words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]`, `puzzles = ["aboveyz", "abrodyz", "abslang", "abnorml", "absoryz", "abuzzzz"]`
  - Output: `[1, 1, 3, 2, 4, 0]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each puzzle, try to form every word by rearranging the letters in the puzzle.
- Step-by-step breakdown of the solution:
  1. Iterate over each puzzle.
  2. For each puzzle, iterate over each word.
  3. Check if the word can be formed by rearranging the letters in the puzzle.
  4. If the word can be formed, increment the count of valid words for the puzzle.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it is not efficient because it involves many unnecessary comparisons.

```cpp
vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
    vector<int> result(puzzles.size(), 0);
    for (int i = 0; i < puzzles.size(); i++) {
        for (const string& word : words) {
            bool isValid = true;
            for (char c : word) {
                if (puzzles[i].find(c) == string::npos) {
                    isValid = false;
                    break;
                }
            }
            if (isValid && word[0] == puzzles[i][0]) {
                result[i]++;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m \times k)$, where $n$ is the number of puzzles, $m$ is the number of words, and $k$ is the maximum length of a word. This is because for each puzzle, we iterate over each word and check if the word can be formed by rearranging the letters in the puzzle.
> - **Space Complexity:** $O(n)$, where $n$ is the number of puzzles. This is because we need to store the count of valid words for each puzzle.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops, and the space complexity occurs because we need to store the result for each puzzle.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a bitmask to represent the presence of each letter in the puzzle and the word. This allows us to quickly check if a word can be formed by rearranging the letters in the puzzle.
- Detailed breakdown of the approach:
  1. Create a bitmask for each puzzle and each word.
  2. Iterate over each puzzle and each word.
  3. Check if the word can be formed by rearranging the letters in the puzzle by using the bitwise AND operator.
  4. If the word can be formed, increment the count of valid words for the puzzle.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(n \times m \times k)$ to $O(n \times m)$, where $n$ is the number of puzzles and $m$ is the number of words.

```cpp
vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
    vector<int> result(puzzles.size(), 0);
    unordered_map<int, int> wordCount;
    for (const string& word : words) {
        int bitmask = 0;
        for (char c : word) {
            bitmask |= 1 << (c - 'a');
        }
        wordCount[bitmask]++;
    }
    for (int i = 0; i < puzzles.size(); i++) {
        int puzzleMask = 0;
        for (char c : puzzles[i]) {
            puzzleMask |= 1 << (c - 'a');
        }
        int submask = puzzleMask;
        int count = 0;
        while (submask > 0) {
            if (wordCount.find(submask) != wordCount.end() && (submask & (1 << (puzzles[i][0] - 'a')))) {
                count += wordCount[submask];
            }
            submask = (submask - 1) & puzzleMask;
        }
        if (wordCount.find(1 << (puzzles[i][0] - 'a')) != wordCount.end()) {
            count += wordCount[1 << (puzzles[i][0] - 'a')];
        }
        result[i] = count;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of puzzles and $m$ is the number of words. This is because we iterate over each puzzle and each word.
> - **Space Complexity:** $O(m)$, where $m$ is the number of words. This is because we need to store the count of each word.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from $O(n \times m \times k)$ to $O(n \times m)$, where $n$ is the number of puzzles and $m$ is the number of words.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation and bitmasking.
- Problem-solving patterns identified: Using bitmasks to quickly check if a word can be formed by rearranging the letters in the puzzle.
- Optimization techniques learned: Reducing the time complexity by using bitmasks.
- Similar problems to practice: Other problems that involve bit manipulation and bitmasking.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the word is not present in the puzzle.
- Edge cases to watch for: The case where the puzzle or the word is empty.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the code with different inputs and edge cases to ensure it works correctly.