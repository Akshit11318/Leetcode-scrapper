## Minimum Number of Pushes to Type Word II

**Problem Link:** https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description

**Problem Statement:**
- Input format: The input consists of a string `word` containing only uppercase letters.
- Constraints: The length of `word` is in the range $[1, 10^5]$.
- Expected output format: The minimum number of pushes to type `word` using a keyboard with a shift key.
- Key requirements and edge cases to consider:
  - The shift key toggles the keyboard between uppercase and lowercase modes.
  - The keyboard starts in uppercase mode.
  - Each character in the word is typed by pressing the corresponding key on the keyboard.
  - If the character is uppercase, it can be typed directly if the keyboard is in uppercase mode. Otherwise, it requires a push of the shift key before typing.
  - If the character is lowercase, it can be typed directly if the keyboard is in lowercase mode. Otherwise, it requires a push of the shift key before typing.
- Example test cases with explanations:
  - For the input "WWhh", the minimum number of pushes is 2 because we need to push the shift key twice to type the lowercase letters.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible combinations of pushes and no-pushes for each character in the word.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for the minimum number of pushes.
  2. Iterate through each character in the word.
  3. For each character, check if it is uppercase or lowercase.
  4. If the character is uppercase and the keyboard is in lowercase mode, increment the counter and toggle the keyboard mode.
  5. If the character is lowercase and the keyboard is in uppercase mode, increment the counter and toggle the keyboard mode.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that tries all possible scenarios.

```cpp
int minPushes(string word) {
    int n = word.size();
    int pushes = 0;
    bool isUpper = true; // Initially in uppercase mode

    for (int i = 0; i < n; i++) {
        if (isUpper && word[i] >= 'a' && word[i] <= 'z') {
            pushes++;
            isUpper = false;
        } else if (!isUpper && word[i] >= 'A' && word[i] <= 'Z') {
            pushes++;
            isUpper = true;
        }
    }

    return pushes;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `word`, because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the counter and the keyboard mode.
> - **Why these complexities occur:** The time complexity is linear because we process each character in the input string once. The space complexity is constant because we use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves maintaining a running count of the number of pushes required based on the current keyboard mode and the case of the characters in the word.
- Detailed breakdown of the approach:
  1. Initialize a counter for the minimum number of pushes.
  2. Initialize a variable to track the current keyboard mode (uppercase or lowercase).
  3. Iterate through each character in the word.
  4. For each character, check if it is uppercase or lowercase and update the counter and keyboard mode accordingly.
- Proof of optimality: This approach is optimal because it makes a single pass through the input string and uses a constant amount of space, resulting in the best possible time and space complexities for this problem.

```cpp
int minPushes(string word) {
    int n = word.size();
    int pushes = 0;
    bool isUpper = true; // Initially in uppercase mode

    for (int i = 0; i < n; i++) {
        if (isUpper && word[i] >= 'a' && word[i] <= 'z') {
            pushes++;
            isUpper = false;
        } else if (!isUpper && word[i] >= 'A' && word[i] <= 'Z') {
            pushes++;
            isUpper = true;
        }
    }

    return pushes;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `word`, because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the counter and the keyboard mode.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time and space complexities for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Single-pass iteration, constant space usage, and conditional updates based on character case and keyboard mode.
- Problem-solving patterns identified: Maintaining a running count and updating it based on specific conditions.
- Optimization techniques learned: Using a single pass through the input and minimizing space usage.
- Similar problems to practice: Other string manipulation problems involving conditional updates and single-pass iterations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the counter or keyboard mode based on character case.
- Edge cases to watch for: Handling the first character in the word and transitioning between uppercase and lowercase modes.
- Performance pitfalls: Using unnecessary data structures or making multiple passes through the input string.
- Testing considerations: Verifying the correctness of the solution for different input cases, including words with varying lengths and combinations of uppercase and lowercase characters.