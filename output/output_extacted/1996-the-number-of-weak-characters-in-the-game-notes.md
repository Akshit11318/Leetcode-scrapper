## The Number of Weak Characters in the Game
**Problem Link:** https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/description

**Problem Statement:**
- Input format: A 2D vector of integers `properties` where each element is a pair of integers representing the `attack` and `defense` of a character.
- Constraints: The length of `properties` will be in the range [1, 10^5].
- Expected output format: An integer representing the number of weak characters.
- Key requirements and edge cases to consider: A character is weak if there is a stronger or same-strength character with more defense. We need to count the number of such weak characters.
- Example test cases with explanations:
  - Example 1: Input: `properties = [[5,5],[6,3],[3,6]]`, Output: `0`. Explanation: No character is weak.
  - Example 2: Input: `properties = [[2,2],[3,3]]`, Output: `1`. Explanation: The first character is weak because the second character has the same attack but more defense.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine if a character is weak, we can compare it with every other character. If we find a character that has more attack (or the same attack and more defense), then the current character is weak.
- Step-by-step breakdown of the solution:
  1. Iterate through each character in `properties`.
  2. For each character, compare it with every other character in `properties`.
  3. If a character is found to be stronger or have the same strength but more defense, mark the current character as weak.
  4. Count the number of weak characters.

```cpp
int numberOfWeakCharacters(vector<vector<int>>& properties) {
    int weakCount = 0;
    for (int i = 0; i < properties.size(); i++) {
        bool isWeak = false;
        for (int j = 0; j < properties.size(); j++) {
            if (i != j && properties[j][0] > properties[i][0] && properties[j][1] > properties[i][1]) {
                isWeak = true;
                break;
            } else if (i != j && properties[j][0] == properties[i][0] && properties[j][1] > properties[i][1]) {
                isWeak = true;
                break;
            }
        }
        if (isWeak) {
            weakCount++;
        }
    }
    return weakCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of characters. This is because we are using a nested loop to compare each character with every other character.
> - **Space Complexity:** $O(1)$, excluding the space required for the input. This is because we are only using a constant amount of space to store the count of weak characters.
> - **Why these complexities occur:** The time complexity is quadratic because of the nested loop, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing each character with every other character, we can sort the characters based on their attack and then iterate through them to find weak characters.
- Detailed breakdown of the approach:
  1. Sort `properties` in ascending order based on attack and in descending order based on defense when attacks are equal.
  2. Initialize the maximum defense seen so far to 0.
  3. Iterate through the sorted `properties`.
  4. For each character, if its defense is less than the maximum defense seen so far, it is a weak character. Increment the count of weak characters.
  5. Update the maximum defense seen so far.

```cpp
int numberOfWeakCharacters(vector<vector<int>>& properties) {
    sort(properties.begin(), properties.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a[0] == b[0]) {
            return a[1] > b[1];
        }
        return a[0] < b[0];
    });
    
    int maxDefense = 0;
    int weakCount = 0;
    for (const auto& property : properties) {
        if (property[1] < maxDefense) {
            weakCount++;
        }
        maxDefense = max(maxDefense, property[1]);
    }
    return weakCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of characters. This is because we are sorting the characters.
> - **Space Complexity:** $O(1)$, excluding the space required for the input. This is because we are only using a constant amount of space to store the count of weak characters and the maximum defense seen so far.
> - **Optimality proof:** This solution is optimal because it reduces the number of comparisons needed to find weak characters. By sorting the characters based on their attack and defense, we can find all weak characters in a single pass through the sorted list.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and comparison.
- Problem-solving patterns identified: Using sorting to reduce the number of comparisons needed.
- Optimization techniques learned: Reducing the time complexity by sorting the input and then iterating through it.
- Similar problems to practice: Other problems that involve comparing elements in a list, such as finding the maximum or minimum element.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input list.
- Edge cases to watch for: Characters with the same attack and defense.
- Performance pitfalls: Using a nested loop to compare each character with every other character, resulting in a time complexity of $O(n^2)$.
- Testing considerations: Testing the solution with different inputs, including edge cases and large inputs, to ensure that it works correctly and efficiently.