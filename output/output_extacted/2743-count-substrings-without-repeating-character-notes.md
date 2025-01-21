## Count Substrings Without Repeating Character
**Problem Link:** https://leetcode.com/problems/count-substrings-without-repeating-character/description

**Problem Statement:**
- Input format and constraints: Given a string `s`, return the number of substrings without repeating characters.
- Expected output format: Integer count of substrings without repeating characters.
- Key requirements and edge cases to consider: 
    - The input string `s` can be empty.
    - The length of the string `s` is at most 10^5.
    - All characters in the string `s` are lowercase English letters.
- Example test cases with explanations:
    - Input: `s = "abcabc"`
      Output: `10`
      Explanation: The substrings without repeating characters are: `"a"`, `"b"`, `"c"`, `"ab"`, `"bc"`, `"ca"`, `"abc"`, `"bca"`, `"cab"`.
    - Input: `s = "aaaaa"`
      Output: `5`
      Explanation: The substrings without repeating characters are: `"a"`, `"a"`, `"a"`, `"a"`, `"a"`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Check every possible substring of the input string `s` to see if it has any repeating characters.
- Step-by-step breakdown of the solution:
    1. Generate all possible substrings of `s`.
    2. For each substring, check if it has any repeating characters.
    3. Count the number of substrings without repeating characters.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem, but it's not efficient for large inputs.

```cpp
int countSubstringsWithoutRepeatingCharacters(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string substring = s.substr(i, j - i);
            if (isSubstringWithoutRepeatingCharacters(substring)) {
                count++;
            }
        }
    }
    return count;
}

bool isSubstringWithoutRepeatingCharacters(string substring) {
    unordered_set<char> charSet;
    for (char c : substring) {
        if (charSet.find(c) != charSet.end()) {
            return false;
        }
        charSet.insert(c);
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string `s`. The outer two loops generate all possible substrings, and the `isSubstringWithoutRepeatingCharacters` function takes $O(k)$ time, where $k$ is the length of the substring. In the worst case, $k$ can be up to $n$.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string `s`. The `charSet` in the `isSubstringWithoutRepeatingCharacters` function uses up to $n$ space in the worst case.
> - **Why these complexities occur:** The brute force approach generates all possible substrings and checks each one for repeating characters, resulting in a high time complexity. The space complexity is due to the use of a set to keep track of characters in each substring.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a sliding window approach to efficiently generate all possible substrings and check for repeating characters.
- Detailed breakdown of the approach:
    1. Initialize a set `charSet` to keep track of characters in the current substring.
    2. Initialize two pointers, `left` and `right`, to the start of the input string `s`.
    3. Move the `right` pointer to the right, adding characters to `charSet` and checking for repeating characters.
    4. When a repeating character is found, move the `left` pointer to the right, removing characters from `charSet`, until the repeating character is removed.
    5. Count the number of substrings without repeating characters.
- Proof of optimality: This approach has a time complexity of $O(n^2)$, which is optimal for this problem because we must generate all possible substrings.

```cpp
int countSubstringsWithoutRepeatingCharacters(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        unordered_set<char> charSet;
        for (int j = i; j < s.length(); j++) {
            if (charSet.find(s[j]) != charSet.end()) {
                break;
            }
            charSet.insert(s[j]);
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string `s`. The outer loop iterates over each character in `s`, and the inner loop iterates over the remaining characters.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string `s`. The `charSet` uses up to $n$ space in the worst case.
> - **Optimality proof:** This approach is optimal because it generates all possible substrings and checks for repeating characters in a single pass, resulting in a time complexity of $O(n^2)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, use of sets to keep track of characters.
- Problem-solving patterns identified: Using a set to efficiently check for repeating characters.
- Optimization techniques learned: Avoiding unnecessary iterations by breaking out of the inner loop when a repeating character is found.
- Similar problems to practice: Other string problems involving substrings and character counting.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the `charSet` or not removing characters from the set when moving the `left` pointer.
- Edge cases to watch for: Empty input string, input string with all repeating characters.
- Performance pitfalls: Using a brute force approach for large inputs, resulting in high time complexity.
- Testing considerations: Testing with different input sizes and edge cases to ensure correctness and performance.