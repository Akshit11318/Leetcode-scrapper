## Find Words Containing Character
**Problem Link:** https://leetcode.com/problems/find-words-containing-character/description

**Problem Statement:**
- Given a list of strings `words` and a character `c`, find all the words that contain the character `c`.
- Input format and constraints: `words` is a list of strings, `c` is a single character.
- Expected output format: A list of strings containing the character `c`.
- Key requirements and edge cases to consider: The list of words may be empty, the character `c` may not exist in any word.
- Example test cases with explanations:
  - Input: `words = ["hello", "world", "python"]`, `c = 'o'`
  - Output: `["hello", "world"]`
  - Explanation: Both "hello" and "world" contain the character 'o'.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each word in the list and check if the character `c` exists in the word.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the words containing the character `c`.
  2. Iterate through each word in the list of words.
  3. For each word, check if the character `c` exists in the word using a loop or the `find` method.
  4. If the character `c` exists in the word, add the word to the list of words containing `c`.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
vector<string> findWords(vector<string>& words, char c) {
    vector<string> result;
    for (string word : words) {
        if (word.find(c) != string::npos) {
            result.push_back(word);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the average length of a word. This is because for each word, we potentially iterate through all its characters to find the character `c`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of words. In the worst case, all words contain the character `c`, so we store all words in the result list.
> - **Why these complexities occur:** The brute force approach involves iterating through each word and potentially each character in the word, leading to the $O(n \cdot m)$ time complexity. The space complexity is due to storing the result list, which in the worst case can contain all input words.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already quite straightforward and efficient for this problem. However, we can slightly optimize it by using `std::string::find` method which returns the position of the first character of the first match, and `std::string::npos` if no matches were found. This is essentially what the brute force does but recognizing it as optimal simplifies our approach.
- Detailed breakdown of the approach: Same as the brute force, but acknowledging its optimality.
- Proof of optimality: Given the problem's nature, we must at least look at each word once and potentially each character in a word to determine if it contains `c`. Thus, the $O(n \cdot m)$ time complexity is optimal for this problem, where $n$ is the number of words and $m$ is the average length of a word.

```cpp
vector<string> findWords(vector<string>& words, char c) {
    vector<string> result;
    for (string word : words) {
        if (word.find(c) != string::npos) {
            result.push_back(word);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the average length of a word.
> - **Space Complexity:** $O(n)$, where $n$ is the number of words.
> - **Optimality proof:** We cannot do better than $O(n \cdot m)$ because in the worst case, we have to examine every character in every word to determine if it contains `c`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, string manipulation, conditional checks.
- Problem-solving patterns identified: Direct iteration and checking.
- Optimization techniques learned: Recognizing when a straightforward approach is already optimal.
- Similar problems to practice: Other string manipulation and searching problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like empty input lists or words.
- Edge cases to watch for: Empty strings, strings without the character `c`, and the case where no words contain `c`.
- Performance pitfalls: Unnecessary iterations or checks that could increase the time complexity beyond $O(n \cdot m)$.
- Testing considerations: Ensure to test with a variety of inputs, including edge cases and large inputs to verify efficiency.