## Count Binary Substrings
**Problem Link:** https://leetcode.com/problems/count-binary-substrings/description

**Problem Statement:**
- Input format and constraints: Given a binary string `s` containing only `0`s and `1`s, return the number of binary substrings that have an equal number of `0`s and `1`s.
- Expected output format: An integer representing the count of such substrings.
- Key requirements and edge cases to consider: The input string may contain any number of `0`s and `1`s, and the substrings must have an equal number of `0`s and `1`s.
- Example test cases with explanations: 
    - For the input `"00110011"`, the output should be `6` because the substrings `"01"`, `"10"`, `"1100"`, `"0101"`, `"0110"`, and `"1001"` have an equal number of `0`s and `1`s.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: One way to solve this problem is to check every possible substring of the input string and count the number of `0`s and `1`s in each substring.
- Step-by-step breakdown of the solution: 
    1. Generate all possible substrings of the input string.
    2. For each substring, count the number of `0`s and `1`s.
    3. If the counts are equal, increment the count of valid substrings.
- Why this approach comes to mind first: This approach is straightforward and simple to understand, but it can be inefficient for large input strings.

```cpp
int countBinarySubstrings(string s) {
    int count = 0;
    int n = s.length();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substr = s.substr(i, j - i);
            int zeros = 0, ones = 0;
            for (char c : substr) {
                if (c == '0') zeros++;
                else ones++;
            }
            if (zeros == ones) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. This is because we generate all possible substrings ($O(n^2)$) and for each substring, we count the number of `0`s and `1`s ($O(n)$).
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the substrings.
> - **Why these complexities occur:** The brute force approach has high time complexity because it checks every possible substring, and for each substring, it counts the number of `0`s and `1`s. This results in a cubic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible substrings, we can iterate through the string and maintain a count of consecutive `0`s and `1`s. When we encounter a different character, we update the count and check if the previous count is equal to the current count.
- Detailed breakdown of the approach:
    1. Initialize two counters, one for `0`s and one for `1`s.
    2. Iterate through the string, updating the counters based on the current character.
    3. When the character changes, update the count of valid substrings if the previous count is equal to the current count.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input string, resulting in a linear time complexity.

```cpp
int countBinarySubstrings(string s) {
    int count = 0;
    int prev = 0, curr = 1;
    for (int i = 1; i < s.length(); i++) {
        if (s[i] == s[i - 1]) curr++;
        else {
            count += min(prev, curr);
            prev = curr;
            curr = 1;
        }
    }
    return count + min(prev, curr);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we only need to make a single pass through the string.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input string. This is because we only need to store a constant amount of information.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input string, resulting in a linear time complexity. This is the best possible time complexity for this problem because we must at least read the input string once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, counter maintenance, and substring counting.
- Problem-solving patterns identified: Using counters to keep track of consecutive characters.
- Optimization techniques learned: Reducing the number of iterations and using a single pass through the input string.
- Similar problems to practice: Other string manipulation problems, such as finding the longest common prefix or suffix.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the counters correctly or not checking for the character change.
- Edge cases to watch for: Empty strings or strings with only one character.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Testing the function with different input strings, including edge cases.