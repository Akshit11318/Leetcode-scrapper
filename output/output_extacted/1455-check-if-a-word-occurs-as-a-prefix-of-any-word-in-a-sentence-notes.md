## Check if a Word Occurs as a Prefix of Any Word in a Sentence
**Problem Link:** https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description

**Problem Statement:**
- Input format and constraints: The function takes two parameters: `sentence` and `searchWord`. The `sentence` is a string that contains a sequence of words separated by spaces, and `searchWord` is a string that represents the word to be searched.
- Expected output format: The function should return `true` if `searchWord` occurs as a prefix of any word in the `sentence`, and `false` otherwise.
- Key requirements and edge cases to consider: The function should handle cases where `searchWord` is an empty string, the `sentence` is empty, or `searchWord` is longer than any word in the `sentence`.
- Example test cases with explanations:
  - Example 1: `sentence = "this problem is an example", searchWord = "example"` returns `true` because `searchWord` is a prefix of the word "example" in the `sentence`.
  - Example 2: `sentence = "i love eating burger", searchWord = "burg"` returns `false` because `searchWord` is not a prefix of any word in the `sentence`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To check if `searchWord` occurs as a prefix of any word in the `sentence`, we can split the `sentence` into words and then iterate over each word to check if `searchWord` is a prefix of that word.
- Step-by-step breakdown of the solution:
  1. Split the `sentence` into words using the space character as a delimiter.
  2. Iterate over each word in the list of words.
  3. For each word, check if `searchWord` is a prefix of that word by comparing characters from the start of both strings.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it directly checks each word in the `sentence` to see if `searchWord` is a prefix.

```cpp
class Solution {
public:
    bool isPrefixOfWord(string sentence, string searchWord) {
        // Split the sentence into words
        vector<string> words;
        string word;
        for (char c : sentence) {
            if (c == ' ') {
                words.push_back(word);
                word.clear();
            } else {
                word += c;
            }
        }
        words.push_back(word);

        // Check each word to see if searchWord is a prefix
        for (string w : words) {
            if (w.find(searchWord) == 0) {
                return true;
            }
        }

        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words in the `sentence` and $m$ is the length of `searchWord`. This is because we are iterating over each word and then checking each character in `searchWord` against the corresponding character in the word.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of characters in the `sentence`. This is because we are storing all the words from the `sentence` in a vector.
> - **Why these complexities occur:** These complexities occur because we are performing a linear search over the words in the `sentence` and then performing another linear comparison for each word.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of manually splitting the `sentence` into words, we can use the `find` function in a loop to find the next space character and extract the word.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `start` and `end`, to the beginning of the `sentence`.
  2. Loop through the `sentence` to find each word.
  3. For each word, check if `searchWord` is a prefix by comparing characters from the start of both strings.
- Proof of optimality: This approach is optimal because it still has to check each word in the `sentence` but does so more efficiently by avoiding the overhead of creating a vector of words.

```cpp
class Solution {
public:
    bool isPrefixOfWord(string sentence, string searchWord) {
        int start = 0;
        while (start < sentence.length()) {
            // Find the end of the current word
            int end = sentence.find(' ', start);
            if (end == string::npos) {
                end = sentence.length();
            }

            // Extract the current word
            string word = sentence.substr(start, end - start);

            // Check if searchWord is a prefix of the current word
            if (word.find(searchWord) == 0) {
                return true;
            }

            // Move to the next word
            start = end + 1;
        }

        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the `sentence` and $m$ is the length of `searchWord`. This is because we are still checking each character in `searchWord` against the corresponding character in each word.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, because we are only using a constant amount of space to store the pointers and the current word.
> - **Optimality proof:** This is optimal because we have reduced the space complexity to constant while maintaining the same time complexity as the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, prefix checking, and optimization of space complexity.
- Problem-solving patterns identified: The importance of considering the input and output formats, handling edge cases, and optimizing for space complexity when possible.
- Optimization techniques learned: Using pointers or indices to traverse a string instead of creating a new data structure.
- Similar problems to practice: Other string manipulation and prefix/suffix checking problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases such as an empty `sentence` or `searchWord`.
- Edge cases to watch for: Cases where `searchWord` is longer than any word in the `sentence`, or when `searchWord` is an empty string.
- Performance pitfalls: Creating unnecessary data structures or using inefficient algorithms for string manipulation.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure correctness and efficiency.