## First Letter Capitalization
**Problem Link:** https://leetcode.com/problems/first-letter-capitalization/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` containing lowercase English letters.
- Expected output format: The output is a string where the first letter of each word is capitalized.
- Key requirements and edge cases to consider: 
  - Handle empty strings.
  - Handle strings with multiple spaces between words.
  - Handle strings with leading or trailing spaces.
- Example test cases with explanations: 
  - Input: "hello world"
    - Expected output: "Hello World"
  - Input: "   hello   world  "
    - Expected output: "Hello World"

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over the string, find the first character of each word, and capitalize it.
- Step-by-step breakdown of the solution:
  1. Remove leading and trailing spaces from the input string.
  2. Split the string into words based on spaces.
  3. For each word, capitalize the first letter.
  4. Join the words back into a string with spaces in between.
- Why this approach comes to mind first: It directly addresses the problem statement by identifying and capitalizing the first letter of each word.

```cpp
#include <iostream>
#include <vector>
#include <sstream>

string capitalizeFirstLetters(string s) {
    // Remove leading and trailing spaces
    while (!s.empty() && s[0] == ' ') {
        s.erase(0, 1);
    }
    while (!s.empty() && s[s.size() - 1] == ' ') {
        s.pop_back();
    }

    stringstream ss(s);
    string word;
    string result;

    // Split into words and capitalize the first letter of each
    while (ss >> word) {
        word[0] = toupper(word[0]);
        for (int i = 1; i < word.size(); ++i) {
            word[i] = tolower(word[i]);
        }
        result += word + " ";
    }

    // Remove the trailing space
    if (!result.empty()) {
        result.pop_back();
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of characters in the string. This is because we potentially iterate over each character in the string once.
> - **Space Complexity:** $O(n)$, as in the worst case, we might need to store all characters in the `result` string and potentially in the `word` variable.
> - **Why these complexities occur:** The iteration over the string and the storage of the result string dictate these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of removing leading and trailing spaces and then splitting the string into words, we can iterate over the string and capitalize the first letter of each word directly. We keep track of whether we are at the start of a word or not.
- Detailed breakdown of the approach:
  1. Initialize a flag `isStartOfWord` to `true`.
  2. Iterate over each character in the string.
  3. If the character is a space, set `isStartOfWord` to `true`.
  4. If the character is not a space and `isStartOfWord` is `true`, capitalize the character and set `isStartOfWord` to `false`.
  5. If the character is not a space and `isStartOfWord` is `false`, ensure the character is lowercase.
- Proof of optimality: This approach achieves the same result as the brute force but in a single pass through the string, making it more efficient.

```cpp
string capitalizeFirstLettersOptimal(string s) {
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == ' ') {
            continue;
        }
        // If this is the first character or follows a space, capitalize it
        if (i == 0 || s[i - 1] == ' ') {
            s[i] = toupper(s[i]);
        } else {
            s[i] = tolower(s[i]);
        }
    }
    return s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of characters in the string. This is because we make one pass through the string.
> - **Space Complexity:** $O(1)$, assuming the input string can be modified in-place. Otherwise, $O(n)$ if we need to create a copy of the string.
> - **Optimality proof:** This is the optimal solution because it only requires a single pass through the input string, and it does not require any additional space that scales with the input size (assuming in-place modification).

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and string manipulation.
- Problem-solving patterns identified: Directly addressing the problem statement and optimizing based on the specific requirements.
- Optimization techniques learned: Reducing the number of passes through the data and minimizing additional space usage.
- Similar problems to practice: Other string manipulation problems, such as reversing strings or finding substrings.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like empty strings or strings with multiple consecutive spaces.
- Edge cases to watch for: Leading, trailing, or multiple consecutive spaces within the string.
- Performance pitfalls: Making unnecessary copies of the string or using inefficient algorithms.
- Testing considerations: Ensure to test with a variety of inputs, including edge cases and large strings to verify performance.