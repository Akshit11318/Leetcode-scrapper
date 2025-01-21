## Shortest Distance to a Character
**Problem Link:** https://leetcode.com/problems/shortest-distance-to-a-character/description

**Problem Statement:**
- Input format: A string `s` and a character `c`.
- Constraints: `1 <= s.length <= 100`, `s` consists of lowercase English letters, `c` is a lowercase English letter.
- Expected output format: An array of integers where each integer is the shortest distance from the corresponding character in `s` to the character `c`.
- Key requirements and edge cases to consider: Handle cases where `c` appears multiple times, does not appear at all, or appears at the start or end of the string.
- Example test cases with explanations:
  - `s = "loveleetcode", c = "e"` should return `[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]`.
  - `s = "aaab", c = "b"` should return `[3, 2, 1, 0]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each character in `s`, find the closest occurrence of `c` by checking all other characters.
- Step-by-step breakdown of the solution:
  1. Iterate over each character in `s`.
  2. For each character, iterate over all other characters to find the closest `c`.
  3. Keep track of the minimum distance found.
- Why this approach comes to mind first: It's a straightforward, intuitive method that checks all possibilities.

```cpp
vector<int> shortestToChar(string s, char c) {
    vector<int> result;
    for (int i = 0; i < s.size(); i++) {
        int minDistance = INT_MAX;
        for (int j = 0; j < s.size(); j++) {
            if (s[j] == c) {
                minDistance = min(minDistance, abs(j - i));
            }
        }
        result.push_back(minDistance);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of `s`, because for each character, we potentially check all other characters.
> - **Space Complexity:** $O(n)$ for storing the result array.
> - **Why these complexities occur:** The nested loop structure leads to quadratic time complexity, and we need to store the result for each character.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all characters for each character, we can make two passes over the string: one from left to right and one from right to left. In each pass, we keep track of the distance to the last seen `c`.
- Detailed breakdown of the approach:
  1. Initialize an array to store the result.
  2. Make a pass from left to right, updating the result array with the distance to the last seen `c`.
  3. Make a pass from right to left, updating the result array with the minimum distance found so far.
- Proof of optimality: This approach ensures we consider all occurrences of `c` in a single pass, leading to linear time complexity.

```cpp
vector<int> shortestToChar(string s, char c) {
    vector<int> result(s.size(), s.size());
    int dist = s.size();
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == c) dist = 0;
        else dist++;
        result[i] = min(result[i], dist);
    }
    dist = s.size();
    for (int i = s.size() - 1; i >= 0; i--) {
        if (s[i] == c) dist = 0;
        else dist++;
        result[i] = min(result[i], dist);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of `s`, because we make two linear passes over the string.
> - **Space Complexity:** $O(n)$ for storing the result array.
> - **Optimality proof:** This is optimal because we must at least read the input string once, and we achieve this lower bound with our two-pass approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, greedy algorithm.
- Problem-solving patterns identified: Breaking down the problem into smaller, more manageable parts (left and right passes).
- Optimization techniques learned: Avoiding unnecessary computations by keeping track of relevant information (distance to last seen `c`).
- Similar problems to practice: Other string manipulation and distance calculation problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, forgetting to reset variables.
- Edge cases to watch for: When `c` does not appear in the string, or when it appears at the start or end.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Thoroughly testing with different edge cases and large inputs to ensure correctness and efficiency.