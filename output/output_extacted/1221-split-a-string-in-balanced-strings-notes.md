## Split a String in Balanced Strings
**Problem Link:** https://leetcode.com/problems/split-a-string-in-balanced-strings/description

**Problem Statement:**
- Input: A string `s` containing only 'L' and 'R' characters.
- Constraints: $1 \leq s.length \leq 10^5$.
- Expected output: The number of balanced strings that can be formed by splitting the input string `s`.
- Key requirements: A string is considered balanced if it has an equal number of 'L' and 'R' characters.
- Example test cases:
  - Input: `s = "RLRRLLRLRL"` Output: `4`
  - Input: `s = "RLLLLRRRLR"` Output: `3`
  - Input: `s = "LLLLRRRR"` Output: `1`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible substrings of the input string `s`.
- Then, for each substring, check if it's balanced by comparing the counts of 'L' and 'R' characters.
- This approach comes to mind first because it's straightforward and doesn't require any complex data structures or algorithms.

```cpp
class Solution {
public:
    int balancedStringSplit(string s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                string substr = s.substr(i, j - i);
                int L = 0, R = 0;
                for (char c : substr) {
                    if (c == 'L') L++;
                    else R++;
                }
                if (L == R) count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string `s`. This is because we have three nested loops: two for generating substrings and one for counting 'L' and 'R' characters in each substring.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we need to store each substring, which can have up to $n$ characters.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops, and its space complexity is relatively low because we only need to store one substring at a time.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to realize that we don't need to generate all substrings and check if they're balanced. Instead, we can iterate through the string once and keep track of the balance between 'L' and 'R' characters.
- We can use a variable `balance` to keep track of the difference between the counts of 'L' and 'R' characters. When `balance` becomes zero, it means we've found a balanced substring.

```cpp
class Solution {
public:
    int balancedStringSplit(string s) {
        int count = 0, balance = 0;
        for (char c : s) {
            if (c == 'L') balance++;
            else balance--;
            if (balance == 0) count++;
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we only need to iterate through the string once.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input string `s`, making it constant. This is because we only use a constant amount of space to store the `count` and `balance` variables.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input string, and it uses a minimal amount of extra space to keep track of the balance between 'L' and 'R' characters.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, balance tracking, and the importance of avoiding unnecessary computations.
- Problem-solving patterns identified: looking for ways to simplify the problem by avoiding brute force approaches and focusing on key insights that can lead to more efficient solutions.
- Optimization techniques learned: reducing the number of iterations and minimizing extra space usage.
- Similar problems to practice: other string manipulation and balancing problems.

**Mistakes to Avoid:**
- Common implementation errors: off-by-one errors in loop indices, incorrect handling of edge cases (like empty strings), and failing to initialize variables properly.
- Edge cases to watch for: empty strings, strings with only 'L' or only 'R' characters, and strings with an odd length (which cannot be split into balanced substrings).
- Performance pitfalls: using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: thoroughly testing the function with various inputs, including edge cases, to ensure it produces the correct output.