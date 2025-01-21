## Index Pairs of a String
**Problem Link:** https://leetcode.com/problems/index-pairs-of-a-string/description

**Problem Statement:**
- Input format and constraints: Given a text string and a word string, return a list of all index pairs `[i, j]` in the text where the word starts at index `i` and the word's last character is at index `j`.
- Expected output format: List of pairs of indices where the word is found in the text.
- Key requirements and edge cases to consider: The word should be a substring of the text, and we should return all non-overlapping occurrences.
- Example test cases with explanations: 
    - For text = "thestoryofus" and word = "story", the output should be [[3,7]] because "story" starts at index 3 and ends at index 7.
    - For text = "ababa" and word = "aba", the output should be [[0,2], [3,5]] because "aba" appears twice in the text.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through the text and for each character, check if the word matches the substring starting at that character.
- Step-by-step breakdown of the solution: 
    1. Initialize an empty list to store the index pairs.
    2. Iterate through the text using a for loop.
    3. For each index, check if the word is equal to the substring of the text starting at that index with the length of the word.
    4. If the word matches, add the index pair to the list.
- Why this approach comes to mind first: It is straightforward and easy to understand, directly addressing the problem statement.

```cpp
vector<vector<int>> indexPairs(string text, string word) {
    vector<vector<int>> result;
    for (int i = 0; i <= text.size() - word.size(); i++) {
        if (text.substr(i, word.size()) == word) {
            result.push_back({i, i + word.size() - 1});
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the length of the text and $m$ is the length of the word. This is because for each character in the text, we potentially compare with the entire word.
> - **Space Complexity:** $O(k)$ where $k$ is the number of occurrences of the word in the text, as we store each occurrence in the result list.
> - **Why these complexities occur:** The time complexity is high because of the nested operations (iteration through the text and comparison with the word), and the space complexity is dependent on the number of occurrences of the word.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a sliding window approach or the `std::string::find` method to efficiently find all occurrences of the word in the text.
- Detailed breakdown of the approach: 
    1. Initialize an empty list to store the index pairs.
    2. Use a loop starting from the beginning of the text.
    3. Inside the loop, use the `std::string::find` method to find the next occurrence of the word in the text, starting from the current position.
    4. If an occurrence is found, calculate the end index and add the index pair to the list, then update the current position to be after the found occurrence.
    5. Repeat until no more occurrences are found.
- Proof of optimality: This approach is optimal because it minimizes the number of comparisons needed to find all occurrences of the word in the text.

```cpp
vector<vector<int>> indexPairs(string text, string word) {
    vector<vector<int>> result;
    size_t pos = text.find(word);
    while (pos != string::npos) {
        result.push_back({static_cast<int>(pos), static_cast<int>(pos + word.size() - 1)});
        pos = text.find(word, pos + 1);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ in the worst case, but practically much faster than the brute force approach because `std::string::find` uses optimized algorithms like the Knuth-Morris-Pratt algorithm or the Boyer-Moore algorithm for efficient string searching.
> - **Space Complexity:** $O(k)$ where $k$ is the number of occurrences of the word in the text, as we store each occurrence in the result list.
> - **Optimality proof:** This is the best approach because it leverages optimized library functions for string searching, minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient string searching, use of sliding window or library functions for optimization.
- Problem-solving patterns identified: Breaking down the problem into smaller, manageable parts (finding each occurrence of the word).
- Optimization techniques learned: Using optimized library functions for common operations like string searching.
- Similar problems to practice: Other string searching or pattern matching problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases like an empty text or word, or not updating the search position correctly after finding an occurrence.
- Edge cases to watch for: Empty strings, words longer than the text, or words that do not appear in the text.
- Performance pitfalls: Using naive approaches that result in high time complexities for large inputs.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure correctness and efficiency.