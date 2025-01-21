## Check if the Sentence is Pangram

**Problem Link:** https://leetcode.com/problems/check-if-the-sentence-is-pangram/description

**Problem Statement:**
- Input format: A string `sentence` containing English letters (both lowercase and uppercase) and non-alphabet characters.
- Constraints: `1 <= sentence.length <= 100`
- Expected output format: A boolean indicating whether the sentence is a pangram.
- Key requirements: A sentence is a pangram if it contains all the letters of the English alphabet at least once.
- Example test cases:
  - Input: `sentence = "The quick brown fox jumps over the lazy dog"`
    - Output: `true`
    - Explanation: The sentence contains all the letters of the English alphabet at least once.
  - Input: `sentence = "hello"`
    - Output: `false`
    - Explanation: The sentence does not contain all the letters of the English alphabet.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each character in the sentence against all the letters of the alphabet to see if it contains every letter at least once.
- Step-by-step breakdown of the solution:
  1. Create a set of all lowercase English letters.
  2. Iterate over each character in the sentence.
  3. For each character, check if it is in the set of English letters.
  4. If it is, remove it from the set.
  5. After iterating over all characters, check if the set is empty. If it is, the sentence is a pangram.

```cpp
class Solution {
public:
    bool checkIfPangram(string sentence) {
        unordered_set<char> alphabet;
        for (char c = 'a'; c <= 'z'; ++c) {
            alphabet.insert(c);
        }
        
        for (char c : sentence) {
            if (alphabet.find(tolower(c)) != alphabet.end()) {
                alphabet.erase(tolower(c));
            }
            if (alphabet.empty()) {
                return true;
            }
        }
        
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the length of the sentence and $m$ is the number of letters in the alphabet (26 in this case). This is because we iterate over the sentence once and over the alphabet once.
> - **Space Complexity:** $O(m)$ for storing the set of alphabet letters.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each character in the sentence and each letter in the alphabet. The space complexity is also linear because we need to store all the letters of the alphabet in the set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of using a set to store the alphabet and removing characters as we find them, we can use a boolean array of size 26 to mark the presence of each letter.
- Detailed breakdown of the approach:
  1. Create a boolean array `seen` of size 26, initialized to `false`.
  2. Iterate over each character in the sentence.
  3. For each character, calculate its index in the `seen` array based on its ASCII value (`c - 'a'` for lowercase letters).
  4. Mark the corresponding index in the `seen` array as `true`.
  5. After iterating over all characters, check if all indices in the `seen` array are `true`. If they are, the sentence is a pangram.

```cpp
class Solution {
public:
    bool checkIfPangram(string sentence) {
        bool seen[26] = {false};
        
        for (char c : sentence) {
            if (c >= 'a' && c <= 'z') {
                seen[c - 'a'] = true;
            } else if (c >= 'A' && c <= 'Z') {
                seen[tolower(c) - 'a'] = true;
            }
        }
        
        for (bool b : seen) {
            if (!b) {
                return false;
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the length of the sentence and $m$ is the number of letters in the alphabet (26 in this case). This is because we iterate over the sentence once and over the `seen` array once.
> - **Space Complexity:** $O(m)$ for storing the `seen` array.
> - **Optimality proof:** This approach is optimal because we only need to iterate over the sentence once and over the alphabet once to determine if the sentence is a pangram. Using a boolean array instead of a set reduces the constant factors in the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a boolean array to keep track of the presence of elements.
- Problem-solving patterns identified: Iterating over the input and using a separate data structure to keep track of the state.
- Optimization techniques learned: Reducing the constant factors in the time complexity by using a boolean array instead of a set.

**Mistakes to Avoid:**
- Common implementation errors: Not handling uppercase letters correctly.
- Edge cases to watch for: Empty input sentence.
- Performance pitfalls: Using a set to store the alphabet letters and removing them as we find them, which has a higher constant factor in the time complexity.
- Testing considerations: Test the function with sentences that are pangrams, not pangrams, and edge cases like empty strings.