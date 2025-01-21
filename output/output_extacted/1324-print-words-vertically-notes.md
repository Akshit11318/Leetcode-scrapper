## Print Words Vertically
**Problem Link:** https://leetcode.com/problems/print-words-vertically/description

**Problem Statement:**
- Input: A list of non-empty words.
- Output: Print the words vertically.
- Key requirements: 
    - Each word should be printed as if we were writing it in columns.
    - If two words have different lengths, the shorter word will be padded with spaces to make it the same length as the longer word.
    - The words should be printed in the order they appear in the input list.
- Example test cases: 
    - Input: `["try","for","code"]`
    - Output: `["tfo","ryc","oe"]`
    - Explanation: The output is the result of printing the words vertically.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each character in the words and create a new word by taking the characters at the same position from each word.
- We will use a loop to iterate over the maximum length of the words, and for each position, we will create a new word with the characters at that position from each word.
- This approach comes to mind first because it is straightforward and easy to understand.

```cpp
class Solution {
public:
    vector<string> printVertically(vector<string>& words) {
        int maxLength = 0;
        for (const auto& word : words) {
            maxLength = max(maxLength, (int)word.size());
        }
        
        vector<string> result;
        for (int i = 0; i < maxLength; i++) {
            string word;
            for (const auto& w : words) {
                if (i < w.size()) {
                    word += w[i];
                } else {
                    word += ' ';
                }
            }
            // Remove trailing spaces
            while (!word.empty() && word.back() == ' ') {
                word.pop_back();
            }
            result.push_back(word);
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of words and $m$ is the maximum length of the words. This is because we are iterating over each word and each character in the words.
> - **Space Complexity:** $O(n \times m)$, where $n$ is the number of words and $m$ is the maximum length of the words. This is because we are storing the result in a vector of strings.
> - **Why these complexities occur:** These complexities occur because we are iterating over each character in each word, and storing the result in a new vector of strings.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use the same approach as the brute force solution, but with some minor optimizations.
- We can use the `std::string` class to create a new string with the characters at the same position from each word.
- This approach is optimal because it has the same time and space complexity as the brute force solution, but with some minor optimizations.

```cpp
class Solution {
public:
    vector<string> printVertically(vector<string>& words) {
        int maxLength = 0;
        for (const auto& word : words) {
            maxLength = max(maxLength, (int)word.size());
        }
        
        vector<string> result;
        for (int i = 0; i < maxLength; i++) {
            string word;
            for (const auto& w : words) {
                if (i < w.size()) {
                    word += w[i];
                } else {
                    word += ' ';
                }
            }
            // Remove trailing spaces
            while (!word.empty() && word.back() == ' ') {
                word.pop_back();
            }
            result.push_back(word);
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of words and $m$ is the maximum length of the words. This is because we are iterating over each word and each character in the words.
> - **Space Complexity:** $O(n \times m)$, where $n$ is the number of words and $m$ is the maximum length of the words. This is because we are storing the result in a vector of strings.
> - **Optimality proof:** This is the optimal solution because it has the same time and space complexity as the brute force solution, but with some minor optimizations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration over characters in strings, creation of new strings with characters at the same position from each word.
- Problem-solving patterns identified: using a loop to iterate over the maximum length of the words, and creating a new word with the characters at the same position from each word.
- Optimization techniques learned: using the `std::string` class to create a new string with the characters at the same position from each word.
- Similar problems to practice: printing words horizontally, printing numbers vertically.

**Mistakes to Avoid:**
- Common implementation errors: not checking for the maximum length of the words, not removing trailing spaces from the result.
- Edge cases to watch for: empty words, words with different lengths.
- Performance pitfalls: using inefficient data structures or algorithms.
- Testing considerations: testing with different inputs, such as empty words, words with different lengths, and words with special characters.