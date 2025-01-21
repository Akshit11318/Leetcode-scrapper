## Shortest Word Distance III

**Problem Link:** https://leetcode.com/problems/shortest-word-distance-iii/description

**Problem Statement:**
- Input: An array of strings `words`, and two different strings `word1` and `word2`.
- Constraints: All words are lowercase and non-empty, and `word1` and `word2` are not the same.
- Expected Output: The shortest distance between `word1` and `word2` in `words`.
- Key Requirements and Edge Cases:
  - If `word1` or `word2` does not exist in `words`, the function should return `-1`.
  - If `word1` and `word2` are the same, the function should return `-1` as per the problem constraints.
- Example Test Cases:
  - Input: `words = ["practice", "makes", "perfect", "coding", "makes"]`, `word1 = "makes"`, `word2 = "coding"`
    - Output: `1`
  - Input: `words = ["practice", "makes", "perfect", "coding", "makes"]`, `word1 = "makes"`, `word2 = "makes"`
    - Output: `-1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the array of words to find the indices of `word1` and `word2`.
- Then, for each index of `word1`, we calculate the distance to the nearest `word2`.
- The minimum distance found is the solution.
- This approach comes to mind first because it directly addresses the problem statement by finding all occurrences of `word1` and `word2` and then calculating distances between them.

```cpp
class Solution {
public:
    int findClosest(vector<string>& words, string word1, string word2) {
        int minDistance = INT_MAX;
        for (int i = 0; i < words.size(); ++i) {
            if (words[i] == word1) {
                for (int j = 0; j < words.size(); ++j) {
                    if (words[j] == word2) {
                        int distance = abs(i - j);
                        if (distance > 0 && distance < minDistance) {
                            minDistance = distance;
                        }
                    }
                }
            }
        }
        return minDistance == INT_MAX ? -1 : minDistance;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of words. This is because in the worst case, we are iterating through the list of words for each word to find `word1` and then again to find `word2`.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The quadratic time complexity arises from the nested loop structure, where for each potential occurrence of `word1`, we are searching through the entire list again for `word2`.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a single pass through the array of words to keep track of the last seen indices of `word1` and `word2`.
- We maintain two variables, `lastWord1` and `lastWord2`, to store the indices of the last occurrences of `word1` and `word2`, respectively.
- As we iterate through the words, we update these variables and calculate the distance between the current word and the last seen word of the other type.
- This approach is optimal because it reduces the time complexity to linear by only requiring a single pass through the data.

```cpp
class Solution {
public:
    int findClosest(vector<string>& words, string word1, string word2) {
        int minDistance = INT_MAX;
        int lastWord1 = -1, lastWord2 = -1;
        for (int i = 0; i < words.size(); ++i) {
            if (words[i] == word1) {
                if (lastWord2 != -1) {
                    minDistance = min(minDistance, i - lastWord2);
                }
                lastWord1 = i;
            } else if (words[i] == word2) {
                if (lastWord1 != -1) {
                    minDistance = min(minDistance, i - lastWord1);
                }
                lastWord2 = i;
            }
        }
        return minDistance == INT_MAX ? -1 : minDistance;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of words. This is because we are making a single pass through the list of words.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the last seen indices and the minimum distance.
> - **Optimality proof:** This solution is optimal because it achieves the minimum possible time complexity for this problem, which is linear. Any algorithm must at least read the input once, resulting in a time complexity of at least $O(n)$.

---

### Final Notes

**Learning Points:**
- The importance of maintaining relevant state (like last seen indices) to avoid unnecessary iterations.
- How to reduce time complexity by combining operations into a single pass through the data.
- The use of `min` and `max` functions to keep track of extreme values (like minimum distance) efficiently.

**Mistakes to Avoid:**
- Assuming nested loops are always necessary for comparing elements in an array.
- Not considering the implications of the problem constraints (e.g., `word1` and `word2` are different) on the solution.
- Failing to optimize the solution by not taking advantage of the problem's structure (e.g., using a single pass).