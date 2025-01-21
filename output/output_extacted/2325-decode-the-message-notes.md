## Decode the Message
**Problem Link:** https://leetcode.com/problems/decode-the-message/description

**Problem Statement:**
- Input: `key` and `message`, where `key` is a string that maps to the decoding alphabet and `message` is the encoded string to be decoded.
- Output: The decoded `message`.
- Key requirements:
  - Each character in `key` maps to a unique letter in the alphabet (from 'a' to 'z').
  - The decoding alphabet is derived from `key` and used to decode `message`.
- Edge cases:
  - `key` and `message` are non-empty strings.
  - `key` contains all unique characters.
  - `message` only contains letters (both lowercase and uppercase) and spaces.

**Example Test Cases:**
- `key = "the five boxing wizards jump quickly at dawn", message = "a b c d e f g h i j k l m n o p q r s t u v w x y z"`
- `key = "elbbz", message = "drzab""

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to create a mapping from `key` to the standard alphabet and then use this mapping to decode `message`.
- We iterate through `key` and `message`, building the mapping and decoding the message character by character.
- This approach comes to mind first because it directly addresses the problem statement by creating a custom alphabet based on `key` and applying it to decode `message`.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

std::string decodeMessage(const std::string& key, const std::string& message) {
    std::unordered_map<char, char> mapping;
    char nextChar = 'a';
    
    // Build the mapping from key to the standard alphabet
    for (char c : key) {
        if (c != ' ' && mapping.find(c) == mapping.end()) {
            mapping[c] = nextChar++;
        }
    }
    
    std::string decodedMessage;
    
    // Decode the message using the mapping
    for (char c : message) {
        if (c == ' ') {
            decodedMessage += c;
        } else {
            decodedMessage += mapping[c];
        }
    }
    
    return decodedMessage;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `key` and $m$ is the length of `message`, because we iterate through both strings once.
> - **Space Complexity:** $O(n)$, because in the worst case, we need to store all characters from `key` in the mapping, assuming all characters are unique.
> - **Why these complexities occur:** The time complexity is linear because we only iterate through `key` and `message` once. The space complexity is also linear because we store a mapping of characters from `key`, which in the worst case, could be all unique characters.

---

### Optimal Approach
**Explanation:**
- The key insight is to realize that we can directly map characters from `key` to the standard alphabet without needing an explicit mapping data structure for the decoding process.
- We iterate through `key` and assign each unique character to the next available character in the standard alphabet.
- This approach is optimal because it minimizes the number of iterations and uses a minimal amount of extra space.

```cpp
#include <iostream>
#include <string>

std::string decodeMessage(const std::string& key, const std::string& message) {
    std::string standardAlphabet = "abcdefghijklmnopqrstuvwxyz";
    std::string customAlphabet;
    std::string decodedMessage;
    
    // Build the custom alphabet based on key
    for (char c : key) {
        if (c != ' ' && customAlphabet.find(c) == std::string::npos) {
            customAlphabet += c;
        }
    }
    
    // Decode the message
    for (char c : message) {
        if (c == ' ') {
            decodedMessage += c;
        } else {
            int index = customAlphabet.find(c);
            decodedMessage += standardAlphabet[index];
        }
    }
    
    return decodedMessage;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `key` and $m` is the length of `message`, because we iterate through both strings once.
> - **Space Complexity:** $O(n)$, because we store the custom alphabet, which in the worst case, could be all unique characters from `key`.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through `key` and `message`, and it uses a minimal amount of extra space to store the custom alphabet.

---

### Final Notes
**Learning Points:**
- The importance of understanding the problem constraints and edge cases.
- How to approach string manipulation problems by breaking them down into smaller, manageable parts.
- The use of iterative techniques to build custom mappings or alphabets.

**Mistakes to Avoid:**
- Not handling edge cases properly, such as ignoring spaces in the `key` and `message`.
- Not optimizing the solution by minimizing unnecessary iterations or memory usage.
- Not considering the implications of using certain data structures (like unordered maps) on the overall complexity of the solution.