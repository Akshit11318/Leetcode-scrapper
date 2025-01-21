## Shortest Distance to Target String in a Circular Array

**Problem Link:** https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description

**Problem Statement:**
- Input: A circular array `words` and a target string `target`.
- Constraints: `1 <= words.length <= 10^5`, `1 <= words[i].length <= 10`, `words[i]` consists of lowercase English letters, and `target` consists of lowercase English letters.
- Expected output: The shortest distance to the target string in the circular array.
- Key requirements and edge cases to consider: Handling circular arrays, finding the shortest distance to the target string.

**Example Test Cases:**
- `words = ["hello", "i", "am", "leetcode", "hello"], target = "hello"`: The shortest distance is 0, as the first occurrence of "hello" is at index 0.
- `words = ["a", "b", "leetcode"], target = "leetcode"`: The shortest distance is 2, as the occurrence of "leetcode" is at index 2.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the array and find the first occurrence of the target string. Then, iterate through the array again to find the minimum distance to the target string.
- Step-by-step breakdown:
  1. Iterate through the array to find the first occurrence of the target string.
  2. If the target string is found, iterate through the array again to find the minimum distance to the target string.
  3. Consider the circular nature of the array by checking distances in both clockwise and counterclockwise directions.

```cpp
int getMinDistance(vector<string>& words, string target) {
    int n = words.size();
    int minDistance = INT_MAX;
    for (int i = 0; i < n; i++) {
        if (words[i] == target) {
            for (int j = 0; j < n; j++) {
                if (words[j] == target) {
                    minDistance = min(minDistance, abs(i - j));
                    minDistance = min(minDistance, n - abs(i - j));
                }
            }
        }
    }
    return minDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array, as we are iterating through the array twice.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity is high because we are iterating through the array twice, and the space complexity is low because we are not using any additional space.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to find all occurrences of the target string and store their indices in a separate array.
- Then, iterate through the array and calculate the minimum distance to the target string using the stored indices.
- Consider the circular nature of the array by checking distances in both clockwise and counterclockwise directions.

```cpp
int getMinDistance(vector<string>& words, string target) {
    int n = words.size();
    vector<int> indices;
    for (int i = 0; i < n; i++) {
        if (words[i] == target) {
            indices.push_back(i);
        }
    }
    if (indices.empty()) {
        return -1; // or any other value to indicate that the target is not found
    }
    int minDistance = INT_MAX;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < indices.size(); j++) {
            minDistance = min(minDistance, abs(i - indices[j]));
            minDistance = min(minDistance, n - abs(i - indices[j]));
        }
    }
    return minDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of elements in the array and $k$ is the number of occurrences of the target string, as we are iterating through the array and the indices of the target string.
> - **Space Complexity:** $O(k)$, as we are storing the indices of the target string.
> - **Optimality proof:** This approach is optimal because we are finding all occurrences of the target string and calculating the minimum distance to the target string using the stored indices, which is the most efficient way to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: finding all occurrences of a target string in an array, calculating the minimum distance to the target string in a circular array.
- Problem-solving patterns identified: using a separate array to store the indices of the target string, considering the circular nature of the array.
- Optimization techniques learned: reducing the time complexity by finding all occurrences of the target string and storing their indices, using the stored indices to calculate the minimum distance to the target string.

**Mistakes to Avoid:**
- Common implementation errors: not considering the circular nature of the array, not handling the case where the target string is not found.
- Edge cases to watch for: the target string is not found, the array is empty.
- Performance pitfalls: using a high-time-complexity approach, not optimizing the solution for the given constraints.
- Testing considerations: testing the solution with different inputs, including edge cases and large inputs.