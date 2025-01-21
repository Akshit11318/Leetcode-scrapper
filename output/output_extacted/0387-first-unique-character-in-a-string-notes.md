## First Unique Character in a String

**Problem Link:** https://leetcode.com/problems/first-unique-character-in-a-string/description

**Problem Statement:**
- Input format: A non-empty string `s` containing lowercase letters.
- Constraints: The length of `s` is at most $10^5$.
- Expected output format: The index of the first unique character in `s`. If no unique character exists, return `-1`.
- Key requirements and edge cases to consider:
  - Handling strings with repeated characters.
  - Finding the first occurrence of a unique character.
- Example test cases with explanations:
  - `s = "leetcode"`: The first unique character is `"l"`, so return `0`.
  - `s = "loveleetcode"`: The first unique character is `"v"`, so return `2`.
  - `s = "aabbcc"`: No unique character exists, so return `-1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the string and check each character's frequency.
- Step-by-step breakdown of the solution:
  1. Iterate through the string to count the frequency of each character.
  2. Iterate through the string again to find the first character with a frequency of `1`.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by checking each character's frequency.

```cpp
int firstUniqChar(string s) {
    // Count the frequency of each character
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }

    // Find the first character with a frequency of 1
    for (int i = 0; i < s.size(); i++) {
        if (freq[s[i]] == 1) {
            return i;
        }
    }

    // If no unique character exists, return -1
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we iterate through the string twice: once to count the frequency of each character and once to find the first unique character.
> - **Space Complexity:** $O(1)$, since the size of the `unordered_map` is at most $26$ (the number of lowercase letters).
> - **Why these complexities occur:** The time complexity is linear because we iterate through the string twice, and the space complexity is constant because the size of the `unordered_map` is bounded by a constant.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the string to count the frequency of each character and then find the first unique character.
- Detailed breakdown of the approach:
  1. Initialize an `unordered_map` to store the frequency of each character.
  2. Iterate through the string to count the frequency of each character and store it in the `unordered_map`.
  3. Iterate through the string again to find the first character with a frequency of `1`.
- Proof of optimality: This solution has a time complexity of $O(n)$, which is the best possible time complexity because we must at least read the input string once.

```cpp
int firstUniqChar(string s) {
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }

    for (int i = 0; i < s.size(); i++) {
        if (freq[s[i]] == 1) {
            return i;
        }
    }

    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we iterate through the string twice: once to count the frequency of each character and once to find the first unique character.
> - **Space Complexity:** $O(1)$, since the size of the `unordered_map` is at most $26$ (the number of lowercase letters).
> - **Optimality proof:** The time complexity is optimal because we must at least read the input string once, and the space complexity is optimal because we only use a constant amount of space to store the frequency of each character.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency counting, iteration through a string.
- Problem-solving patterns identified: Using a single pass through the string to count the frequency of each character and then finding the first unique character.
- Optimization techniques learned: Using an `unordered_map` to store the frequency of each character.
- Similar problems to practice: Finding the first duplicate character in a string, finding the most frequent character in a string.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `unordered_map` correctly, not checking for the existence of a character in the `unordered_map`.
- Edge cases to watch for: Empty strings, strings with repeated characters.
- Performance pitfalls: Using a slow data structure to store the frequency of each character.
- Testing considerations: Testing the function with different input strings, including edge cases.