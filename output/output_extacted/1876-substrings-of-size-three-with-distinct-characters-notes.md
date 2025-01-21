## Substrings of Size Three with Distinct Characters

**Problem Link:** https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` containing lowercase English letters.
- Expected output format: The output should be a vector of substrings of size three with distinct characters.
- Key requirements and edge cases to consider: The input string may contain duplicate characters, and the length of the input string may vary.
- Example test cases with explanations:
    - Input: "abc"
      Output: ["abc"]
    - Input: "aaaa"
      Output: []
    - Input: "abcabc"
      Output: ["abc", "bca"]

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible substrings of size three and check if each substring has distinct characters.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of size three.
  2. For each substring, check if it has distinct characters by comparing each pair of characters.
  3. If a substring has distinct characters, add it to the result vector.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that involves checking every possible substring.

```cpp
vector<string> findSubstrings(string s) {
    vector<string> result;
    for (int i = 0; i <= s.size() - 3; i++) {
        string substring = s.substr(i, 3);
        if (substring[0] != substring[1] && substring[0] != substring[2] && substring[1] != substring[2]) {
            result.push_back(substring);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the input string and $m$ is the size of the substring (in this case, $m = 3$). The reason is that we are generating all possible substrings and checking each one.
> - **Space Complexity:** $O(n)$, as we need to store the result vector, which can contain up to $n - 2$ substrings (when all substrings have distinct characters).
> - **Why these complexities occur:** The time complexity occurs because we are using a nested loop to generate all substrings, and the space complexity occurs because we need to store the result vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to generate substrings and check for distinct characters.
- Detailed breakdown of the approach:
  1. Initialize a result vector and a sliding window of size three.
  2. Iterate over the input string using the sliding window.
  3. For each window, check if the characters are distinct by comparing each pair of characters.
  4. If the characters are distinct, add the substring to the result vector.
- Proof of optimality: This approach has a linear time complexity because we are only iterating over the input string once, and we are not generating all possible substrings.

```cpp
vector<string> findSubstrings(string s) {
    vector<string> result;
    for (int i = 0; i <= s.size() - 3; i++) {
        if (s[i] != s[i + 1] && s[i] != s[i + 2] && s[i + 1] != s[i + 2]) {
            result.push_back(s.substr(i, 3));
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. The reason is that we are only iterating over the input string once.
> - **Space Complexity:** $O(n)$, as we need to store the result vector, which can contain up to $n - 2$ substrings (when all substrings have distinct characters).
> - **Optimality proof:** This approach is optimal because we are only iterating over the input string once, and we are not generating all possible substrings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, substring generation, and character comparison.
- Problem-solving patterns identified: Using a sliding window to reduce the time complexity of substring generation.
- Optimization techniques learned: Reducing the number of iterations and avoiding unnecessary computations.
- Similar problems to practice: Substring problems, such as finding the longest substring with distinct characters.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input string or a string with less than three characters.
- Edge cases to watch for: Input strings with duplicate characters or substrings with less than three distinct characters.
- Performance pitfalls: Generating all possible substrings, which can lead to a high time complexity.
- Testing considerations: Testing the function with different input strings, including edge cases and large inputs.