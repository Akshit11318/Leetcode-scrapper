## Single Row Keyboard
**Problem Link:** https://leetcode.com/problems/single-row-keyboard/description

**Problem Statement:**
- Input format and constraints: Given a string `word` and a string `keyboard`, return the minimum time it takes to type `word` using the keyboard. The keyboard is a single row of characters.
- Expected output format: The minimum time it takes to type `word`.
- Key requirements and edge cases to consider: The keyboard only contains lowercase English letters, and `word` will only contain lowercase English letters.
- Example test cases with explanations:
  - Input: `word = "abc", keyboard = "cba"` Output: `4` Explanation: The minimum time it takes to type `word` is to move the pointer from `c` to `b` (1 step), then from `b` to `a` (1 step), then from `a` to `c` (1 step) and finally from `c` to `a` (1 step).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each character in the `word` and finding its position in the `keyboard`. Then, we calculate the minimum distance from the previous character to the current character.
- Step-by-step breakdown of the solution:
  1. Initialize the total time to 0.
  2. Initialize the previous character's position to the position of the first character in the `word`.
  3. Iterate over each character in the `word`.
  4. For each character, find its position in the `keyboard`.
  5. Calculate the minimum distance from the previous character to the current character.
  6. Add the minimum distance to the total time.
  7. Update the previous character's position.
- Why this approach comes to mind first: This approach is straightforward and involves iterating over each character in the `word` and calculating the minimum distance to the current character.

```cpp
int calculateTime(string word, string keyboard) {
    int totalTime = 0;
    int prevPos = keyboard.find(word[0]);
    for (int i = 1; i < word.length(); i++) {
        int currPos = keyboard.find(word[i]);
        totalTime += abs(currPos - prevPos);
        prevPos = currPos;
    }
    return totalTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the length of the `word` and $m$ is the length of the `keyboard`. This is because for each character in the `word`, we are finding its position in the `keyboard` which takes $O(m)$ time.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the total time and the previous character's position.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over each character in the `word` and finding its position in the `keyboard`. The space complexity occurs because we are using a constant amount of space to store the total time and the previous character's position.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using the same approach as the brute force solution, but with a slight modification. Instead of using the `find` method to find the position of each character in the `keyboard`, we can create a map to store the position of each character in the `keyboard`. This way, we can find the position of each character in $O(1)$ time.
- Detailed breakdown of the approach:
  1. Create a map to store the position of each character in the `keyboard`.
  2. Initialize the total time to 0.
  3. Initialize the previous character's position to the position of the first character in the `word`.
  4. Iterate over each character in the `word`.
  5. For each character, find its position in the map.
  6. Calculate the minimum distance from the previous character to the current character.
  7. Add the minimum distance to the total time.
  8. Update the previous character's position.
- Proof of optimality: This approach is optimal because we are using a map to store the position of each character in the `keyboard`, which allows us to find the position of each character in $O(1)$ time.

```cpp
int calculateTime(string word, string keyboard) {
    unordered_map<char, int> posMap;
    for (int i = 0; i < keyboard.length(); i++) {
        posMap[keyboard[i]] = i;
    }
    int totalTime = 0;
    int prevPos = posMap[word[0]];
    for (int i = 1; i < word.length(); i++) {
        int currPos = posMap[word[i]];
        totalTime += abs(currPos - prevPos);
        prevPos = currPos;
    }
    return totalTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the `word` and $m$ is the length of the `keyboard`. This is because we are creating a map to store the position of each character in the `keyboard`, which takes $O(m)$ time, and then iterating over each character in the `word`, which takes $O(n)$ time.
> - **Space Complexity:** $O(m)$, as we are using a map to store the position of each character in the `keyboard`.
> - **Optimality proof:** This approach is optimal because we are using a map to store the position of each character in the `keyboard`, which allows us to find the position of each character in $O(1)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a map to store the position of each character in the `keyboard` to reduce the time complexity.
- Problem-solving patterns identified: Using a map to store the position of each character in the `keyboard` to reduce the time complexity.
- Optimization techniques learned: Using a map to store the position of each character in the `keyboard` to reduce the time complexity.
- Similar problems to practice: Problems that involve finding the position of each character in a string, such as the "Find All Anagrams in a String" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not using a map to store the position of each character in the `keyboard`, which can lead to a higher time complexity.
- Edge cases to watch for: The `word` and `keyboard` can be empty, which should be handled accordingly.
- Performance pitfalls: Not using a map to store the position of each character in the `keyboard`, which can lead to a higher time complexity.
- Testing considerations: The `word` and `keyboard` can be of different lengths, which should be handled accordingly.