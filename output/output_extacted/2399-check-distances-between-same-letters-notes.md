## Check Distances Between Same Letters

**Problem Link:** https://leetcode.com/problems/check-distances-between-same-letters/description

**Problem Statement:**
- Input: a string `s` containing lowercase English letters.
- Output: a boolean indicating whether the distance between each pair of identical letters is the same.
- Key requirements:
  - Compare the distances between all pairs of the same letter.
  - Return `true` if all distances are consistent for each letter, `false` otherwise.
- Edge cases:
  - Single character strings.
  - Strings with unique characters.
- Example test cases:
  - `s = "abba"` returns `true`.
  - `s = "abcd"` returns `true`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every pair of identical letters in the string.
- For each unique letter, calculate the distance between all pairs of occurrences.
- Compare these distances to determine if they are consistent.

```cpp
bool checkDistancesBetweenSameLetters(string s) {
    unordered_map<char, vector<int>> charIndices;
    for (int i = 0; i < s.size(); ++i) {
        charIndices[s[i]].push_back(i);
    }

    for (auto& pair : charIndices) {
        if (pair.second.size() < 2) continue; // Less than 2 occurrences, no distance to check

        int expectedDistance = pair.second[1] - pair.second[0];
        for (int i = 2; i < pair.second.size(); ++i) {
            if (pair.second[i] - pair.second[i-1] != expectedDistance) return false;
        }
    }

    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the string and $m$ is the maximum number of occurrences of any character. This is because in the worst case, we might need to iterate over the entire string for each unique character, and for each character, we might need to check all its occurrences.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every index of the string in the `charIndices` map.
> - **Why these complexities occur:** The brute force approach involves iterating over the string to find the indices of each character and then checking the distances between these indices. This results in a time complexity that is linear with respect to the string length and the number of occurrences of each character.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we can use a single pass through the string to calculate the distances between all pairs of identical letters.
- For each character, we only need to store the index of its last occurrence to calculate the distance.
- If we encounter a character that we've seen before, we can immediately calculate the distance and compare it with the expected distance for that character.

```cpp
bool checkDistancesBetweenSameLetters(string s) {
    unordered_map<char, int> lastSeen;
    unordered_map<char, int> distance;

    for (int i = 0; i < s.size(); ++i) {
        if (lastSeen.find(s[i]) != lastSeen.end()) {
            int dist = i - lastSeen[s[i]];
            if (distance.find(s[i]) != distance.end() && distance[s[i]] != dist) {
                return false;
            } else {
                distance[s[i]] = dist;
            }
        }
        lastSeen[s[i]] = i;
    }

    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we make a single pass through the string.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every character in the `lastSeen` and `distance` maps.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input string, minimizing the time complexity. The space complexity is also optimal because we must store information about each character's last seen index and its distance to ensure correctness.

---

### Final Notes

**Learning Points:**
- **Hash tables** (`unordered_map`) are useful for storing and looking up data efficiently.
- **Single pass algorithms** can significantly improve performance by reducing the time complexity.
- **Optimization techniques** like using a single pass and minimizing the number of operations can lead to more efficient solutions.

**Mistakes to Avoid:**
- Not considering the **worst-case scenario** when analyzing time and space complexity.
- Failing to **validate inputs** and handle edge cases.
- Not optimizing the solution by reducing unnecessary operations or using more efficient data structures.