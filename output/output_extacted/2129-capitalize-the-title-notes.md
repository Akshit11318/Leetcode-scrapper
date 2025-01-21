## Capitalize the Title
**Problem Link:** https://leetcode.com/problems/capitalize-the-title/description

**Problem Statement:**
- Input format and constraints: Given a string `title`, you need to capitalize the title by converting the first character of every word to uppercase and making all other characters in the word lowercase. However, you should not capitalize the first word if it is less than three characters long. Similarly, you should not capitalize any word that is less than three characters long.
- Expected output format: The function should return the title with the specified capitalization.
- Key requirements and edge cases to consider: 
  - The input string `title` may contain multiple words separated by spaces.
  - The function should handle edge cases where the input string is empty or contains only one word.
- Example test cases with explanations:
  - Input: `title = "capiTALize tHE titLe"` 
    - Expected output: `"Capitalize The Title"`
  - Input: `title = "first leTTeR oF eAch Word"`
    - Expected output: `"First Letter Of Each Word"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each character in the input string, checking if it is the first character of a word, and if so, converting it to uppercase. Otherwise, it converts the character to lowercase.
- Step-by-step breakdown of the solution:
  1. Split the input string into words.
  2. Iterate over each word.
  3. If the word is the first word and its length is less than 3, or if the word's length is less than 3, convert all characters to lowercase.
  4. Otherwise, convert the first character of the word to uppercase and the rest to lowercase.
  5. Join the modified words back into a string.

```cpp
class Solution {
public:
    string capitalizeTitle(string title) {
        istringstream iss(title);
        string word, result;
        
        while (iss >> word) {
            if (word.length() < 3) {
                for (char& c : word) {
                    c = tolower(c);
                }
            } else {
                word[0] = toupper(word[0]);
                for (int i = 1; i < word.length(); ++i) {
                    word[i] = tolower(word[i]);
                }
            }
            result += word + " ";
        }
        
        // Remove the trailing space
        if (!result.empty()) {
            result.pop_back();
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words in the input string and $m$ is the maximum length of a word. This is because we iterate over each character in each word.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the average length of a word. This is because we store the modified words in the `result` string.
> - **Why these complexities occur:** These complexities occur because we need to process each character in the input string and store the modified words.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using the same approach as the brute force solution but with minor optimizations to reduce the number of operations.
- Detailed breakdown of the approach:
  1. Split the input string into words.
  2. Iterate over each word.
  3. If the word is the first word and its length is less than 3, or if the word's length is less than 3, convert all characters to lowercase using the `tolower` function.
  4. Otherwise, convert the first character of the word to uppercase using the `toupper` function and the rest to lowercase using the `tolower` function.
  5. Join the modified words back into a string.

```cpp
class Solution {
public:
    string capitalizeTitle(string title) {
        istringstream iss(title);
        string word, result;
        bool isFirstWord = true;
        
        while (iss >> word) {
            if ((isFirstWord && word.length() < 3) || word.length() < 3) {
                for (char& c : word) {
                    c = tolower(c);
                }
            } else {
                for (char& c : word) {
                    c = tolower(c);
                }
                word[0] = toupper(word[0]);
            }
            result += word + " ";
            isFirstWord = false;
        }
        
        // Remove the trailing space
        if (!result.empty()) {
            result.pop_back();
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words in the input string and $m$ is the maximum length of a word. This is because we iterate over each character in each word.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the average length of a word. This is because we store the modified words in the `result` string.
> - **Optimality proof:** This solution is optimal because we need to process each character in the input string to determine the correct capitalization.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, character conversion, and conditional statements.
- Problem-solving patterns identified: iterating over words in a string, checking word lengths, and applying different conversions based on word position and length.
- Optimization techniques learned: reducing the number of operations by using the `tolower` and `toupper` functions directly on characters.
- Similar problems to practice: other string manipulation problems involving character conversions and word processing.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle edge cases, such as empty input strings or words with lengths less than 3.
- Edge cases to watch for: input strings with multiple words, words with lengths less than 3, and the first word with a length less than 3.
- Performance pitfalls: using inefficient algorithms or data structures that lead to high time or space complexities.
- Testing considerations: testing the function with different input strings, including edge cases, to ensure correct capitalization.