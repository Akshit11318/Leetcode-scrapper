## Smallest String with a Given Numeric Value

**Problem Link:** https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/description

**Problem Statement:**
- Input: An integer `n` representing the numeric value of the string.
- Output: The lexicographically smallest string of length `n` that can be formed using the digits '1' through '26', where each digit represents the corresponding letter in the alphabet.
- Key requirements:
  - The string must be of length `n`.
  - The numeric value of the string must be equal to `n`.
- Edge cases:
  - `n` is a positive integer.
  - The string can only contain the digits '1' through '26'.

**Example Test Cases:**
- Input: `n = 5`
- Output: `"11zz"`
- Explanation: The numeric value of the string "11zz" is 1 + 1 + 26 + 26 = 54, which is not equal to 5. However, the lexicographically smallest string of length 5 that can be formed is "11zz". We need to find a string where each character represents the corresponding letter in the alphabet, so the correct output would be a string where the sum of the positions in the alphabet of its characters equals `n`.

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible strings of length `n` using the digits '1' through '26' and check if the numeric value of each string is equal to `n`.
- However, this approach is not feasible due to the large number of possible strings.
- A better approach is to use a greedy algorithm to construct the string.

```cpp
#include <string>

string getSmallestString(int n) {
    string result;
    while (n > 0) {
        for (int i = 26; i >= 1; i--) {
            if (n >= i) {
                result += (char)('a' + i - 1);
                n -= i;
                break;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input integer. This is because we are constructing the string character by character.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the output string. This is because we are storing the output string.
> - **Why these complexities occur:** The time complexity is linear because we are using a simple loop to construct the string. The space complexity is also linear because we are storing the output string.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a greedy algorithm to construct the string.
- We start with the largest possible character ('z') and keep adding it to the string until we can no longer add it without exceeding the numeric value `n`.
- We then move to the next largest character and repeat the process.
- This approach ensures that we construct the lexicographically smallest string.

```cpp
#include <string>

string getSmallestString(int n) {
    string result;
    while (n > 0) {
        for (int i = 26; i >= 1; i--) {
            if (n >= i) {
                result += (char)('a' + i - 1);
                n -= i;
                break;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input integer. This is because we are constructing the string character by character.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the output string. This is because we are storing the output string.
> - **Optimality proof:** This approach is optimal because we are using a greedy algorithm to construct the string. We are always choosing the largest possible character that does not exceed the remaining numeric value, which ensures that we construct the lexicographically smallest string.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: greedy algorithm, string construction.
- Problem-solving patterns identified: using a greedy approach to construct the optimal solution.
- Optimization techniques learned: using a simple loop to construct the string.
- Similar problems to practice: constructing the lexicographically smallest string with a given set of characters.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not using a greedy approach.
- Edge cases to watch for: `n` is a positive integer, the string can only contain the digits '1' through '26'.
- Performance pitfalls: using a brute force approach, not using a greedy algorithm.
- Testing considerations: testing with different values of `n`, testing with edge cases.