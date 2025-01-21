## Check if Word Equals Summation of Two Words

**Problem Link:** https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `word` as input and asks if it can be expressed as the summation of two other strings. Each character in the strings represents a numerical value corresponding to its position in the alphabet (a = 1, b = 2, ..., z = 26).
- Expected output format: The function should return `true` if `word` can be expressed as the summation of two other words, and `false` otherwise.
- Key requirements and edge cases to consider: The strings only contain lowercase English letters, and the input `word` is not empty.

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible combinations of strings to see if their summation equals the input `word`.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of the input `word`.
  2. For each pair of substrings, calculate their numerical summation.
  3. Compare the summation with the remaining part of the `word`.
- Why this approach comes to mind first: It's a straightforward, exhaustive approach that guarantees finding a solution if one exists.

```cpp
class Solution {
public:
    bool isSumEqual(string word1, string word2, string word3) {
        int sum1 = 0, sum2 = 0, sum3 = 0;
        for (char c : word1) sum1 += c - 'a' + 1;
        for (char c : word2) sum2 += c - 'a' + 1;
        for (char c : word3) sum3 += c - 'a' + 1;
        return sum1 + sum2 == sum3;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + k)$, where $n$, $m$, and $k$ are the lengths of `word1`, `word2`, and `word3`, respectively. This is because we iterate over each character in the three strings once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the sums.
> - **Why these complexities occur:** The time complexity is linear because we perform a single pass over each string. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution still involves calculating the numerical values of `word1`, `word2`, and `word3`, but it does so in a straightforward manner without unnecessary complexity.
- Detailed breakdown of the approach: Calculate the numerical value of each string by summing the values of its characters.
- Proof of optimality: This approach is optimal because it directly calculates the required values without any unnecessary steps or comparisons.

```cpp
class Solution {
public:
    bool isSumEqual(string word1, string word2, string word3) {
        int sum1 = 0, sum2 = 0, sum3 = 0;
        for (char c : word1) sum1 += c - 'a' + 1;
        for (char c : word2) sum2 += c - 'a' + 1;
        for (char c : word3) sum3 += c - 'a' + 1;
        return sum1 + sum2 == sum3;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + k)$, where $n$, $m$, and $k$ are the lengths of `word1`, `word2`, and `word3`, respectively.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the sums.
> - **Optimality proof:** This is the most efficient solution because it directly calculates the required sums without any unnecessary operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over strings, calculation of numerical values based on character positions in the alphabet.
- Problem-solving patterns identified: Direct calculation of required values, comparison of sums.
- Optimization techniques learned: Avoiding unnecessary complexity, using straightforward approaches when possible.
- Similar problems to practice: Other string manipulation and comparison problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect calculation of character values, incorrect comparison of sums.
- Edge cases to watch for: Empty strings, strings with non-alphabet characters.
- Performance pitfalls: Using overly complex solutions when a straightforward approach is sufficient.
- Testing considerations: Test with various input strings, including edge cases.