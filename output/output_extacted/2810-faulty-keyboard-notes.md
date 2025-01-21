## Faulty Keyboard
**Problem Link:** https://leetcode.com/problems/faulty-keyboard/description

**Problem Statement:**
- Input format: Two strings, `name` and `typed`, where `name` is the intended input and `typed` is the actual input on the faulty keyboard.
- Constraints: Both strings only contain lowercase letters.
- Expected output format: A boolean indicating whether the `typed` string could have been produced by the faulty keyboard.
- Key requirements and edge cases to consider:
  - The faulty keyboard might have multiple faulty keys.
  - A key might be faulty but still produce its original character.
  - The `typed` string might contain extra characters not present in the `name` string.
- Example test cases with explanations:
  - `name = "abc"`, `typed = "abcc"`: Returns `true` because the extra 'c' could be due to a faulty keyboard.
  - `name = "abc"`, `typed = "abcb"`: Returns `false` because the 'b' after 'c' cannot be explained by a faulty keyboard.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each character in the `typed` string and check if it matches the current character in the `name` string or if it could be a faulty version of the next character.
- Step-by-step breakdown of the solution:
  1. Initialize two pointers, one for each string, at the beginning of each string.
  2. Iterate through the `typed` string. For each character:
    - Check if the current character matches the character at the current position in the `name` string. If it does, move the pointer for the `name` string forward.
    - If it doesn't match, check if it could be a faulty version of the next character in the `name` string. If it is, move the pointer for the `name` string forward.
    - If neither condition is met, return `false` because the `typed` string cannot be produced by the faulty keyboard.
  3. After iterating through the `typed` string, check if all characters in the `name` string have been matched. If not, return `false`.
- Why this approach comes to mind first: It's a straightforward, character-by-character comparison that considers the possibility of faulty keys.

```cpp
bool isTypo(string name, string typed) {
    int i = 0, j = 0;
    while (j < typed.size()) {
        if (i < name.size() && name[i] == typed[j]) {
            i++;
            j++;
        } else if (j > 0 && typed[j] == typed[j-1]) {
            j++;
        } else {
            return false;
        }
    }
    return i == name.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the `typed` string, because we're doing a single pass through the `typed` string.
> - **Space Complexity:** $O(1)$, because we're using a constant amount of space to store the pointers and variables.
> - **Why these complexities occur:** The time complexity is linear because we're iterating through the `typed` string once. The space complexity is constant because we're not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but we can optimize the implementation by directly checking for repeated characters in the `typed` string without explicitly checking for matches with the `name` string first.
- Detailed breakdown of the approach:
  1. Initialize two pointers for the `typed` string, one at the current character and one at the next character.
  2. Iterate through the `typed` string, checking for repeated characters that could indicate a faulty key.
  3. Use the `name` string to validate the sequence of characters, ensuring that the `typed` string could have been produced by a faulty keyboard.
- Proof of optimality: This approach is optimal because it still requires a single pass through the `typed` string, and the operations within the loop are constant time.

```cpp
bool isTypo(string name, string typed) {
    int i = 0, j = 0;
    while (j < typed.size()) {
        if (i < name.size() && name[i] == typed[j]) {
            i++;
            j++;
        } else if (j > 0 && typed[j] == typed[j-1]) {
            j++;
        } else {
            return false;
        }
    }
    return i == name.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `typed` string, because we're doing a single pass through the `typed` string.
> - **Space Complexity:** $O(1)$, because we're using a constant amount of space.
> - **Optimality proof:** This is the optimal solution because any algorithm must at least read the input, which takes $O(n)$ time. Our algorithm does this in a single pass, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, pointer manipulation, and conditional checks.
- Problem-solving patterns identified: Checking for repeated characters to handle faulty keys.
- Optimization techniques learned: Directly checking for repeated characters without explicit matching.
- Similar problems to practice: Other string manipulation problems involving faulty or damaged input devices.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for repeated characters, incorrectly handling the end of the `name` string.
- Edge cases to watch for: Empty strings, strings with only one character, strings with all characters being the same.
- Performance pitfalls: Using unnecessary data structures or algorithms with higher time complexities.
- Testing considerations: Thoroughly testing with various input scenarios, including edge cases and large inputs.