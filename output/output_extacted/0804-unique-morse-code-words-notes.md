## Unique Morse Code Words
**Problem Link:** https://leetcode.com/problems/unique-morse-code-words/description

**Problem Statement:**
- Input format: An array of strings `words`.
- Constraints: Each word consists of lowercase English letters.
- Expected output format: The number of unique Morse code words.
- Key requirements and edge cases to consider: The Morse code mapping for each letter, and the uniqueness of the resulting Morse code words.
- Example test cases with explanations:
  - Input: `words = ["gin", "zen", "gig", "msg"]`
  - Output: `2`
  - Explanation: The translation of each word into Morse code is: 
    - "gin" -> "--...-."
    - "zen" -> "--...-."
    - "gig" -> "--...--."
    - "msg" -> "--...--."
    - The unique Morse code words are "--...-." and "--...--.", so the answer is `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can first create a mapping of English letters to their corresponding Morse code. Then, we can translate each word into Morse code and store the results in a set to eliminate duplicates.
- Step-by-step breakdown of the solution:
  1. Create a mapping of English letters to Morse code.
  2. Iterate through each word in the input array.
  3. For each word, translate it into Morse code using the mapping.
  4. Add the translated Morse code to a set.
  5. After iterating through all words, return the size of the set, which represents the number of unique Morse code words.
- Why this approach comes to mind first: It directly addresses the problem by translating each word into Morse code and counting the unique translations.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

int uniqueMorseRepresentations(vector<string>& words) {
    string morse[] = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
    unordered_set<string> unique;

    for (const string& word : words) {
        string code;
        for (char c : word) {
            code += morse[c - 'a'];
        }
        unique.insert(code);
    }

    return unique.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$, where $N$ is the number of words and $M$ is the maximum length of a word. This is because for each word, we iterate through its characters to translate it into Morse code.
> - **Space Complexity:** $O(N \cdot M)$, as we store the translated Morse code for each word in a set.
> - **Why these complexities occur:** The iteration through each character of each word leads to the time complexity, and storing the Morse code translations in a set leads to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already quite efficient for this problem, as it directly translates each word into Morse code and counts the unique translations. The use of an `unordered_set` for storing unique Morse code words is optimal for eliminating duplicates.
- Detailed breakdown of the approach:
  1. Define the Morse code mapping for each letter.
  2. Iterate through each word, translating it into Morse code.
  3. Add each translated Morse code to an `unordered_set`.
  4. Return the size of the set, which represents the number of unique Morse code words.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input array and uses an `unordered_set` for efficient storage and lookup of unique Morse code words.

```cpp
int uniqueMorseRepresentations(vector<string>& words) {
    string morse[] = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
    unordered_set<string> unique;

    for (const string& word : words) {
        string code;
        for (char c : word) {
            code += morse[c - 'a'];
        }
        unique.insert(code);
    }

    return unique.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$, where $N$ is the number of words and $M$ is the maximum length of a word.
> - **Space Complexity:** $O(N \cdot M)$, for storing the translated Morse code words in a set.
> - **Optimality proof:** This is the most efficient approach because it minimizes the number of operations required to translate words into Morse code and count unique translations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of `unordered_set` for efficient storage and lookup of unique elements, and the direct translation of words into Morse code.
- Problem-solving patterns identified: Directly addressing the problem by translating each word into Morse code and counting the unique translations.
- Optimization techniques learned: Using an `unordered_set` for efficient elimination of duplicates.
- Similar problems to practice: Other string manipulation and set-based problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly defining the Morse code mapping or failing to handle edge cases.
- Edge cases to watch for: Empty input array or words with non-lowercase letters.
- Performance pitfalls: Using a less efficient data structure than `unordered_set` for storing unique Morse code words.
- Testing considerations: Thoroughly testing the function with various input arrays, including edge cases.