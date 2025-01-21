## Find Common Characters
**Problem Link:** [https://leetcode.com/problems/find-common-characters/description](https://leetcode.com/problems/find-common-characters/description)

**Problem Statement:**
- Input: A list of strings `A` where each string `A[i]` is non-empty and consists only of lowercase letters.
- Output: A list of strings, where each string is a character that appears in every string in `A`, and the count of each character is the minimum count it appears in any string.
- Expected output format: List of strings.
- Key requirements and edge cases to consider:
  - Handling empty strings or null input.
  - Handling strings with different lengths.
  - Handling strings with no common characters.
- Example test cases with explanations:
  - Input: `["bella","label","roller"]`
    - Output: `["e","l","l"]`
    - Explanation: The characters 'e' and 'l' appear in every string, with 'l' appearing twice in the first and last strings and once in the middle string. The minimum count for 'l' is 1.
  - Input: `["cool","lock","cook"]`
    - Output: `["c","o"]`
    - Explanation: The characters 'c' and 'o' appear in every string.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each character in the first string, check how many times it appears in every other string, and keep track of the minimum count across all strings.
- Step-by-step breakdown of the solution:
  1. Iterate through each character in the first string.
  2. For each character, iterate through the rest of the strings and count its occurrences.
  3. Keep track of the minimum count of each character across all strings.
  4. If a character does not appear in any string, do not include it in the result.
- Why this approach comes to mind first: It directly addresses the requirement of finding common characters and their minimum counts by exhaustively checking each character in each string.

```cpp
vector<string> commonChars(vector<string>& A) {
    if (A.empty()) return {};
    
    vector<string> result;
    for (char c = 'a'; c <= 'z'; ++c) {
        int minCount = INT_MAX;
        for (const string& str : A) {
            int count = 0;
            for (char ch : str) {
                if (ch == c) ++count;
            }
            minCount = min(minCount, count);
        }
        for (int i = 0; i < minCount; ++i) {
            result.push_back(string(1, c));
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$ where $n$ is the number of strings, $m$ is the average length of a string, and $k$ is the number of unique characters (26 for lowercase letters).
> - **Space Complexity:** $O(n \cdot m)$ for storing the result in the worst case.
> - **Why these complexities occur:** The nested loops for each character, string, and character count contribute to the time complexity. The space complexity is due to storing the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating through each character in the alphabet, we can iterate through each character in the first string and then check its count in the rest of the strings. This reduces unnecessary iterations.
- Detailed breakdown of the approach:
  1. Initialize a map to store the count of each character in the first string.
  2. Iterate through the rest of the strings and update the map with the minimum count for each character.
  3. Construct the result by adding each character the number of times it appears in the map.
- Proof of optimality: This approach ensures that we only consider characters that are present in the first string, thus reducing unnecessary iterations over the entire alphabet.

```cpp
vector<string> commonChars(vector<string>& A) {
    if (A.empty()) return {};
    
    vector<int> count(26, 0); // Initialize count for each character
    for (char c : A[0]) {
        count[c - 'a']++; // Count characters in the first string
    }
    
    for (int i = 1; i < A.size(); ++i) {
        vector<int> temp(26, 0);
        for (char c : A[i]) {
            temp[c - 'a']++;
        }
        for (int j = 0; j < 26; ++j) {
            count[j] = min(count[j], temp[j]); // Update with minimum count
        }
    }
    
    vector<string> result;
    for (int i = 0; i < 26; ++i) {
        for (int j = 0; j < count[i]; ++j) {
            result.push_back(string(1, 'a' + i));
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of strings and $m$ is the average length of a string.
> - **Space Complexity:** $O(m)$ for storing the count of characters and the result.
> - **Optimality proof:** This approach minimizes the number of iterations by only considering characters present in the first string and then efficiently updating the counts for the rest of the strings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Character counting, minimum count across multiple strings.
- Problem-solving patterns identified: Iterating through strings and characters, using maps or vectors for efficient counting.
- Optimization techniques learned: Reducing unnecessary iterations by focusing on relevant characters.
- Similar problems to practice: Problems involving string manipulation and character counting.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing counts correctly, not updating minimum counts properly.
- Edge cases to watch for: Empty strings, strings with no common characters.
- Performance pitfalls: Using inefficient data structures or algorithms for counting characters.
- Testing considerations: Thoroughly testing with different input sizes and edge cases.