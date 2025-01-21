## Shortest Completing Word
**Problem Link:** https://leetcode.com/problems/shortest-completing-word/description

**Problem Statement:**
- Input format and constraints: The problem takes two parameters: `licensePlate` and `words`. The `licensePlate` is a string containing alphanumeric characters and spaces, and `words` is a list of strings. The goal is to find the shortest word that contains all the letters in the `licensePlate`, ignoring case and non-alphabetic characters.
- Expected output format: The function should return the shortest word that meets the conditions. If multiple words have the same minimum length, the function should return the one that appears first in the `words` list.
- Key requirements and edge cases to consider: The function should handle cases where there are multiple words with the same minimum length, and it should also handle cases where no word contains all the letters in the `licensePlate`.
- Example test cases with explanations:
  - Example 1: `licensePlate = "1s3 PSt"` and `words = ["step","steps","stripe","stepple"]`. The output should be `"steps"`.
  - Example 2: `licensePlate = "1s3 456"` and `words = ["looks","pest","stew","show"]`. The output should be `"pest"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each word in the `words` list and checking if it contains all the letters in the `licensePlate`.
- Step-by-step breakdown of the solution:
  1. Preprocess the `licensePlate` to extract the unique letters and store them in a set or map for efficient lookups.
  2. Iterate over each word in the `words` list.
  3. For each word, create a copy of the set or map of letters from the `licensePlate`.
  4. Iterate over each character in the word, and if the character is in the set or map of letters, remove it.
  5. If the set or map of letters becomes empty, it means the word contains all the letters in the `licensePlate`.
  6. Keep track of the shortest word that meets the condition and return it.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>

std::string shortestCompletingWord(std::string licensePlate, std::vector<std::string>& words) {
    // Preprocess the licensePlate
    std::unordered_map<char, int> licensePlateLetters;
    for (char c : licensePlate) {
        if (c >= 'a' && c <= 'z') {
            licensePlateLetters[c]++;
        } else if (c >= 'A' && c <= 'Z') {
            licensePlateLetters[c + 32]++;
        }
    }

    // Initialize the result
    std::string result;
    int minLength = INT_MAX;

    // Iterate over each word
    for (std::string word : words) {
        // Create a copy of the licensePlateLetters
        std::unordered_map<char, int> wordLetters = licensePlateLetters;

        // Check if the word contains all the letters in the licensePlate
        for (char c : word) {
            if (wordLetters.find(c) != wordLetters.end()) {
                wordLetters[c]--;
                if (wordLetters[c] == 0) {
                    wordLetters.erase(c);
                }
            }
        }

        // If the word contains all the letters and is shorter than the current result, update the result
        if (wordLetters.empty() && word.length() < minLength) {
            result = word;
            minLength = word.length();
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the average length of a word. This is because we iterate over each word and each character in the word.
> - **Space Complexity:** $O(k)$, where $k$ is the number of unique letters in the `licensePlate`. This is because we store the letters in a set or map for efficient lookups.
> - **Why these complexities occur:** The time complexity occurs because we have two nested loops: one for iterating over the words and one for iterating over the characters in each word. The space complexity occurs because we need to store the unique letters in the `licensePlate` for efficient lookups.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over each character in the word, we can use a hash map to count the frequency of each letter in the word. This allows us to compare the frequency of letters in the word with the frequency of letters in the `licensePlate` in constant time.
- Detailed breakdown of the approach:
  1. Preprocess the `licensePlate` to extract the unique letters and store them in a hash map for efficient lookups.
  2. Iterate over each word in the `words` list.
  3. For each word, create a hash map to count the frequency of each letter in the word.
  4. Compare the frequency of letters in the word with the frequency of letters in the `licensePlate`. If the word contains all the letters in the `licensePlate`, update the result.
  5. Keep track of the shortest word that meets the condition and return it.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

std::string shortestCompletingWord(std::string licensePlate, std::vector<std::string>& words) {
    // Preprocess the licensePlate
    std::unordered_map<char, int> licensePlateLetters;
    for (char c : licensePlate) {
        if (c >= 'a' && c <= 'z') {
            licensePlateLetters[c]++;
        } else if (c >= 'A' && c <= 'Z') {
            licensePlateLetters[c + 32]++;
        }
    }

    // Initialize the result
    std::string result;
    int minLength = INT_MAX;

    // Iterate over each word
    for (std::string word : words) {
        // Create a copy of the licensePlateLetters
        std::unordered_map<char, int> wordLetters = licensePlateLetters;

        // Count the frequency of each letter in the word
        std::unordered_map<char, int> wordCount;
        for (char c : word) {
            if (c >= 'a' && c <= 'z') {
                wordCount[c]++;
            } else if (c >= 'A' && c <= 'Z') {
                wordCount[c + 32]++;
            }
        }

        // Check if the word contains all the letters in the licensePlate
        bool containsAllLetters = true;
        for (auto& pair : wordLetters) {
            if (wordCount[pair.first] < pair.second) {
                containsAllLetters = false;
                break;
            }
        }

        // If the word contains all the letters and is shorter than the current result, update the result
        if (containsAllLetters && word.length() < minLength) {
            result = word;
            minLength = word.length();
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the average length of a word. This is because we iterate over each word and each character in the word.
> - **Space Complexity:** $O(k)$, where $k$ is the number of unique letters in the `licensePlate`. This is because we store the letters in a hash map for efficient lookups.
> - **Optimality proof:** This solution is optimal because we only iterate over each word and each character in the word once, and we use a hash map to count the frequency of each letter in the word in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, frequency counting, and string manipulation.
- Problem-solving patterns identified: Preprocessing the input, iterating over each word, and comparing the frequency of letters.
- Optimization techniques learned: Using hash maps to count the frequency of each letter in the word in constant time.
- Similar problems to practice: Other string manipulation problems, such as finding the longest common prefix or suffix.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle case sensitivity, not checking for empty words or `licensePlate`, and not handling edge cases.
- Edge cases to watch for: Empty words or `licensePlate`, words with different lengths, and words with different frequencies of letters.
- Performance pitfalls: Using inefficient data structures, such as arrays or linked lists, instead of hash maps.
- Testing considerations: Testing with different inputs, such as empty words or `licensePlate`, and testing with different edge cases.