## Rearrange Spaces Between Words
**Problem Link:** https://leetcode.com/problems/rearrange-spaces-between-words/description

**Problem Statement:**
- Input format and constraints: The input is a string `text` containing words separated by spaces. The string can contain leading, trailing, or multiple consecutive spaces.
- Expected output format: The function should return a string where the spaces are rearranged to be evenly distributed between words.
- Key requirements and edge cases to consider:
  - If there are multiple consecutive spaces in the input, they should be condensed into a single space in the output.
  - If there are more spaces than needed to separate the words evenly, the extra spaces should be added to the end of the string.
  - If there are not enough spaces to separate the words, the function should still distribute the available spaces as evenly as possible.
- Example test cases with explanations:
  - Input: `text = "  this   is  a sentence "` 
    - Expected Output: `"this is a sentence"`
  - Input: `text = " practice   makes   perfect"`
    - Expected Output: `"practice makes perfect "`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to remove leading and trailing spaces from the input string and count the number of words and spaces.
- Step-by-step breakdown of the solution:
  1. Remove leading and trailing spaces from the input string.
  2. Split the string into words and count the number of words and spaces.
  3. Calculate the number of spaces needed to separate the words evenly.
  4. Distribute the spaces between the words.
- Why this approach comes to mind first: It is straightforward and involves basic string manipulation.

```cpp
#include <iostream>
#include <vector>
#include <sstream>

string reorderSpaces(string text) {
    int spaceCount = 0;
    for (char c : text) {
        if (c == ' ') {
            spaceCount++;
        }
    }

    vector<string> words;
    string word;
    for (char c : text) {
        if (c == ' ') {
            if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        } else {
            word += c;
        }
    }
    if (!word.empty()) {
        words.push_back(word);
    }

    int wordCount = words.size();
    if (wordCount == 1) {
        return words[0] + string(spaceCount, ' ');
    }

    int spaceBetween = spaceCount / (wordCount - 1);
    int extraSpace = spaceCount % (wordCount - 1);

    string result;
    for (int i = 0; i < words.size(); ++i) {
        result += words[i];
        if (i < words.size() - 1) {
            result += string(spaceBetween, ' ');
            if (i < extraSpace) {
                result += ' ';
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate over the string to count spaces and split it into words.
> - **Space Complexity:** $O(n)$, because we store the words in a vector, which in the worst case (when the string consists of single characters separated by spaces) can be of the same length as the input string.
> - **Why these complexities occur:** These complexities occur due to the need to process the entire input string and store the words in memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved by first counting the spaces and words, then distributing the spaces between the words.
- Detailed breakdown of the approach:
  1. Count the spaces and words in the input string.
  2. Calculate the number of spaces to be placed between words and the number of extra spaces.
  3. Construct the output string by placing the calculated number of spaces between words and appending the extra spaces at the end.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input string to count the spaces and words, and then it constructs the output string in a single pass.

```cpp
#include <iostream>
#include <vector>
#include <sstream>

string reorderSpaces(string text) {
    int spaceCount = 0;
    int wordCount = 0;
    string word;
    for (char c : text) {
        if (c == ' ') {
            spaceCount++;
            if (!word.empty()) {
                wordCount++;
                word.clear();
            }
        } else {
            word += c;
        }
    }
    if (!word.empty()) {
        wordCount++;
    }

    if (wordCount == 1) {
        return word + string(spaceCount, ' ');
    }

    int spaceBetween = spaceCount / (wordCount - 1);
    int extraSpace = spaceCount % (wordCount - 1);

    string result;
    for (int i = 0; i < wordCount; ++i) {
        if (i > 0) {
            result += string(spaceBetween, ' ');
            if (i <= extraSpace) {
                result += ' ';
            }
        }
        // Append the word, but first we need to reconstruct the word list
        // which can be done by splitting the input string again
        // or by storing the words in a vector during the counting phase
        // For simplicity, we'll assume we have a function to get the ith word
        // from the input string
        result += getWord(text, i);
    }
    return result;
}

// Helper function to get the ith word from the input string
string getWord(string text, int index) {
    int wordCount = 0;
    string word;
    for (char c : text) {
        if (c == ' ') {
            if (!word.empty()) {
                wordCount++;
                if (wordCount == index + 1) {
                    return word;
                }
                word.clear();
            }
        } else {
            word += c;
        }
    }
    if (!word.empty() && wordCount == index) {
        return word;
    }
    return "";
}
```

However, the optimal solution provided earlier still requires reconstructing the words from the input string, which can be avoided by storing the words during the counting phase. Here's the corrected optimal solution:

```cpp
#include <iostream>
#include <vector>
#include <sstream>

string reorderSpaces(string text) {
    int spaceCount = 0;
    vector<string> words;
    string word;
    for (char c : text) {
        if (c == ' ') {
            spaceCount++;
            if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        } else {
            word += c;
        }
    }
    if (!word.empty()) {
        words.push_back(word);
    }

    if (words.size() == 1) {
        return words[0] + string(spaceCount, ' ');
    }

    int spaceBetween = spaceCount / (words.size() - 1);
    int extraSpace = spaceCount % (words.size() - 1);

    string result;
    for (int i = 0; i < words.size(); ++i) {
        result += words[i];
        if (i < words.size() - 1) {
            result += string(spaceBetween, ' ');
            if (i < extraSpace) {
                result += ' ';
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate over the string to count spaces and split it into words.
> - **Space Complexity:** $O(n)$, because we store the words in a vector, which in the worst case (when the string consists of single characters separated by spaces) can be of the same length as the input string.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input string to count the spaces and words, and then it constructs the output string in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, counting, and distribution of spaces.
- Problem-solving patterns identified: breaking down the problem into smaller steps, counting and distribution.
- Optimization techniques learned: avoiding unnecessary passes through the input data, using vectors to store intermediate results.
- Similar problems to practice: other string manipulation problems, such as removing duplicates or rearranging characters.

**Mistakes to Avoid:**
- Common implementation errors: off-by-one errors when calculating the number of spaces between words.
- Edge cases to watch for: handling empty input strings, strings with only one word, or strings with no spaces.
- Performance pitfalls: using inefficient algorithms that require multiple passes through the input data.
- Testing considerations: testing the function with different input cases, including edge cases and large input strings.