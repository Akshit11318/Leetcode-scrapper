## Minimum Time to Type Word Using Special Typewriter

**Problem Link:** https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description

**Problem Statement:**
- Input format and constraints: The input is a string `word` consisting of lowercase English letters. The length of `word` is between 1 and 100.
- Expected output format: The minimum time in seconds to type out the word using the special typewriter.
- Key requirements and edge cases to consider: 
  - The special typewriter can only type one character at a time.
  - The special typewriter can move the cursor one position to the left or to the right.
  - If the next character is the same as the previous one, it takes 2 seconds to type it.
  - If the next character is different from the previous one, it takes 1 second to type it.
  - If the next character is the same as the previous one and is at the beginning of the word, it takes 2 seconds to type it.
- Example test cases with explanations:
  - Input: `word = "abc"`
    - Output: `3`
    - Explanation: It takes 1 second to type 'a', 1 second to type 'b', and 1 second to type 'c'.
  - Input: `word = "bba"`
    - Output: `4`
    - Explanation: It takes 1 second to type 'b', 2 seconds to type 'b', and 1 second to type 'a'.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over the word and calculate the time to type each character based on whether it is the same as the previous character.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `time` to 0.
  2. Iterate over the word from the second character to the end.
  3. For each character, check if it is the same as the previous character.
  4. If it is the same, add 2 to `time`. Otherwise, add 1 to `time`.
  5. Return `time` plus 1 (for the first character).

```cpp
int minTimeToType(string word) {
    int time = 1; // 1 second for the first character
    for (int i = 1; i < word.size(); i++) {
        if (word[i] == word[i - 1]) {
            time += 2;
        } else {
            time += 1;
        }
    }
    return time;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the word, because we are iterating over the word once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the time.
> - **Why these complexities occur:** The time complexity is linear because we are iterating over the word once. The space complexity is constant because we are using a constant amount of space to store the time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, because the problem is already quite simple and efficient.
- Detailed breakdown of the approach: Same as the brute force approach.
- Proof of optimality: The time complexity is already linear, which is the best we can do because we have to iterate over the word at least once.

```cpp
int minTimeToType(string word) {
    int time = 1; // 1 second for the first character
    for (int i = 1; i < word.size(); i++) {
        if (word[i] == word[i - 1]) {
            time += 2;
        } else {
            time += 1;
        }
    }
    return time;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the word, because we are iterating over the word once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the time.
> - **Optimality proof:** The time complexity is already linear, which is the best we can do because we have to iterate over the word at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements.
- Problem-solving patterns identified: Simple iteration and calculation.
- Optimization techniques learned: None, because the problem is already quite simple and efficient.
- Similar problems to practice: Other string manipulation problems, such as finding the length of the longest substring without repeating characters.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the time variable correctly, not checking for the same character correctly.
- Edge cases to watch for: The first character, the last character, and characters that are the same as the previous one.
- Performance pitfalls: Using unnecessary loops or data structures.
- Testing considerations: Test with different inputs, such as short words, long words, words with many repeating characters, and words with few repeating characters.