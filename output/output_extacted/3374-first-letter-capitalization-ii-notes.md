## First Letter Capitalization II

**Problem Link:** https://leetcode.com/problems/first-letter-capitalization-ii/description

**Problem Statement:**
- Input format: A string `word` containing only lowercase English letters.
- Constraints: `1 <= word.length <= 100`
- Expected output format: Return the word after converting the first letter of every word to uppercase and the rest of the letters to lowercase.
- Key requirements and edge cases to consider: 
  - Words are separated by spaces.
  - Single-character words should be capitalized.
  - The input string only contains lowercase letters and spaces.
- Example test cases with explanations:
  - Input: "word"
    - Expected output: "Word"
  - Input: "first letter capitalization"
    - Expected output: "First Letter Capitalization"

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to manually iterate over each character in the string, checking if it's the start of a word and if so, converting it to uppercase, and converting the rest of the characters to lowercase.
- Step-by-step breakdown of the solution:
  1. Split the input string into words.
  2. For each word, capitalize the first letter and make the rest lowercase.
  3. Join the words back together with spaces in between.

```cpp
#include <iostream>
#include <sstream>
#include <string>

string capitalizeWord(string word) {
    string capitalizedWord = "";
    for (int i = 0; i < word.length(); i++) {
        if (i == 0) {
            // Capitalize the first letter
            capitalizedWord += toupper(word[i]);
        } else {
            // Make the rest lowercase
            capitalizedWord += tolower(word[i]);
        }
    }
    return capitalizedWord;
}

string capitalizeFirstLetter(string word) {
    stringstream ss(word);
    string token;
    string result = "";
    
    while (ss >> token) {
        result += capitalizeWord(token) + " ";
    }
    
    // Remove the trailing space
    if (!result.empty()) {
        result.pop_back();
    }
    
    return result;
}

int main() {
    string word = "first letter capitalization";
    cout << capitalizeFirstLetter(word) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words in the string and $m$ is the average length of a word. This is because we are iterating over each character in each word.
> - **Space Complexity:** $O(n \cdot m)$, as we are storing the modified words in new strings.
> - **Why these complexities occur:** These complexities occur because we are manually processing each character in the input string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of creating a new string for each word, we can directly modify the input string or create a single output string and append to it as we process each word.
- Detailed breakdown of the approach:
  1. Initialize an empty string `result` to store the final output.
  2. Initialize a flag `capitalizeNext` to true to indicate that the next character should be capitalized.
  3. Iterate over each character in the input string.
  4. If the character is a space, append it to `result` and set `capitalizeNext` to true.
  5. If `capitalizeNext` is true, capitalize the character and append it to `result`, then set `capitalizeNext` to false.
  6. If `capitalizeNext` is false, make the character lowercase and append it to `result`.

```cpp
#include <iostream>
#include <string>

string capitalizeFirstLetter(string word) {
    string result = "";
    bool capitalizeNext = true;
    
    for (char c : word) {
        if (c == ' ') {
            result += c;
            capitalizeNext = true;
        } else {
            if (capitalizeNext) {
                result += toupper(c);
                capitalizeNext = false;
            } else {
                result += tolower(c);
            }
        }
    }
    
    return result;
}

int main() {
    string word = "first letter capitalization";
    std::cout << capitalizeFirstLetter(word) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we make a single pass through the string.
> - **Space Complexity:** $O(n)$, as we are creating a new string that is at most the same length as the input string.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through the input string and uses a minimal amount of extra space to store the output.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, character iteration, and conditional logic.
- Problem-solving patterns identified: The importance of iterating over the input string only once to achieve optimal time complexity.
- Optimization techniques learned: Avoiding unnecessary string creations and using flags to track state.
- Similar problems to practice: Other string manipulation problems, such as reversing strings or finding substrings.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like single-character words or empty strings.
- Edge cases to watch for: Words with multiple consecutive spaces, or strings containing non-alphabet characters.
- Performance pitfalls: Creating unnecessary intermediate strings or using inefficient algorithms.
- Testing considerations: Thoroughly testing the function with a variety of inputs, including edge cases.