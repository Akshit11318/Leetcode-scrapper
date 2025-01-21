## Count Substrings with K Frequency Characters II

**Problem Link:** https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/description

**Problem Statement:**
- Input format and constraints: Given a string `s` and an integer `k`, find the number of substrings where every character appears `k` times.
- Expected output format: The number of substrings where every character appears `k` times.
- Key requirements and edge cases to consider: Handle cases where `k` is 0 or greater than the length of `s`, and consider substrings of varying lengths.
- Example test cases with explanations:
  - Example 1: Input: `s = "abcabc", k = 2`, Output: `2`. Explanation: The substrings are `"abcabc"` and `"bcb"`.
  - Example 2: Input: `s = "abab", k = 2`, Output: `0`. Explanation: There are no substrings where every character appears 2 times.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible substrings of `s` and for each substring, count the frequency of each character. If all characters appear `k` times, increment the count.
- Step-by-step breakdown of the solution:
  1. Initialize count to 0.
  2. Iterate through all possible substrings of `s`.
  3. For each substring, create a frequency map of characters.
  4. Check if all characters in the substring appear `k` times.
  5. If they do, increment the count.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it has a high time complexity due to the nested loops.

```cpp
int countSubstringsWithKFrequencies(string s, int k) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string substring = s.substr(i, j - i);
            unordered_map<char, int> freqMap;
            for (char c : substring) {
                freqMap[c]++;
            }
            bool isValid = true;
            for (auto &pair : freqMap) {
                if (pair.second != k) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `s`. This is because we have three nested loops: two for iterating through substrings and one for creating the frequency map.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`. This is because we need to store the frequency map for each substring.
> - **Why these complexities occur:** The high time complexity occurs because we are iterating through all possible substrings and creating a frequency map for each one. The space complexity occurs because we need to store the frequency map for each substring.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating through all possible substrings, we can use a sliding window approach to reduce the time complexity.
- Detailed breakdown of the approach:
  1. Initialize count to 0.
  2. Iterate through all possible start indices of substrings.
  3. For each start index, iterate through all possible end indices of substrings.
  4. Use a sliding window approach to create a frequency map of characters in the current substring.
  5. Check if all characters in the substring appear `k` times.
  6. If they do, increment the count.
- Proof of optimality: This approach has a lower time complexity than the brute force approach because we are using a sliding window to reduce the number of iterations.

```cpp
int countSubstringsWithKFrequencies(string s, int k) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        unordered_map<char, int> freqMap;
        for (int j = i; j < s.length(); j++) {
            freqMap[s[j]]++;
            bool isValid = true;
            for (auto &pair : freqMap) {
                if (pair.second != k) {
                    isValid = false;
                    break;
                }
            }
            if (isValid && freqMap.size() > 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `s`. This is because we have two nested loops: one for iterating through start indices and one for iterating through end indices.
> - **Space Complexity:** $O(n)$, where $n` is the length of `s`. This is because we need to store the frequency map for each substring.
> - **Optimality proof:** This approach is optimal because we are using a sliding window to reduce the number of iterations, resulting in a lower time complexity than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, frequency maps, and substring iteration.
- Problem-solving patterns identified: Reducing time complexity by using a sliding window approach.
- Optimization techniques learned: Using a sliding window to reduce the number of iterations.
- Similar problems to practice: Other substring problems, such as finding the longest substring with a certain property.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as when `k` is 0 or greater than the length of `s`.
- Edge cases to watch for: Handling cases where `k` is 0 or greater than the length of `s`, and considering substrings of varying lengths.
- Performance pitfalls: Not using a sliding window approach, resulting in a high time complexity.
- Testing considerations: Testing with different inputs, including edge cases, to ensure the solution is correct.